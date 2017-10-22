import mysql.connector
from mysql.connector import errorcode
from test import *

actor_dictionary = {"CharFname": None , "CharLname": None, "CharNickname": None, "CharLoc": None, "CharFunc": None, "CharLevel": None, 
"CharXP": None, "CharSTR": None, "CharPER": None, "CharEND": None, "CharCHA": None, "CharINT": None, "CharAGI": None, "CharLUC": None, 
"CharTAG": None, "CharCOL": None}


actor_index = {"0": "CharFname", "1": "CharLname", "2": "CharNickname", "3": "CharLoc", "4": "CharFunc", "5": "CharLevel", "6": "CharXP", 
"7": "CharSTR", "8": "CharPER", "9": "CharEND", "10": "CharCHA", "11": "CharINT", "12": "CharAGI", "13": "CharLUC", "14": "CharTAG", "15": "CharCOL" }

#ATTEMPTING TO MAKE THE REMOTE DATABASE CONNECTION
try:
	conn = mysql.connector.connect(user="GandhiAndy", password="cheater99", host="teawithlucas.com", database="kirill_game")
	cursor = conn.cursor()

except mysql.connector.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("Something is wrong with your user name or password")
	elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print("Database does not exist")
	else:
		print(err)

#THIS METHOD FETCHES ALL ROWS IN A DATABASE TABLE AND SEPERATES EACH ROW INTO A LIST OF DICTIONARIES. 
#
def fetch_all(stringSQL, dictionary, index_dict):
	query = stringSQL
	cursor.execute(query)
	rows = cursor.fetchall()
	final_list = []
	string = ""
	for item in rows:
		dictionary[index_dict["0"]] = item[0]
		dictionary[index_dict["1"]] = item[1]
		dictionary[index_dict["2"]] = item[2]
		dictionary[index_dict["3"]] = item[3]
		dictionary[index_dict["4"]] = item[3]
		dictionary[index_dict["5"]] = item[5]
		dictionary[index_dict["6"]] = item[6]
		dictionary[index_dict["7"]] = item[7]
		dictionary[index_dict["8"]] = item[8]
		dictionary[index_dict["9"]] = item[9]
		dictionary[index_dict["10"]] = item[10]
		dictionary[index_dict["11"]] = item[11]
		dictionary[index_dict["12"]] = item[12]
		dictionary[index_dict["13"]] = item[13]
		dictionary[index_dict["14"]] = item[14]
		dictionary[index_dict["15"]] = item[15]
		string = string + " , " + str(dictionary)
	final_list = string.split(" , ")
	final_list.pop(0)
	print(final_list)
	return final_list

def insert_records(stringSQL, stringData):
	query = stringSQL
	data = stringData
	cursor.execute(query, data)
	conn.commit()

