# from flask import Flask, render_template ,request , redirect
# import  pymysql

# mydb = pymysql.connect(host='localhost',user='root',password='myroot@123',port = 3306)
# mycursor = mydb.cursor()
# if mydb.connect:
#     print("Successfully connected to the database")


# mydb =pymysql.connect(host='localhost',user='root',password='myroot@123',database='flask_crud')
# mycursor=mydb.cursor()
# # mycursor.execute('create table if not exists student(id INT NOT NULL AUTO_INCREMENT,name VARCHAR(20),age VARCHAR(20),subject VARCHAR(20),PRIMARY KEY (id)')
# mydb.commit()

# app = Flask("__name__")
# @app.route('/',methods = ['POST','GET'])
# # --------------creating data to database-----------------------
# def index():
#     if request.method == 'POST':
#         name = request.form['name']
#         age = request.form['name']
#         subject = request.form['age']
        
#         student =(name,age,subject)

#         query = "insert into student(name,age,subject) value ('%s','%s','%s')"
#         mycursor.execute(query%student)
#         mydb.commit()
#         return redirect('/read')
    
#     return render_template('index.html')

# app.run(debug=True)

# # ----------------reading data from database------------
# @app.route('/read',methods = ['GET'])
# def read():
#     query = "SELECT * FROM student"
#     mycursor.execute(query)
#     pid = mycursor.fetchall()
#     return render_template('read.html',pid = pid)

# if __name__ == "__main__":
#     app.run(debug=True)



