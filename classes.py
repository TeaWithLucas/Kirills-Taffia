import time
from functions import *
from tkinter import *

""" These are the classes which are the structures for different objects in the game """

class Actor():
	def __init__(self):
		self.name = 'Blank_name'
		self.inv = []
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

class gui():
	#constructor called on creation
	def __init__(self, player):
		#TK gui window
		self.main = Tk ()

		#window background
		frame = GradientFrame(self.main)
		frame.place(x=0, y=0, relwidth=1, relheight=1)

		#creating each widget
		console = Entry(self.main, bg = 'white', fg = 'black', width = 100)
		map_label = Label(self.main,text = 'MAP',  bg = '#3a3f2d', fg = 'white', width = 20 )
		inv_txt = Text(self.main, bg = '#262820',fg = 'white', width = 25, height = 15)
		stats_txt = Text(self.main, bg = '#3a3f2d', fg = 'white', width = 25, height = 15)
		out_console = Text(self.main, bg = 'black', fg = 'white', width = 100)
		choice_console = Text(self.main, bg = 'black', fg = 'white', width = 100, height = 10)

		#Display and layout of all widgets
		console.grid(row = 4, column = 1, columnspan = 3)
		map_label.grid(row = 1, column = 1)
		inv_txt.grid(row = 1, column = 3, rowspan = 2)
		stats_txt.grid(row = 2, column = 1)
		out_console.grid(row = 1, column = 2, rowspan = 2)
		choice_console.grid(row = 3, column = 1, columnspan = 3)

		self.locations = {
			'frame' : frame,
			'console' : console,
			'map_label' : map_label,
			'inv_txt' : inv_txt,
			'stats_txt' : stats_txt,
			'out_console' : out_console,
			'choice_console' : choice_console
		}

		self.running = True
		self.title = 'The Game'
		self.player = player
		self.user_input = ""
		self.curent_stage = "main_menu"

		#Start
		self.navigate()

	def update_stat_display(self):

		update_txt = ""
		player_vitals = self.player.stats['health']
		player_health_perc = player_vitals['curh']/player_vitals['maxh']
		update_txt += '\t[STATISTICS]\n\n'
		for desc, amount in self.player.stats['special'].items():
			num_spaces = 13 - (len(desc) + 2)
			spaces = ''
			for a in range(0,num_spaces):
				spaces += ' '

			update_txt += ' ' + desc.upper() + ': '+ spaces + str(amount) + '\n'

		count_hash = player_health_perc * 10
		count_dash = 10 - count_hash

		hashes = ''
		for i in range(0,int(count_hash)):
			hashes += '#'

		dashes = ''
		for i in range(0,int(count_dash)):
			dashes += '-'

		update_txt += '\n\n\n Health:\n'
		update_txt += ' [' + hashes + dashes +']'

		self.update_txt('stats_txt', update_txt)

		#self.update_txt(player.name + "\n" + str(player.stats['special']))

	def update_inv_display(self):
		update_txt = ""
		update_txt += '      [INVENTORY]\n\n'
		for item in self.player.inv:
			update_txt += '  ---  ' + item.id + '\n'
		self.update_txt('inv_txt', update_txt)

	def refresh(self):
		self.update_stat_display()
		self.update_inv_display()
		self.update_txt('out_console', "")
		self.update_txt('choice_console', "")

	#displays the main menu of the game
	def main_menu(self):
		#Display
		self.curent_stage = "main_menu"

		normalised_input = self.user_input
		self.user_input = ""

		if normalised_input == 'a':
			self.add_txt('choice_console', "Correct, You said: " + normalised_input + "\n")
		elif normalised_input== 'b':
			self.add_txt('choice_console', "Correct, You said: " + normalised_input + "\n")
		elif normalised_input == 'c':
			self.add_txt('choice_console', "Correct, You said: " + normalised_input + "\n")
		elif normalised_input == '':
			pass
		else:
			self.update_txt('choice_console', "Invalid, You said: " + normalised_input + "\n")

		
		out_console = ""
		choice_console = ""
		out_console += draw_ascii('welcome.txt') + '\n'
		out_console += '\n\n\n\n'
		#out_console += self.title.upper() + '\n'
		out_console += 'Welcome ' + self.player.name + '\t\t\t\t\t\t\t'
		choice_console += 'Select:\n\n\t\t\ta.New Game\n\t\t\tb.Load Game\n\t\t\tc.Exit'

		self.add_txt('out_console', out_console)
		self.add_txt('choice_console', choice_console)
		

		time.sleep(1)
		self.locations['console'].bind('<Return>', self.callback)

	def callback(self, event):
		print("Enter Key")
		self.user_input = self.get_input()
		self.navigate()

	def navigate(self):
		self.refresh()
		if self.curent_stage == "main_menu":
			self.main_menu()
		elif self.curent_stage == "other":
			pass
		else:
			self.main_menu()

	def update_txt(self, location, input):
		self.locations[location].delete(1.0, END)
		self.locations[location].insert(END, input)

	def add_txt(self, location, input):
		self.locations[location].insert(END, input)

	def get_txt(self, location):
		return self.locations[location].get(1.0, END)

	def get_input(self):
		return self.locations['console'].get()
			



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
	def __init__(self, id, name, description):
		self.id = id
		self.name = name
		self.description = description

	def inspect():
		#Print out name, description and hints in narration section
		pass
