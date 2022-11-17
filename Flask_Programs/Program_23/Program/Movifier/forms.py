#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 15:04:21 2019

@author: jacobwilkins
"""
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import TextAreaField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

class TextSearchForm(FlaskForm): # form for text search
    movieDescription = TextAreaField('Movie description:', 
                                     validators=[DataRequired(), Length(min=1, max=500)])
    numResults = IntegerField('# of results listed:',
                              validators=[DataRequired(), NumberRange(min=1, max=100)])
    submit = SubmitField('Submit')
    
    def __repr__(self): return f"Movie('{self.movieDescription}', '{self.numResults}')"
    
class TextClassifyForm(FlaskForm): # form for text classification
    movieDescription = TextAreaField('Movie description:', 
                                     validators=[DataRequired(), Length(min=1, max=500)])
    submit = SubmitField('Submit')
    
    def __repr__(self): return f"Classify('{self.movieDescription}')"
    
class ImageCaptionForm(FlaskForm): # form for image caption generation
    image = FileField(u'Movie Poster')
    submit = SubmitField('Submit')
    
    def __repr__(self): return f"Caption('{self.image}')"
