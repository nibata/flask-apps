
from ..auth.users import User
from ..forms.authentication_form import LoginForm
from ..services.login_manager import login_manager
from flask_login import login_user, logout_user, current_user
from flask import render_template, redirect, url_for, request, abort, flash, current_app


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


def login():
    title = "Login"
    if not current_user.is_authenticated:
        form = LoginForm()

        if form.validate_on_submit():
            #user = User.query.filter_by(email=form.email.data).first()

            #if user and user.check_password(form.password.data):
            #    login_user(user)

            #    flash('Welcome', category="success")

            #    return redirect(url_for("default_bp.index"))

            #else:
            #    flash("The password or the email are wrong. Please try again.", category="danger")
            ...

        return render_template('views/login/login.html', form=form, title=title)

    #else:
    #    flash("You are already loged in.", category="info")
    #    return redirect(url_for("default_bp.index"))


def logout():
    logout_user()
    flash('Logged out', category="info")
    return redirect(url_for("default_bp.index"))
