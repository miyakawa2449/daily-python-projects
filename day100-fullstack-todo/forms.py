from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, SelectField, DateField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from models import User

class LoginForm(FlaskForm):
    username = StringField('ユーザー名', validators=[DataRequired()])
    password = PasswordField('パスワード', validators=[DataRequired()])
    remember_me = BooleanField('ログイン状態を保持')

class RegisterForm(FlaskForm):
    username = StringField('ユーザー名', validators=[DataRequired(), Length(min=3, max=80)])
    email = StringField('メールアドレス', validators=[DataRequired(), Email()])
    password = PasswordField('パスワード', validators=[DataRequired(), Length(min=6)])
    password2 = PasswordField('パスワード（確認）', validators=[DataRequired(), EqualTo('password')])
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('このユーザー名は既に使用されています。')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('このメールアドレスは既に登録されています。')

class TodoForm(FlaskForm):
    title = StringField('タイトル', validators=[DataRequired(), Length(max=200)])
    description = TextAreaField('詳細説明（Markdown対応）')
    priority = SelectField('優先度', choices=[
        ('low', '低'),
        ('medium', '中'),
        ('high', '高')
    ], default='medium')
    due_date = DateField('期限', format='%Y-%m-%d', validators=[], render_kw={'type': 'date'})
    image = FileField('画像メモ', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'gif'], '画像ファイルのみアップロード可能です。')])