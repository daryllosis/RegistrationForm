# Author: Daryll Osis
# Date: April 9, 2018
# Description: This program is just a registration form that has validations. 
#              has to meet the requirements to be able to register. 


from flask import Flask, render_template, request, redirect, flash
import re

app = Flask(__name__)
app.secret_key = 'denvernuggets'

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm_password']

    #checks if there's a number in the first name
    for x in first_name:
        if x.isdigit():
            flash(f"Can't have a number in the First Name")
            return redirect('/')

    #checks if there's a number in the last name
    for x in last_name:
        if x.isdigit():
            flash(f"Can't have a number in the Last Name")
            return redirect('/')

    #checks if the password is less than 8 characters
    if len(password) < 8:
        flash(f"Password should be more than 8 characters")
        return redirect('/')

    if not EMAIL_REGEX.match(request.form['email']):
        flash(f"Invalid Email Address!")
        return redirect('/')

    #checking if password includes 1 digit and 1 uppercase letter
    numCounter = 0
    upperCounter = 0
    for x in password:
        if x.isdigit():
            numCounter+=1
        if x.isupper():
            upperCounter+=1
    if upperCounter < 1 or numCounter < 1:
        flash(f"Password has to have atleast a digit and an uppercase letter!")
        return redirect('/')

    if password != confirm_password:
        flash(f"Password must match!")
        return redirect('/')

    #check if there's any empty forms
    if len(first_name) < 1 or len(last_name) < 1 or len(email) < 1 or len(password) < 1 or len(confirm_password) < 1:
        flash(f"Everything must be filled out")
    else:
        flash(f"Thank you {first_name} for filling up the survey!")
    return redirect('/')

if __name__ == "__main__":
    #run our server
    app.run(debug=True)