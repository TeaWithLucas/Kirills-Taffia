import time
from functions import *
from tkinter import *
import PIL.ImageTk
import PIL.Image

""" These are the classes which are the structures for different objects in the game """


class Actor():
	def __init__(self, name='Blank_name', inv=[]):
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
		new_maxh = self.stats['special']['str'] * 8
		new_curh = cur_curh + (new_maxh - cur_maxh)
		self.stats['health'] = {'maxh': new_maxh, 'curh': new_curh}

"""The room class. Rooms will for maps which will be assigned to levels. The rooms will determine the story. """

class Room():
	def __init__(self, name, des, exits, items):
		self.name = name
		self.description = des
		self.exits = exits
		self.items = items

class Stage():
	def __init__(self, stage_id, name, narration, choices):
		self.stage_id = stage_id
		self.name = name
		self.narration = narration
		self.choices = choices
		self.choicesinput = []
		for choice in choices:
			self.choicesinput.append(choice.lower())

""" The level class that is responsible for navigation on the map for that level """

class Level():
	def __init__(self, id, title, intro_text, current_room):
		self.id = id
		self.title = title
		self.intro_text = intro_text
		self.current_room = current_room

	def start(self):

		#print(self.intro_text)
		#print_level()
		draw_ascii('map.txt')
		#print('\n\n\n\n Press ENTER to continue...')
		#a = input()
		self.level_main()

	def show_room(self, room):

		print('\n' + room.name.upper() + '\n')
		print(room.description + '\n')


	def exit_leads_to(self, exits, direction):

		return rooms[exits[direction]].name

	def print_line(self, direction, leads_to):

		print('Go ' + direction.upper() + ' to ' + leads_to + '.')

	def display_exits(self, exits):
		print('Select action:')
		for exit in exits:
			self.print_line(exit, self.exit_leads_to(exits, exit))

	def exit_selection(self,exits):
		while True:

			#display the options
			self.display_exits(exits)
			#get input
			#ans = input()
			#normalise input

			#validate input

			return ans

	def move_player(self, exits, direction):

		return rooms[exits[direction]]

	#the level loop
	def level_main(self):
		while True:

			#Display current situation
			self.show_room(self.current_room)
			#Get exits
			exits = self.current_room.exits
			#Let player select exit
			direction = self.exit_selection(exits)
			#move the player
			self.current_room = self.move_player(exits, direction)		



class GradientFrame(Canvas):
	'''A gradient frame which uses a canvas to draw the background'''
	def __init__(self, parent, borderwidth=1, relief="sunken"):
		Canvas.__init__(self, parent, borderwidth=borderwidth, relief=relief)
		self._color1 = '#152018'
		self._color2 = '#344e3a'
		self.bind("<Configure>", self._draw_gradient)

	def _draw_gradient(self, event=None):
		'''Draw the gradient'''
		self.delete("gradient")
		width = self.winfo_width()
		height = self.winfo_height()
		limit = width
		(r1,g1,b1) = self.winfo_rgb(self._color1)
		(r2,g2,b2) = self.winfo_rgb(self._color2)
		r_ratio = float(r2-r1) / limit
		g_ratio = float(g2-g1) / limit
		b_ratio = float(b2-b1) / limit

		for i in range(limit):
			nr = int(r1 + (r_ratio * i))
			ng = int(g1 + (g_ratio * i))
			nb = int(b1 + (b_ratio * i))
			color = "#%4.4x%4.4x%4.4x" % (nr,ng,nb)
			self.create_line(i,0,i,height, tags=("gradient",), fill=color)
		self.lower("gradient")

class Item():
	def __init__(self, itemid, name, description):
		self.itemid = itemid
		self.name = name
		self.description = description

	def inspect():
		#Print out name, description and hints in narration section
		pass
