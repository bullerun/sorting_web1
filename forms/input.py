from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, BooleanField, RadioField, StringField, SelectField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    radio = RadioField('Выберете тип шкафа', choices=['АВР', 'Насосы'], validators=[DataRequired()])
    rated = StringField('Цифры', validators=[DataRequired()])
    nominal = SelectField('Номинал', choices=[('Амперы', 'Амперы'), ('Ваты', 'Ваты')], validators=[DataRequired()])
    submit = SubmitField('Поиск')
