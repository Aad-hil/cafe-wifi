from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, URL


class CreateAddReviewForm(FlaskForm):
    name = StringField("Name of the cafe", validators=[DataRequired()])
    location = StringField("Location", validators=[DataRequired()])
    wifi_strength = StringField("Wifi-Strength", validators=[DataRequired()])
    power_outlets = StringField("Number of power outlets", validators=[DataRequired()])
    seating_capacity = IntegerField("Seating capacity",validators=[DataRequired()])
    amenities = StringField("Amenities")
    submit = SubmitField("Add Cafe")
