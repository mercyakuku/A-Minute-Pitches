from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SubmitField,TextAreaField,RadioField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError



class PitchForm(FlaskForm):
	title = StringField('Title', validators=[DataRequired()])
	description = TextAreaField("What would you like to pitch?",validators=[DataRequired()])
	category = RadioField('Label', choices=[ ('motivationalpitch','motivationalpitch'), ('interviewpitch','interviewpitch'),('chefspitch','chefspitch'),('hairdressingpitch','hairdressingpitch')],validators=[DataRequired()])
	submit = SubmitField('Submit')

class CommentForm(FlaskForm):
	description = TextAreaField('Add comment',validators=[DataRequired()])
	submit = SubmitField()

class UpvoteForm(FlaskForm):
	submit = SubmitField()


class Downvote(FlaskForm):
	submit = SubmitField()