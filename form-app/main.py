from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
       
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']

        
        result_data = {
            'First Name': first_name,
            'Last Name': last_name,
            'Email': email,
        }

        
        return render_template('result.html', result=result_data)

if __name__ == '__main__':
    app.run(debug=True)
