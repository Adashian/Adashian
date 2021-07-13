from flask_wtf import FlaskForm
from wtforms.fields import SelectField, SubmitField, TextAreaField, FloatField
from wtforms.validators import InputRequired, NumberRange, Length


class PaidForm(FlaskForm):
    ''' Формы для html страницы'''
    amount = FloatField('Сумма', validators=[InputRequired(), NumberRange(0.1, 9999)])
    currency = SelectField('Валюта', choices=[(978, 'EUR'), (840, 'USD'), (643, 'RUB')])
    description_field = TextAreaField('Описание товара', [Length(min=0, max=4096)])
    submit = SubmitField('Оплатить')
