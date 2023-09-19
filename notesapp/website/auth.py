from flask import Blueprint, render_template, request, flash

auth =  Blueprint('auth',__name__)


@auth.route('/login',methods=["GET","POST"])
def login():
    return render_template("login.html")


@auth.route('/logout')
def logout():
    return "<p>logout</p>"


@auth.route('/signup',methods=["GET","POST"])
def signup():
    if request.method=='POST':
        email = request.form.get('email')
        firstname=request.form.get('firstname')
        password1=request.form.get('password1')
        password2=request.form.get('password2')
        
        if len(email) <4:
            flash('Email must be greater than 4 characters.', category='success')
        elif len(firstname) <2:
            flash('first name should be greater than 2', category='error')
        elif password1 != password2:
            flash('Passwords are not matched please enter the correct password', category='error')
        elif  len(password1) < 7:
            flash('Passwords should be greater than 7 character', category='error')
        else:
            flash('Your account is succesfully created Please login ', category='success')
    
    return render_template("signup.html")