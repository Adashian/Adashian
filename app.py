from flask import Flask, render_template, request, redirect
from classes import Pay
from forms import PaidForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'


@app.route('/', methods=['GET', 'POST'])
def main():
    form = PaidForm()
    amount = form.amount.data
    currency = form.currency.data
    description = form.description_field.data
    if request.method == 'POST' and form.validate_on_submit():
        if currency == '978':
            data = Pay(amount=amount, currency=currency, description=description).ptx()
            return render_template('pay.html', data=data)
        elif currency == '840':
            data = Pay(amount=amount, currency=currency, description=description).bill()
            return redirect(data)
        elif currency == '643':
            data = Pay(amount=amount, currency=currency, description=description).invoice()
            method = data['method']
            url = data['url']
            params = data['data']
            return render_template('invoice.html', method=method, url=url, params=params)
    return render_template('main.html', form=form)


if __name__ == '__main__':
    app.run(debug=False)
