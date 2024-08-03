from datetime import datetime

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, TimeField, SelectField
from wtforms.validators import DataRequired, URL
import csv
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Coffee location on Google Maps (URL)',
                           validators=[DataRequired(), URL(require_tld=True, message='Enter a valid URL')])
    open_time = TimeField('Open Time eg 8:00AM', format='%H:%M', validators=[DataRequired()], default=datetime.now())
    close_time = TimeField('Closing Time eg 5:30PM', format='%H:%M', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating', choices=[('☕️'), ('☕️☕️'), ('☕️☕☕'), ('☕️☕️☕️☕️'), ('☕️☕️☕️☕️☕️')],
                                validators=[DataRequired()])
    wifi_rating = SelectField('Wifi Rating', choices=[('💪'), ('💪💪'), ('💪💪💪'), ('💪💪💪💪'), ('💪💪💪💪💪')],
                              validators=[DataRequired()])
    power_rating = SelectField('Power Rating', choices=[('✘'), ('✘✘'), ('✘✘✘'), ('✘✘✘✘'), ('✘✘✘✘✘')],
                               validators=[DataRequired()])
    submit = SubmitField('Submit')


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        cafe = request.form['cafe']
        location = request.form['location']
        open_time = request.form['open_time']
        close_time = request.form['close_time']
        coffee_rating = request.form['coffee_rating']
        wifi_rating = request.form['wifi_rating']
        power_rating = request.form['power_rating']
        fieldnames = [cafe, location, open_time, close_time, coffee_rating, wifi_rating, power_rating]
        with open('cafe-data.csv', 'a', encoding="utf8", newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow(fieldnames)
        print(cafe, location)
        print("True")
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()

    return render_template('add.html', form=form)


@app.route('/cafes', methods=["GET", "POST"])
def cafes():
    with open('cafe-data.csv', encoding="utf8", newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
