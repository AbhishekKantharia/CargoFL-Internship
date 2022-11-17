#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 19:44:53 2019

@author: jacobwilkins
"""

from nltk.stem import PorterStemmer
import os
import re
import json
import math
import tempfile
import hashlib

__version__ = (1, 0, 0)

class Textsearch(object):
    
    stopwords = set([
        'a', 'an', 'and', 'are', 'as', 'at', 'be', 'but', 'by',
        'for', 'if', 'in', 'into', 'is', 'it',
        'no', 'not', 'of', 'on', 'or', 's', 'such',
        't', 'that', 'the', 'their', 'then', 'there', 'these',
        'they', 'this', 'to', 'was', 'will', 'with'
    ])
    
    punctuation = re.compile('[~`!@#$%^&*()+={\[}\]|\\:;"\',<.>/?]')
    
    def __init__(self, base_directory):
        
        self.base_directory = base_directory
        self.index_path = os.path.join(self.base_directory, 'index')
        self.docs_path = os.path.join(self.base_directory, 'documents')
        self.stats_path = os.path.join(self.base_directory, 'stats.json')
        self.setup()
    
    def setup(self):
        if not os.path.exists(self.base_directory):
            os.makedirs(self.base_directory)

        if not os.path.exists(self.index_path):
            os.makedirs(self.index_path)

        if not os.path.exists(self.docs_path):
            os.makedirs(self.docs_path)

        return True
    
    def read_stats(self):
        if not os.path.exists(self.stats_path):
            return {
                'version': '.'.join([str(bit) for bit in __version__]),
                'total_docs': 0,
            }

        with open(self.stats_path, 'r') as stats_file:
            return json.load(stats_file)
        
    def write_stats(self, new_stats):
        with open(self.stats_path, 'w') as stats_file:
            json.dump(new_stats, stats_file)

        return True
    
    def increment_total_docs(self):
        current_stats = self.read_stats()
        current_stats.setdefault('total_docs', 0)
        current_stats['total_docs'] += 1
        self.write_stats(current_stats)
        
    def get_total_docs(self):
        current_stats = self.read_stats()
        return int(current_stats.get('total_docs', 0))
    
    def make_tokens(self, blob):
        blob = self.punctuation.sub(' ', blob) #strip the punctuation
        tokens = []
        ps = PorterStemmer()
        
        for token in blob.split():
            
            token = token.lower().strip() #strip whitespace
            token = ps.stem(token) #stem the token

            if not token in self.stopwords: #check for stop words
                tokens.append(token)

        return tokens
    
    def make_ngrams(self, tokens, min_gram = 4, max_gram = 7):
        terms = {}
        
        for position, token in enumerate(tokens):
            for window_length in range(min_gram, min(max_gram + 1, len(token) + 1)):
                
                gram = token[:window_length]
                terms.setdefault(gram, [])

                if not position in terms[gram]:
                    terms[gram].append(position)

        return terms
    
    def hash_name(self, term, length = 6):
        term = term.encode('ascii', errors='ignore')
        
        hashed = hashlib.md5(term).hexdigest()
        return hashed[:length]
    
    def make_segment_name(self, term):
        return os.path.join(self.index_path, "{0}.index".format(self.hash_name(term)))
    
    def parse_record(self, line):
        return line.rstrip().split('\t', 1)
    
    def make_record(self, term, term_info):
        return "{0}\t{1}\n".format(term, json.dumps(term_info, ensure_ascii=False))
    
    def update_term_info(self, orig_info, new_info):
        for doc_id, positions in new_info.items():
            if not doc_id in orig_info:
                orig_info[doc_id] = positions
            else:
                orig_positions = set(orig_info.get(doc_id, []))
                new_positions = set(positions)
                orig_positions.update(new_positions)
                orig_info[doc_id] = list(orig_positions)

        return orig_info
    
    def save_segment(self, term, term_info, update=False):
        seg_name = self.make_segment_name(term)
        new_seg_file = tempfile.NamedTemporaryFile(delete=False)
        written = False
        
        if not os.path.exists(seg_name):
            with open(seg_name, 'w') as seg_file:
                seg_file.write('')

        with open(seg_name, 'r') as seg_file:
            for line in seg_file:
                seg_term, seg_term_info = self.parse_record(line)

                if not written and seg_term > term:
                    new_line = self.make_record(term, term_info)
                    new_seg_file.write(new_line.encode('utf-8'))
                    written = True
                elif seg_term == term:
                    if not update:
                        line = self.make_record(term, term_info)
                    else:
                        new_info = self.update_term_info(json.loads(seg_term_info), term_info)
                        line = self.make_record(term, new_info)

                    written = True

                new_seg_file.write(line.encode('utf-8'))

            if not written:
                line = self.make_record(term, term_info)
                new_seg_file.write(line.encode('utf-8'))

        new_seg_file.close()
        try:
            os.rename(new_seg_file.name, seg_name)
        except OSError:
            os.remove(seg_name)
            os.rename(new_seg_file.name, seg_name)
        return True
    
    def load_segment(self, term):
        seg_name = self.make_segment_name(term)

        if not os.path.exists(seg_name):
            return {}

        with open(seg_name, 'r') as seg_file:
            for line in seg_file:
                seg_term, term_info = self.parse_record(line)

                if seg_term == term:
                    return json.loads(term_info)

        return {}
    
    def make_document_name(self, doc_id):
        return os.path.join(self.docs_path, self.hash_name(doc_id), "{0}.json".format(doc_id))
    
    def save_document(self, doc_id, document, link, poster):
        doc_path = self.make_document_name(doc_id)
        base_path = os.path.dirname(doc_path)

        if not os.path.exists(base_path):
            os.makedirs(base_path)

        with open(doc_path, 'w') as doc_file:
            doc_file.write(json.dumps([link, document, poster], ensure_ascii=False))

        return True
    
    def load_document(self, doc_id):
        doc_path = self.make_document_name(doc_id)

        with open(doc_path, 'r') as doc_file:
            data = json.loads(doc_file.read())

        return data
    
    def index(self, doc_id, document, link, poster):
        if not hasattr(document, 'items'):
            raise AttributeError('You must provide `index` with a document in the form of a dictionary.')

        if not 'text' in document:
            raise KeyError('You must provide `index` with a document with a `text` field in it.')

        doc_id = str(doc_id)
        self.save_document(doc_id, document, link, poster)
        
        tokens = self.make_tokens(document.get('text', ''))
        terms = self.make_ngrams(tokens)

        for term, positions in terms.items():
            self.save_segment(term, {doc_id: positions}, update=True)

        self.increment_total_docs()
        return True
    
    def parse_query(self, query):
        tokens = self.make_tokens(query)
        return self.make_ngrams(tokens)
    
    def collect_results(self, terms):
        per_term_docs = {}
        per_doc_counts = {}

        for term in terms:
            term_matches = self.load_segment(term)

            per_term_docs.setdefault(term, 0)
            per_term_docs[term] += len(term_matches.keys())

            for doc_id, positions in term_matches.items():
                per_doc_counts.setdefault(doc_id, {})
                per_doc_counts[doc_id].setdefault(term, 0)
                per_doc_counts[doc_id][term] += len(positions)

        return per_term_docs, per_doc_counts
    
    def bm25_relevance(self, terms, matches, current_doc, total_docs, curr_len, avg_len, b, k):
        score = b

        for term in terms:
            idf = math.log((total_docs - matches[term] + 0.5) / (matches[term] + 0.5))# / math.log(1.0 + total_docs)
            score = score + (current_doc.get(term, 0) * idf * (k + 1)) / (current_doc.get(term, 0) + k * (1 - b + (b * (curr_len / avg_len))))

        return score
    
    def search(self, query, offset, limit):
        results = {
            'total_hits': 0,
            'results': []
        }

        if not len(query):
            return results

        total_docs = self.get_total_docs()

        if total_docs == 0:
            return results

        terms = self.parse_query(query)
        per_term_docs, per_doc_counts = self.collect_results(terms)
        scored_results = []
        
        total_length = 0.0
        for doc_id, current_doc in per_doc_counts.items():
            total_length += len(current_doc)
        avg_length = total_length / total_docs

        for doc_id, current_doc in per_doc_counts.items():
            scored_results.append({
                'id': doc_id,
                'score': self.bm25_relevance(terms, per_term_docs, current_doc, total_docs, len(current_doc), avg_length, 0.75, 1.2),
            })

        sorted_results = sorted(scored_results, key=lambda res: res['score'], reverse=True)
        results['total_hits'] = len(sorted_results)

        sliced_results = sorted_results[offset:offset + limit]

        for res in sliced_results:
            doc_dict = self.load_document(res['id'])
            doc_dict[1].update(res)
            results['results'].append(doc_dict)

        return results, terms
