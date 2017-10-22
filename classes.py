import time
from functions import *
from tkinter import *

""" These are the classes which are the structures for different objects in the game """
class Actor():
	def __init__(self,tag,speech_color, name='Blank_name', inv=[]):
		self.speech_color = speech_color
		self.tag = tag
		self.name = name
		self.inv = inv
		self.stats = {
			'special': {'str':0, 'per':0, 'end':0, 'cha':0, 'int':0, 'agi':0, 'luc':0},
			'health': {'curh':0, 'maxh':0},
			'level': {'exp':0,'lvl':1,'nxt_lvl':0, 'nxt_exp':0}
		}

		self.stats['special'] = {'str':1, 'per':1, 'end':1, 'cha':1, 'int':1, 'agi':1, 'luc':1}
		self.calc_stats()

	def __init__(self, data):
		#self.speech_color = data['CharID']: 1
		self.fname = data['CharFname']
		self.lname = data['CharLname']
		self.name = self.fname + " " + self.lname
		self.id = self.fname + "_" + self.lname
		self.nickname = data['CharNickname']
		self.location = data['CharLoc']
		self.function = data['CharFunc']
		self.stats = {
			'special': {'str':int(data['CharSTR']), 'per':int(data['CharPER']), 'end':int(data['CharEND']), 'cha':int(data['CharCHA']), 'int':int(data['CharINT']), 'agi':int(data['CharAGI']), 'luc':int(data['CharLUC'])},
			'health': {'curh':0, 'maxh':0},
			'level': {'exp':int(data['CharXP']),'lvl':int(data['CharLevel']),'nxt_lvl':0, 'nxt_exp':0}
		}
		self.tag = self.id
		self.speech_color = data['CharCOL']
		self.inv = []
		self.calc_stats()

	def calc_stats(self):
		cur_maxh = self.stats['health']['maxh']
		cur_curh = self.stats['health']['curh']
		new_maxh = self.stats['level']['lvl'] * 8 + self.stats['special']['end'] * 8
		new_curh = cur_curh + (new_maxh - cur_maxh)
		self.stats['health'] = {'maxh': new_maxh, 'curh': new_curh}

"""The room class. Rooms will for maps which will be assigned to levels. The rooms will determine the story. """

class Location():
	def __init__(self, locname, name, image = "", desc = ""):
		self.locname = locname
		self.name = name
		self.image = image
		self.description = desc

"""The Stage class allows to navigate through the game"""
class Stage():
	def __init__(self, stage_id, name, narration, choices):
		self.stage_id = stage_id
		self.name = name
		self.narration = narration
		self.choices = choices
		self.choicesinput = []
		for choice in choices:
			self.choicesinput.append(choice.lower())

"""The Stage Manager allows to easily change stages, take inputs and display all the outputs"""
class Stage_Manager():
	def __init__(self, gui_obj, all_stages, start_stage, narrator, waittime):
		self.all_stages = all_stages
		self.gui_obj = gui_obj
		self.current_stage = start_stage
		self.stages_availiable = []
		self.remaining_narration = self.current_stage.narration
		self.current_location = []
		self.narrator = narrator
		self.waittime = waittime


	#Will play out the current stage
	def narrate_current_stage(self):
		for narration in self.remaining_narration:
			narration_tag = narration['speaker'].tag
			narration_color = narration['speaker'].speech_color
			output2 = narration['dialog'] + ''
			output = ''
			print(self.change_location(narration['location']))
			if self.change_location(narration['location']):
				if narration['speaker'] == self.narrator:
					output +=  output2 + '\n\n'
					self.gui_obj.add_txt('narration', output, 'center_tag', narration_color)
				else:
					output +=  narration['speaker'].name + ': ' + output2 + '\n\n'
					self.gui_obj.add_txt('narration', output, narration_tag, narration_color)


				self.gui_obj.add_txt('narration', '_____________________________________________________________________\n\n', 'center_tag', 'white')

		self.update_choices()

	#Output choices for stage
	def update_choices(self):
		for choice in self.current_stage.choices:
			print('c = ' + choice)
			self.gui_obj.add_txt('choice', '[' + choice.upper() + ']    \n\n', 'center_tag', self.gui_obj.player.speech_color)


	def take_input(self, input):
		if input == 'exit':
			quit()
		else:
			self.current_stage = self.select_stage(self.current_stage.choices[input])
			self.get_narration()

	def select_stage(self, text):
		for stage in self.all_stages:
			if text == stage.stage_id:
				return stage

	def get_narration(self):
		self.remaining_narration = self.current_stage.narration

	def change_location(self, new_location):
		if self.current_location != new_location:
			self.gui_obj.change_image('loc_img', './assets/' + new_location.image)
			self.gui_obj.update_label('loc_desc', new_location.name)
			self.gui_obj.add_txt('narration', new_location.description + '\n\n', self.narrator.tag, self.narrator.speech_color)
			#self.gui_obj.cur_loc = new_location.name
			self.current_location = new_location
			return False
		else:
			return True

	#def load_loc_description(self):
	#	location_description = self.current_stage.location.description
	#	if not (location_description == ''):
	#		self.current_stage.narration.insert(0, {'speaker':self.narrator, 'dialog':location_description})

class Item():
	def __init__(self, itemid, name, description):
		self.itemid = itemid
		self.name = name
		self.description = description

	def inspect():
		#Print out name, description and hints in narration section
		pass
