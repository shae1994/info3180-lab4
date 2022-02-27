from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms.validators import FileAllowed;
from wtforms.validators import FileField;
from wtforms.validators import FileRequired;

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg','gif']

class UploadForm(FlaskForm):
    img=FileField(validators=[FileAllowed(ALLOWED_EXTENSIONS, 'Please ensure that your image is of an image format.'),FileRequired(),])


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER