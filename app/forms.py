from wsgiref.validate import validator
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from flask_wtf.file import FileField
from flask_wtf.file import FileRequired

class UploadForm(FlaskForm):
    image=FileField(validators=[FileRequired(), FileAllowed(['png', 'jpg'], 'Images only !')])
