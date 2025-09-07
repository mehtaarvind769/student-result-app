from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Apna secret key yahan daal do

# Dummy student database
students = {
    "101": {
        "password": "pass101",
        "name": "Amit",
        "father_name": "Rajesh Kumar",
        "mother_name": "Suman Devi",
        "dob": "12-08-2010",
        "math": 85,
        "science": 90,
        "english": 88
    },
    "102": {
        "password": "pass102",
        "name": "Priya",
        "father_name": "Suresh Meena",
        "mother_name": "Geeta Meena",
        "dob": "22-06-2011",
        "math": 78,
        "science": 80,
        "english": 75
    },
    "103": {
        "password": "pass103",
        "name": "Rahul",
        "father_name": "Manoj Verma",
        "mother_name": "Kavita Verma",
        "dob": "05-09-2009",
        "math": 92,
        "science": 89,
        "english": 94
    }
}

@app.route('/')
def home():
    if 'user' in session:
        roll = session['user']
        student = students.get(roll)
        return render_template('result.html', roll=roll, student=student)
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        roll = request.form['roll']
        password = request.form['password']
        student = students.get(roll)

        if student and student['password'] == password:
            session['user'] = roll
            return redirect(url_for('home'))
        else:
            return "<h3>Invalid Roll No or Password</h3><a href='/login'>Try Again</a>"

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)