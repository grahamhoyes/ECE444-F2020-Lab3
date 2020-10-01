from datetime import datetime
import os

from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment

from forms import NameForm

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "123456")

bootstrap = Bootstrap(app)
moment = Moment(app)


@app.route("/", methods=["GET", "POST"])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get("name")
        if old_name is not None and old_name != form.name.data:
            flash("Looks like you have changed your name!")

        session["name"] = form.name.data

        old_email = session.get("email")
        if old_email is not None and old_email != form.email.data:
            flash("Looks like you have changed your email!")

        session["email"] = form.email.data

        return redirect(url_for("index"))

    return render_template(
        "index.html",
        form=form,
        name=session.get("name"),
        email=session.get("email"),
        current_time=datetime.utcnow(),
    )


@app.route("/user/<name>/")
def user(name):
    return render_template("user.html", name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
