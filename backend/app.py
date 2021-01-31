from flask import Flask, request, json, render_template
import mysql.connector

app = Flask(__name__)

#app.config['MYSQL_HOST'] = 'database'
#app.config['MYSQL_USER'] = 'admin'
#app.config['MYSQL_PASSWORD'] = 'password'
#app.config['MYSQL_DB'] = 'db'
#db = yaml.load(open('Backend\db.yaml'))
#app.config['MYSQL_HOST'] = db['mysql_host']
#app.config['MYSQL_USER'] = db['mysql_user']
#app.config['MYSQL_PASSWORD'] = db['mysql_password']
#app.config['MYSQL_DB'] = db['mysql_db']

#mysql = MySQL(app)


@app.route('/person', methods = ['POST'])
def insert():    
    mySQL = mysql.connector.connect(host="localhost", user="admin", password="password", database="db")   
    #variables for storing inputted vlaues on html, later sent to D   
    name = request.form['firstname']
    lastname = request.form ['lastname']
    cursor = mySQL.cursor()
    cursor.execute("INSERT INTO persons(Firstname, Lastname) VALUES(%s, %s)", (name, lastname))
    mySQL.commit()
    cursor.close()
    return render_template('insert.html')

@app.route('/persons', methods = ['GET'])
def jsonify():
    mySQL = mysql.connector.connect(host="localhost", user="admin", password="password", database="db")
    query = "select * from persons"
    cursor = mySQL.connection.cursor()
    cursor.execute(query)
    queryResult = cursor.fetchall()
    
    personRegister = []

    for row in queryResult:
        personRegister.append({'PersonID:':row[0], 'Firstname':row[1], 'Lastname':row[2]})
        cursor.close()
        personJson = json.dumps(personRegister, indent=1)
        print(personJson)      

    
    return personJson
    

    
    




if __name__ == "__main__":
    app.run(host='0.0.0.0')