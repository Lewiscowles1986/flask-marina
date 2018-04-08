from flask import Flask
from flask import render_template, flash

from forms import IntervalDelayForm


app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/', methods=('GET', 'POST'))
def intervalDelayForm():
    form = IntervalDelayForm()
    if form.validate_on_submit():
        # We submitted a valid form
        flash(u"Program Executing", 'success')
    else:
        # Errors occurred
        for field, errors in form.errors.items():
            for error in errors:
                flash(u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                ), 'error')
    return render_template('interval-delay-form.html', form=form)
