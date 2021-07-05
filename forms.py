from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, TextAreaField, FloatField
from wtforms.validators import DataRequired, Length


class PaidForm(FlaskForm):
    amount = FloatField('Введите сумму:', validators=[DataRequired()])
    currency = SelectField('Валюта', choices=[(978, 'EUR'), (840, 'USD'), (643, 'RUB')])
    description_field = TextAreaField('Описание товара', [Length(min=0, max=4096)])
    submit = SubmitField('Оплатить')
