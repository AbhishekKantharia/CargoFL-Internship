# Import nltk module using the import keyword
import nltk
# Import wordnet from corpus of nltk module using the import keyword
from nltk.corpus import wordnet
# Create an empty list to store the synonyms
synonyms_lst = []
# Create an empty list to store the antonyms
antonyms_lst = []

# Loop in the synsets of the word using the for loop
for syn in wordnet.synsets("good"):
  # Loop in the above  using another nested for loop
    for l in syn.lemmas():
        # Add the synonym of the word to the synonyms list using the append() function
        synonyms_lst.append(l.name())
        # Adding the antonyms to the antonyms list
        if l.antonyms():
            antonyms_lst.append(l.antonyms()[0].name())

# Print all the unique synonyms from the above resultant synonyms list
# using the set() function
print('The synonyms of the word {good}',set(synonyms_lst))
# Print all the unique antonyms from the above resultant antonyms list
# using the set() function
print('The antonyms of the word {good}',set(antonyms_lst))