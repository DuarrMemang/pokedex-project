from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, EmailField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class LoginForm(FlaskForm):
    username            = StringField("username", validators=[DataRequired()])
    password            = PasswordField("password", validators=[DataRequired()])
    submit              = SubmitField("login")

class SignUpForm(FlaskForm):
    username            = StringField("username", validators=[DataRequired(), Length(min=4, max=12)])
    fullname            = StringField("full name", validators=[DataRequired(), Length(min=4, max=16)])
    email               = EmailField("email", validators=[DataRequired(), Email()])
    password            = PasswordField("password", validators=[DataRequired()])
    confirm_password    = PasswordField("confirm password", validators=[DataRequired(), EqualTo("password")])
    submit              = SubmitField("sign up")

class EditProfileForm(FlaskForm):
    username            = StringField("username", validators=[DataRequired(), Length(min=4, max=12)])
    fullname            = StringField("full name", validators=[DataRequired(), Length(min=4, max=16)])
    bio                 = StringField("bio")
    profile_pic         = FileField("picture picture", validators=[FileAllowed(["jpg", "png", "jpeg"])])
    submit              = SubmitField("update profile")

class ResetPasswordForm(FlaskForm):
    old_password        = PasswordField("old password", validators=[DataRequired()])
    new_password        = PasswordField("new password", validators=[DataRequired()])
    confirm_new_password = PasswordField("confirm new password", validators=[DataRequired(), EqualTo("new_password")])
    submit              = SubmitField("reset password")

class ForgotPasswordForm(FlaskForm):
    email               = EmailField("email", validators=[DataRequired()])
    #recaptcha           = RecaptchaField()
    submit              = SubmitField("send link verification to email")