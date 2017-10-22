from DBObject import *

# ***WORKING***
#TEST FOR INSERTING RECORDS INTO THE DATABASE
#LINE 7 INCREMENTS THE AUTO-INCREMENT ID FOR CHARID IN THIS INSTANCE
#CharID = cursor.lastrowid
#stringSQL2 = ("INSERT INTO tblCharacters " "(CharID, CharName) " "VALUES (%(CharID)s, %(CharName)s)")
#data = {"CharID": CharID, "CharName": "Dmytro"}
#insert_records(stringSQL2, data)

# ***WORKING*** 
#TEST FOR SELECTING ALL RECORDS FROM A TABLE
stringSQL = "SELECT CharFname, CharLname, CharNickname, CharLoc, CharFunc, CharLevel, CharXP, CharSTR, CharPER, CharEND, CharCHA, CharINT, CharAGI, CharLUC, CharTAG, CharCOL FROM tblCharacters"
fetch_all(stringSQL, actor_dictionary, actor_index)


