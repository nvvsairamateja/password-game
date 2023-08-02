from flask import Flask, render_template, request, jsonify

app = Flask(__name__,)  #template_folder='C:\\Users\\nvvsa\\OneDrive\\Desktop\\Game projects\\PasswordGame\\password-game\\')

@app.route('/')
def index():
    return render_template("pasword.html")

@app.route('/check_password_strength', methods=['POST'])
def check_password_strength():
    password = str(request.form['password'])
    password_length = len(password)

    if password_length >= 5:
        if password.islower():
            response = {'message': 'Your password must include an uppercase letter.'}
        else:
            if not any(chr.isdigit() for chr in password):
                response = {'message': 'Your password must include a number.'}
            else:
                response = {'message': 'Password is strong!'}
    else:
        response = {'message': 'Your password must be at least 5 characters long.'}



    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
