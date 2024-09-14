from flask import Flask, render_template, request, redirect
import mysql.connector

# Establishing the database connection
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='myroot@123',
    port='3306'  # Change to the correct port
)


# Creating a cursor object
mycursor = mydb.cursor()

# Creating the database if it doesn't exist
mycursor.execute("CREATE DATABASE IF NOT EXISTS flask_crud")
mydb.commit()

# Connecting to the newly created database
mydb = mysql.connector.connect(
    host='localhost', 
    user='root', 
    password='myroot@123',  # Ensure the correct password
    port='3306',
    database='flask_crud'
)
mycursor = mydb.cursor()

# Creating the student table if it doesn't exist
mycursor.execute('''
    CREATE TABLE IF NOT EXISTS student(
        id INT NOT NULL AUTO_INCREMENT, 
        name VARCHAR(20), 
        age VARCHAR(20), 
        subject VARCHAR(20), 
        PRIMARY KEY (id)
    )
''')
mydb.commit()

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    # --------------creating data to database-----------------------
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        subject = request.form['subject']
        
        student = (name, age, subject)

        # Insert query using placeholders
        query = "INSERT INTO student (name, age, subject) VALUES (%s, %s, %s)"
        mycursor.execute(query, student)
        mydb.commit()

        return redirect('/read')
    
    return render_template('index.html')

# ----------------reading data from database------------
@app.route('/read', methods=['GET'])
def read():
    query = "SELECT * FROM student"
    mycursor.execute(query)
    pid= mycursor.fetchall()

    return render_template('read.html', pid=pid)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request, redirect
import mysql.connector

# Establishing the database connection
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='myroot@123',
    port='3306'  # Ensure the correct port
)

# Creating a cursor object
mycursor = mydb.cursor()

# Creating the database if it doesn't exist
mycursor.execute("CREATE DATABASE IF NOT EXISTS flask_crud")
mydb.commit()

# Connecting to the newly created database
mydb = mysql.connector.connect(
    host='localhost', 
    user='root', 
    password='myroot@123',  # Ensure the correct password
    port='3306',
    database='flask_crud'
)
mycursor = mydb.cursor()

# Creating the student table if it doesn't exist
mycursor.execute('''
    CREATE TABLE IF NOT EXISTS student(
        id INT NOT NULL AUTO_INCREMENT, 
        name VARCHAR(20), 
        age VARCHAR(20), 
        subject VARCHAR(20), 
        PRIMARY KEY (id)
    )
''')
mydb.commit()

app = Flask(__name__)

# -------------- Home route to create data -----------------------
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        subject = request.form['subject']
        
        student = (name, age, subject)

        # Insert query using placeholders
        query = "INSERT INTO student (name, age, subject) VALUES (%s, %s, %s)"
        mycursor.execute(query, student)
        mydb.commit()

        return redirect('/read')
    
    return render_template('index.html')

# ---------------- Route to read data from the database -------------------
@app.route('/read', methods=['GET'])
def read():
    query = "SELECT * FROM student"
    mycursor.execute(query)
    students = mycursor.fetchall()

    return render_template('read.html', students=students)

# ----------------Update the data into database------------
@app.route('/update/id', methods=['POST'])
def updata(id):
    if id:
     if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        subject = request.form['subject']
        
        student = (name, age, subject,id)

        # Insert query using placeholders
        query = "UPDATE INTO student (name, age, subject) VALUES (%s, %s, %s)  where id = %s"
        mycursor.execute(query,student)
        mydb.commit()

        return redirect('/read')
    else:
        return render_template('read.html')

