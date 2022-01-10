import os
import sys
from flask import Flask, render_template, redirect, request, abort, url_for

from forms.input import LoginForm
from data import db_session
from data.AVR import AVR
from data.contactors import Contactors
from data.busbars import Busbars
from data.disconnector import Disconnector
from data.FuseLinks import FuseLinks

sys.path.append('/home/c/cx56944/myenv/lib/python3.6/site-packages/')
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
application = app


def main():
    db_session.global_init("db/table.sqlite")


@app.route("/index", methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST'])
def index():
    db_sess = db_session.create_session()
    form = LoginForm()
    if form.validate_on_submit():
        all_name_table = [AVR, Busbars, Contactors, Disconnector, FuseLinks]
        d = {
            'AVR': [],
            'Copper busbars': [],
            'Contactors': [],
            'Disconnector': [],
            'FuseLinks': []
        }
        count = 0
        examination = True
        try:
            rated = int(form.rated.data)
        except ValueError:
            examination = False
        if form.radio.data == 'АВР' and examination:
            if form.nominal.data == 'Амперы':
                for i in all_name_table:
                    for j in db_sess.query(i).filter(rated <= i.rated_A).all():
                        d[i.__tablename__].append([j.vendor_code, j.manufacturer, j.rated_A, j.price])
                        count += j.price
            elif form.nominal.data == 'Ваты':
                for i in all_name_table:
                    for j in db_sess.query(i).filter(rated <= i.rated_KW).all():
                        d[i.__tablename__].append([j.vendor_code, j.manufacturer, j.rated_A, j.price])
                        count += j.price
            return render_template("out.html", d=d, nominal=form.nominal.data)
    return render_template("index.html", form=form)


if __name__ == '__main__':
    main()
    app.run(debug=True)
