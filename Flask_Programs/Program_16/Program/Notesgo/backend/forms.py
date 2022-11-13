from wtforms import  StringField, IntegerField, validators
from flask_wtf import Form
class AddNoteForm(Form):
    '''
    Form to add new notes to the database

    subjectTitle, subjectName, chapterName, link, semester
    '''
    subjectTitle = StringField('Subject Title', [validators.Length(min=6, max=15)], render_kw={"placeholder": "Ex: BTCSE-304"})
    subjectName = StringField('Subject Name', [validators.Length(min=4, max=40)], render_kw={"placeholder": "Ex: Data Structure, Applied Mathematics"})
    chapterName = StringField('Chapter Name', [validators.Length(min=4, max=40)], render_kw={"placeholder": "limit: max 40 characters"})
    semester = IntegerField('Semester',render_kw={"placeholder": "Ex: 1,2,e.t.c"})
    link = StringField('link', [validators.Length(min=4, max=120)], render_kw={"placeholder": "Ex: www.linktodrive.com"})
    
    # password = PasswordField('New Password', [
    #     validators.DataRequired(),
    #     validators.EqualTo('confirm', message='Passwords must match')
    # ])
   