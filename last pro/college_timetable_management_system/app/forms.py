from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class ScheduleForm(FlaskForm):
    day = StringField('Day', validators=[DataRequired()])
    time = StringField('Time', validators=[DataRequired()])
    course_name = StringField('Course Name', validators=[DataRequired()])
    instructor = StringField('Instructor', validators=[DataRequired()])
    submit = SubmitField('Create Schedule')

class AnnouncementForm(FlaskForm):
    content = StringField('Announcement', validators=[DataRequired()])
    submit = SubmitField('Create Announcement')
