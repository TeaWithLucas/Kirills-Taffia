import mysql.connector
from mysql.connector import errorcode

#ATTEMPTING TO MAKE THE REMOTE DATABASE CONNECTION
try:
	conn = mysql.connector.connect(user="GandhiAndy", password="cheater99", host="teawithlucas.com", database="kirill_game")
	cursor = conn.cursor(dictionary=True)

except mysql.connector.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("Something is wrong with your user name or password")
	elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print("Database does not exist")
	else:
		print(err)

#THIS METHOD FETCHES ALL ROWS IN A DATABASE TABLE AND SEPERATES EACH ROW INTO A LIST OF DICTIONARIES.
#
def fetch_all(stringSQL):
	query = stringSQL
	cursor.execute(query)
	rows = cursor.fetchall()
	return rows

def insert_records(stringSQL, stringData):
	query = stringSQL
	data = stringData
	cursor.execute(query, data)
	conn.commit()

#testing area
#stringSQL = "SELECT * FROM tblCharacters"
#actorsdata = fetch_all(stringSQL)
#print(actorsdata)
#for actor in actorsdata:
#	print(json.loads(actor['CharTags']))
#diction = {'lmargin1':1,'lmargin2':1,'rmargin':1,'foreground':'#24d075','justify':'RIGHT','spacing1':1,'spacing3':1,'font':'Arial'}
#print(json.dumps(diction))