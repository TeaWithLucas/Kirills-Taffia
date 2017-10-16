from functions import *
from tkinter import *

""" These are the classes which are the structures for different objects in the game """

class Actor():
	def __init__(self):
		self.name = 'Blank_name'
		self.inv = []
		self.stats = {
			#'special': {'s':0, 'p':0, 'e':0, 'c':0, 'i':0, 'a':0, 'l':0},
			'health': {'curh':0, 'maxh':0},
			'level': {'exp':0,'lvl':0,'nxt_lvl':0, 'nxt_exp':0}
		}

		self.stats['special'] = {'strenght':1, 'preception':1, 'endurance':1, 'charisma':1, 'inteligence':1, 'agility':1, 'luck':1}
		self.calc_stats()

	def calc_stats(self):
		cur_maxh = self.stats['health']['maxh']
		cur_curh = self.stats['health']['curh']
		new_maxh = self.stats['special']['preception'] * 8
		new_curh = cur_curh + (new_maxh - cur_maxh)
		self.stats['health'] = {'maxh': new_maxh, 'curh': new_curh }

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
		a = input()
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
			ans = input()
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



class Game():
	#constructor called on creation
	def __init__(self, gui, player, level):
		self.running = True
		self.title = 'The Game'
		self.game_levels = level
		self.player = player
		self.gui = gui
		self.display_stats()

	#Displays stats in the stat console
	def display_stats(self):
		self.gui.add('stats_txt', '      [STATISTICS]\n\n')
		for item in self.player.stats['special']:
			num_spaces = 13 - (len(item) + 2)
			spaces = ''
			for a in range(0,num_spaces):
				spaces += ' '

			self.gui.add('stats_txt',' ' + item.upper() + ': '+ spaces + str(self.player.stats['special'][item]) + '\n')


		#self.gui.update('stats_txt', player.name + "\n" + str(player.stats['special']))

	#run main loop
	def run_game(self):
		while self.running:
			self.main_menu()

	#displays the main menu of the game
	def main_menu(self):
		#Display

		self.gui.add('out_console', draw_ascii('welcome.txt'))
		self.gui.add('out_console', '\n\n\n\n')
		#self.gui.add('out_console', self.title.upper() + '\n')
		self.gui.add('out_console', 'Welcome ' + self.player.name)
		self.gui.add('out_console', 'Health: ' + str(self.player.stats['health']['curh']) + "/" + str(self.player.stats['health']['maxh']) )
		self.gui.add('out_console', '\t\t\tSelect:\n\n\t\t\ta.New Game\n\t\t\tb.Load Game\n\t\t\tc.Exit\n\n')

		#Take input
		inp = input('->')
		if inp == 'a':
			self.new_game_menu()

		elif inp == 'b':
			pass
		elif inp == 'c':
			quit()
		else:

			self.gui.add('out_console', 'Enter a valid option')
			time.sleep(1)

	#Start a new game at the level of the new player
	def new_game_menu(self):
		global player


		self.gui.add('out_console', 'Enter new character name:\n ')
		new_name = input('->')

		self.player.name = new_name
		self.start_level(self.player)

	#init the level
	def start_level(self, player):
		pass


class gui():
	#constructor called on creation
	def __init__(self):
		#TK gui window
		self.main = Tk ()

		#window background
		#background_label = Label(self.main, bg = '#445b19')
		f = GradientFrame(self.main)

		#Input console
		console = Text(self.main, bg = 'black', fg = 'white', height = 1, insertbackground = 'white')
		console.insert(END, '->')

		#The map
		map_label = Label(self.main,text = 'MAP',  bg = '#3a3f2d', fg = 'white', width = 20 )

		#Inventory display console
		inv_txt = Text(self.main, bg = '#262820',fg = 'white', width = 25, height = 15)

		#Stats display console
		stats_txt = Text(self.main, bg = '#3a3f2d', fg = 'white', width = 25, height = 10)

		#Output console
		out_console = Text(self.main, bg = 'black', fg = 'white')

		#Choice console
		choice_console = Text(self.main, bg = 'black', fg = 'white', height = 10)

		#Display and layout of all components
		f.place(x=0, y=0, relwidth=1, relheight=1)
		console.grid(row = 4, column = 1, columnspan = 3)
		map_label.grid(row = 1, column = 1)
		inv_txt.grid(row = 1, column = 3, rowspan = 2)
		stats_txt.grid(row = 2, column = 1)
		out_console.grid(row = 1, column = 2, rowspan = 2)
		choice_console.grid(row = 3, column = 1, columnspan = 3)

		self.locations = {
			'background_label' : f,
			'console' : console,
			'map_label' : map_label,
			'inv_txt' : inv_txt,
			'stats_txt' : stats_txt,
			'out_console' : out_console,
			'choice_console' : choice_console
		}

		#The main loop
		#self.main.mainloop()

	def update(self, location, input):
		self.locations[location].delete(1.0, END)
		self.locations[location].insert(END, input)

	def add(self, location, input):
		self.locations[location].insert(END, input)

	def get(self, location):
		self.locations[location].get(1.0, END)


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
