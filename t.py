import pyodbc as db

server = 'localhost' 
database = 'student' 
username = 'root' 
password = '' 
cnxn = db.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()