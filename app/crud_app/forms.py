# app/crud_app/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from app.models import Farm, Role

class FarmForm(FlaskForm):
    " Form to add or edit farm "
    name = StringField('Name', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    total_field_area = IntegerField('Total Field Area', validators=[NumberRange(min=0)])
    average_temperature = IntegerField('Average Temperature', validators=[NumberRange(min=0)])
    submit = SubmitField('Submit')

class RoleForm(FlaskForm):
    " Form to add or edit role "
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')

class FarmerForm(FlaskForm):
    " Form to add or edit farmers "
    email = StringField('Email', validators=[DataRequired()])
    username = StringField('User name', validators=[DataRequired()])
    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('Last name', validators=[DataRequired()])
    farm = QuerySelectField(query_factory=lambda: Farm.query.all(),
                            get_label="name")
    role = QuerySelectField(query_factory=lambda: Role.query.all(),
                            get_label="name")

    submit = SubmitField('Submit')