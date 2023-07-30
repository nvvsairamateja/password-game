from flask import Flask, render_template, request, jsonify

app = Flask(__name__,)  #template_folder='C:\\Users\\nvvsa\\OneDrive\\Desktop\\Game projects\\PasswordGame\\password-game\\')

@app.route('/')
def index():
    return render_template("pasword.html")

@app.route('/check_password_strength', methods=['POST'])
def check_password_strength():
    password = request.form['password']
    password_length = len(password)

    if password_length >= 8:
        response = {'message': 'Password is strong!'}
    else:
        response = {'message': 'Password is weak. It should be at least 8 characters long.'}

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
