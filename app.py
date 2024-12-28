# from flask import Flask, render_template, request, redirect, url_for, session
# import mysql.connector
# from mysql.connector import Error

# app = Flask(__name__)

# # Set secret key for sessions
# app.secret_key = 'your_secret_key'  # Replace with a strong random value

# # Connect to MySQL Database
# def create_connection():
#         return mysql.connector.connect(
#             host='localhost',
#             database='libr',
#             user='root',  # replace with your MySQL username
#             password='1130'  # replace with your MySQL password
#         )

# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if request.method == 'POST':
#         username = request.form['username']
#         email = request.form['email']
#         password = request.form['password']

#         # Insert user data into database
#         connection = create_connection()
#         cursor = connection.cursor()
#         query = "INSERT INTO users(username, email, password) VALUES (%s, %s, %s)"
#         values = (username, email, password)
#         cursor.execute(query, values)
#         connection.commit()
#         cursor.close()
#         connection.close()

#         return redirect(url_for('login'))

#     return render_template('signup.html')
# @app.route('/login', methods=['GET', 'POST'])
# def login():
    
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']

#         connection = create_connection()
#         cursor = connection.cursor(dictionary=True)
#         query = "SELECT * FROM users WHERE email = %s AND password = %s"
#         values = (email, password)
#         cursor.execute(query,values)
#         user = cursor.fetchone()
#         return render_template('index.html')

#     return render_template('login.html')
# @app.route('/index')
# def index():
#     return render_template('index.html')



# @app.route('/books', methods=['GET', 'POST'])
# def books():
    
#     if request.method == 'POST':
#         title = request.form['title']
#         author = request.form['author']
#         publisher= request.form['publisher']
#         publication_date= request.form['publication_date']
#         # Insert user data into database
#         connection = create_connection()
#         cursor = connection.cursor()
#         query = "INSERT INTO books(Title,Author,Publisher,PublicationDate) VALUES (%s, %s,%s,%s)"
#         values = (title,author,publisher,publication_date) 
#         cursor.execute(query, values)
#         connection.commit()
#         cursor.close()
#         connection.close()

#         return render_template('borrowers.html')

#     return render_template('books.html')

# @app.route('/borrowers', methods=['GET', 'POST'])
# def borrowers():
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         phone_number= request.form['phone_number']
#         address= request.form['address']
        
        

#         # Insert user data into database
#         connection = create_connection()
#         cursor = connection.cursor()
#         query = "INSERT INTO borrowers(Name, Email, PhoneNumber,Address)  VALUES (%s, %s, %s,%s)"
#         values = (name,email,phone_number,address) 
#         cursor.execute(query,values)
#         connection.commit()
#         cursor.close()
#         connection.close()

#         return render_template('fines.html')

#     return render_template('borrowers.html')
# @app.route('/fines',methods=['GET','POST'])
# def fines():
    
#     if request.method == 'POST':
#         bookID = request.form['bookID']
#         borrowerid = request.form['borrowerid']
#         borrowdate = request.form['borrowdate']
#         returndate = request.form['returndate']
#         fineamount= request.form['fineamount']
        

#         # Insert user data into database
#         connection = create_connection()
#         cursor = connection.cursor()
#         query = "INSERT INTO borrowings(BookID,BorrowerID,BorrowDate,ReturnDate,FineAmount)VALUES(%s, %s, %s,%s,%s)"
#         values = (bookID,borrowerid,borrowdate,returndate,fineamount)
#         cursor.execute(query,values)
#         connection.commit()
#         cursor.close()
#         connection.close()

#         return render_template('librarians.html')

#     return render_template('fines.html')

# @app.route('/librarians', methods=['GET','POST'])
# def librarians():
    
#     if request.method == 'POST':
#         name  = request.form['name']
#         email = request.form['email']
#         phoneNumber= request.form['phoneNumber']
#         password= request.form['password']
        
        

#         # Insert user data into database
#         connection = create_connection()
#         cursor = connection.cursor()
#         query = "INSERT INTO librarians(Name, Email , PhoneNumber,Password)VALUES (%s, %s,%s,%s)"
#         values = (name, email,phoneNumber,password)
#         cursor.execute(query,values)
#         connection.commit()
#         cursor.close()
#         connection.close()
#         return render_template('thankyou.html')

#     return render_template('librarians.html')


# if __name__ == '__main__':

#     app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Function to connect to the database
def connect_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",       # Database host
            user="root",    # MySQL username
            password="1130",# MySQL password
            database="libr"     # Database name
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Route to add a new user
@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        
        connection = connect_db()
        if connection:
            cursor = connection.cursor()
            query = "INSERT INTO userss (username, email) VALUES (%s, %s)"
            cursor.execute(query, (username, email))
            connection.commit()
            cursor.close()
            connection.close()
           
    return render_template('add_user.html')

# Route to search and retrieve user details
@app.route('/', methods=['GET', 'POST'])
def index():
    user_data = None
    if request.method == 'POST':
        user_id = request.form['user_id']
        
        if user_id.isdigit():
            connection = connect_db()
            if connection:
                cursor = connection.cursor()
                query = "SELECT * FROM userss WHERE id = %s"
                cursor.execute(query, (user_id,))
                user_data = cursor.fetchone()
                cursor.close()
                connection.close()
        else:
            user_data = "Invalid User ID. Please enter a numeric value."
    
    return render_template('user_details.html', user_data=user_data)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Function to connect to the database
def connect_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",       # Database host
            user="root",    # MySQL username
            password="1130",# MySQL password
            database="libr"     # Database name
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Route to add a new user
@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        
        connection = connect_db()
        if connection:
            cursor = connection.cursor()
            query = "INSERT INTO userss (username, email) VALUES (%s, %s)"
            cursor.execute(query, (username, email))
            connection.commit()
            cursor.close()
            connection.close()
           
    return render_template('add_user.html')

# Route to search and retrieve user details
@app.route('/', methods=['GET', 'POST'])
def index():
    user_data = None
    if request.method == 'POST':
        user_id = request.form['user_id']
        
        if user_id.isdigit():
            connection = connect_db()
            if connection:
                cursor = connection.cursor()
                query = "SELECT * FROM users WHERE id = %s"
                cursor.execute(query, (user_id,))
                user_data = cursor.fetchone()
                cursor.close()
                connection.close()
        else:
            user_data = "Invalid User ID. Please enter a numeric value."
    
    return render_template('user_details.html', user_data=user_data)

if __name__ == '__main__':
    app.run(debug=True)