from wsgiref.validate import validator
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from flask_wtf.file import FileField
from flask_wtf.file import FileRequired

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg','gif']

class UploadForm(FlaskForm):
    img=FileField(validators=[FileAllowed(ALLOWED_EXTENSIONS, 'Please ensure that your file is of an image format.'),FileRequired()])
