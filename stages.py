from classes import *

"""The Stage Manager allows to easily change stages, take inputs and display all the outputs"""
class Stage_Manager():
	def __init__(self, gui_obj, all_stages, start_stage, narrator):
		self.all_stages = all_stages
		self.gui_obj = gui_obj
		self.current_stage = start_stage
		self.stages_availiable = []
		self.remaining_narration = self.current_stage.narration
		self.current_location = []
		self.narrator = narrator
		self.linebar = '__________________________________________________________\n'


	#Will play out the current stage
	def narrate_current_stage(self):
		for narration in self.remaining_narration:
			print(self.change_location(narration['location']))
			if self.change_location(narration['location']):
				if narration['speaker'] == self.narrator:
					self.gui_obj.add_txt('narration', narration['dialog'] + '\n\n', narration['speaker'].tag)
				else:
					self.gui_obj.add_txt('narration', narration['speaker'].name + ': ' + narration['dialog'] + '\n\n', narration['speaker'].tag)
					#self.gui_obj.add_txt('narration', '_____________________________________________________________________\n\n', 'center_tag', '#FFFACD')
		self.update_choices()

	#Output choices for stage
	def update_choices(self):
		for choice in self.current_stage.choices:
			print('c = ' + choice)
			self.gui_obj.add_txt('choice', '[' + choice.upper() + ']    \n\n', 'center_tag')


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
			img_loc = './assets/' + new_location.image
			print('img location: ' + img_loc)
			self.gui_obj.change_image('loc_img', img_loc)
			self.gui_obj.update_label('loc_desc', new_location.name)
			if new_location.id != 'menu':
				self.gui_obj.add_txt('narration', self.linebar + new_location.desc['long1'] + '\n' + self.linebar, self.narrator.tag)
			#self.gui_obj.cur_loc = new_location.name
			self.current_location = new_location
			return False
		else:
			return True

	#def load_loc_description(self):
	#	location_description = self.current_stage.location.description
	#	if not (location_description == ''):
	#		self.current_stage.narration.insert(0, {'speaker':self.narrator, 'dialog':location_description})