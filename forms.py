from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import InputRequired, NumberRange


class IntervalDelayForm(FlaskForm):
    t1 = IntegerField('T1', default=0, validators=[InputRequired(),NumberRange(min=0,max=3600)])
    t2 = IntegerField('T2', default=0, validators=[InputRequired(),NumberRange(min=0,max=3600)])
    t3 = IntegerField('T3', default=0, validators=[InputRequired(),NumberRange(min=0,max=3600)])
    t4 = IntegerField('T4', default=0, validators=[InputRequired(),NumberRange(min=0,max=3600)])
    t5 = IntegerField('T5', default=0, validators=[InputRequired(),NumberRange(min=0,max=3600)])
    t6 = IntegerField('T6', default=0, validators=[InputRequired(),NumberRange(min=0,max=3600)])
    t7 = IntegerField('T7', default=0, validators=[InputRequired(),NumberRange(min=0,max=3600)])
    t8 = IntegerField('T8', default=0, validators=[InputRequired(),NumberRange(min=0,max=3600)])
