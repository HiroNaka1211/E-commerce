from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField
from wtforms.validators import InputRequired, email

# form used in basket
class CheckoutForm(FlaskForm):
    firstname = StringField("Your first name", validators=[InputRequired()])
    lastname = StringField("Your lastname", validators=[InputRequired()])
    email = StringField("Your email", validators=[InputRequired(), email()])
    phone = StringField("Your phone number", validators=[InputRequired()])
    address = StringField("Your address", validators=[InputRequired()])
    submit = SubmitField("Place Order")