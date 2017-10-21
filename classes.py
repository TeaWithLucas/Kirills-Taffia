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
			'level': {'exp':0,'lvl':0,'nxt_lvl':0, 'nxt_exp':0}
		}

		self.stats['special'] = {'str':1, 'per':1, 'end':1, 'cha':1, 'int':1, 'agi':1, 'luc':1}
		self.calc_stats()

	def calc_stats(self):
		cur_maxh = self.stats['health']['maxh']
		cur_curh = self.stats['health']['curh']
		new_maxh = self.stats['special']['str'] * 20
		new_curh = cur_curh + (new_maxh - cur_maxh)
		self.stats['health'] = {'maxh': new_maxh, 'curh': new_curh}

"""The room class. Rooms will for maps which will be assigned to levels. The rooms will determine the story. """

class Location():
	def __init__(self, name, des, items):
		self.name = name
		self.description = des
		self.items = items

"""The Stage class allows to navigate through the game"""
class Stage():
	def __init__(self,location, stage_id, name, narration, choices):
		self.location = location
		self.stage_id = stage_id
		self.name = name
		self.narration = narration
		self.choices = choices
		self.choicesinput = []
		for choice in choices:
			self.choicesinput.append(choice.lower())

"""The Stage Manager allows to easily change stages, take inputs and display all the outputs"""
class Stage_Manager():
	def __init__(self, all_stages, gui_obj, narrator):
		self.all_stages = all_stages
		self.gui_obj = gui_obj
		self.current_stage = self.all_stages['start']
		self.stages_availiable = []
		self.remaining_narration = self.current_stage.narration
		self.narrator = narrator


	#Will play out the current stage
	def narrate_current_stage(self):
		#Narrate stage
		self.load_loc_description()
		narration = self.remaining_narration
		output = "\n\n"
		narration_tag = narration[0]['speaker'].tag
		narration_color = narration[0]['speaker'].speech_color
		output2 = narration[0]['dialog'] + ''
		if narration[0]['speaker'] == self.narrator:
			output += output2
		else:
			output += narration[0]['speaker'].name + ':\t\t\"' + output2 + '\"'

		self.gui_obj.add_txt('narration', output, narration_tag, narration_color)

		if len(narration) > 1:
			print('Getting more narration')
			self.remaining_narration = narration[1:]
			self.gui_obj.main.after(500, self.narrate_current_stage)
		else:
			print('Now diplay choices')
			self.update_choices()


	#Output choices for stage
	def update_choices(self):
		for i in self.current_stage.choices:
			self.gui_obj.add_txt('choice', '\t\t\t\t' + i.upper() + '\n', self.gui_obj.player.tag, self.gui_obj.player.speech_color)



	def take_input(self, input):
		input_words_list = input.split()
		if input_words_list[0] == 'take':
			print('Take')
			item_name = input_words_list[1]
			print(item_name)
			for i in self.current_stage.location.items:
				print(i.name.lower() + ' == ' + item_name)
				if i.itemid.lower() == item_name:
					print('Removing item')
					self.current_stage.location.items.remove(i)
					self.gui_obj.player.inv.append(i)


		elif input == 'exit':
			quit()
		else:
			if self.check_in_choices(input):
				self.current_stage = self.select_stage(self.current_stage.choices[input])
				self.get_narration()

	def check_in_choices(self, text):
		for choice_txt in self.current_stage.choices:
			if text == choice_txt:
				return True

		return False

	def select_stage(self, text):
		for stage in self.all_stages:
			if text == stage:
				return self.all_stages[stage]

	def get_narration(self):
		self.remaining_narration = self.current_stage.narration

	def load_loc_description(self):
		location_description = self.current_stage.location.description
		if not (location_description == ''):
			self.current_stage.narration.insert(0, {'speaker':self.narrator, 'dialog':location_description})

class Item():
	def __init__(self, itemid, name, description):
		self.itemid = itemid
		self.name = name
		self.description = description

	def inspect():
		#Print out name, description and hints in narration section
		pass
