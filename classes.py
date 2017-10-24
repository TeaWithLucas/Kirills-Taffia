import time
from functions import *
from tkinter import *
import json

""" These are the classes which are the structures for different objects in the game """
class Actor():
	#Constructor inits the object with data pulled form DB
	def __init__(self, data):
		#self.speech_color = data['CharID']: 1
		self.fname =  str(data['CharFname']).strip()
		self.lname =  str(data['CharLname']).strip()
		self.name = self.fname + " " + self.lname
		self.id = self.fname + "_" + self.lname
		self.nickname =  str(data['CharNickname']).strip()
		self.location =  str(data['CharLoc']).strip()
		self.function =  str(data['CharFunc']).strip()
		self.stats = {
			'special': {'str':int(data['CharSTR']), 'per':int(data['CharPER']), 'end':int(data['CharEND']), 'cha':int(data['CharCHA']), 'int':int(data['CharINT']), 'agi':int(data['CharAGI']), 'luc':int(data['CharLUC'])},
			'health': {'curh':0, 'maxh':0},
			'level': {'exp':int(data['CharXP']),'lvl':int(data['CharLevel']),'nxt_lvl':0, 'nxt_exp':0}
		}
		self.wallet = int(data['CharWallet'])
		self.tag = self.id
		#self.tags = {'foreground':data['CharCOL'].strip()}
		self.tags = json.loads(data['CharTags'])
		if self.tags['justify']=='RIGHT': self.tags['justify']=RIGHT
		elif self.tags['justify']=='LEFT': self.tags['justify']=LEFT
		elif self.tags['justify']=='CENTER': self.tags['justify']=CENTER
		else: self.tags['justify']=LEFT
		self.inv = []
		self.calc_stats()

	#calculates the currect stats of the actor
	def calc_stats(self):
		cur_maxh = self.stats['health']['maxh']
		cur_curh = self.stats['health']['curh']
		new_maxh = self.stats['level']['lvl'] * 8 + self.stats['special']['end'] * 8
		new_curh = cur_curh + (new_maxh - cur_maxh)
		self.stats['health'] = {'maxh': new_maxh, 'curh': new_curh}


"""The Stage class allows to navigate through the game"""
class Stage():
	def __init__(self, stage_id, name, narration, choices):
		self.stage_id = stage_id
		self.name = name
		self.narration = narration #The text to be displayed in this stage (story/dialog)
		self.choices = choices #The choices availiable at the end of this stage
		self.choicesinput = [] #List of choices to filter out bad input
		for choice in choices:
			self.choicesinput.append(choice.lower())

"""The location class allows to navigate through the game map and describe locations in the narration """

class Location():
	#def __init__(self, locname, name, image = "", desc = ""):
		#self.id = locname
		#self.locname = locname
		#self.name = name
		#self.image = image
		#self.description = desc

	#Constructor pulls location data from DB
	def __init__(self, data):
		self.id =  str(data['LocID']).strip()
		self.locname = self.id
		self.name =  str(data['LocName']).strip()
		self.image =  str(data['LocImage']).strip()
		self.description =  str(data['LocID']).strip()
		self.desc = {'short': str(data['LocDescShort']).strip(), 'long1':  str(data['LocDescLong1']).strip(), 'long2':  str(data['LocDescLong2']).strip()}

"""Item class not complete(need to integrate with DB)"""
class Item():
	def __init__(self, itemid, name, description):
		self.itemid = itemid
		self.name = name
		self.description = description

	def inspect():
		#Print out name, description and hints in narration section
		pass
