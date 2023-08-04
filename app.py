from flask import Flask, render_template, request, jsonify
import re


app = Flask(__name__,)  #template_folder='C:\\Users\\nvvsa\\OneDrive\\Desktop\\Game projects\\PasswordGame\\password-game\\')

@app.route('/')
def index():
    return render_template("pasword.html")


def is_month(password):
    months = 'january|february|march|april|may|june|july|august|september|october|november|december'
    return re.search(months, password, re.IGNORECASE)


def check_special_char(password):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if(regex.search(password) == None):
        return True
    else:
        return False


def sum_of_digits(password):
    digits = []
    total = 0
    for chr in password:
        if chr.isdigit():
            digits.append(int(chr))
    total = sum(digits)
    return total


@app.route('/check_password_strength', methods=['POST'])
def check_password_strength():
    password = str(request.form['password'])
    password_length = len(password)

    if password_length < 5:
        response = {'message': 'Your password must be at least 5 characters long.'}
    elif password.islower():
        response = {'message': 'Your password must include an uppercase letter.'}
    elif not any(chr.isdigit() for chr in password):
        response = {'message': 'Your password must include a number.'}
    elif check_special_char(password):
        response = {'message': 'Your password must include a special character.'}
    elif sum_of_digits(password) != 25:
        response = {'message': 'The digits in your password must add up to 25.'}
    elif not is_month(password):
        response = {'message': 'Your password must include a month of the year.'}
    else:
        response = {'message': 'Password is strong!'}


    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
