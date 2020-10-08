from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required, Email, ValidationError


class NameForm(FlaskForm):
    name = StringField("What is your name?", validators=[Required()])
    email = StringField(
        "What is your UofT email address?",
        render_kw={"type": "email"},
        validators=[Required(), Email()],
    )
    submit = SubmitField("Submit")

    def validate_email(self, field):
        if not field.data.endswith("utoronto.ca"):
            raise ValidationError("Please use your UofT email.")
