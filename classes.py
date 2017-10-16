from functions import *

""" These are the classes which are the structures for different objects in the game """

class Actor():
	def __init__(self):
		self.name = 'Blank_name'
		self.inv = []
		self.stats = {
			'special': {'s':0, 'p':0, 'e':0, 'c':0, 'i':0, 'a':0, 'l':0},
			'health': {'curh':0, 'maxh':0},
			'level': {'exp':0,'lvl':0,'nxt_lvl':0, 'nxt_exp':0}
		}

		self.stats['special'] = {'s':1, 'p':1, 'e':1, 'c':1, 'i':1, 'a':1, 'l':1}
		self.calc_stats()

	def calc_stats(self):
		cur_maxh = self.stats['health']['maxh']
		cur_curh = self.stats['health']['curh']
		new_maxh = self.stats['special']['p'] * 8
		new_curh = cur_curh + (new_maxh - cur_maxh)
		self.stats['health'] = {'maxh': new_maxh, 'curh': new_curh }

		print(self.stats)

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
		clear()
		#print(self.intro_text)
		#print_level()
		draw_ascii('map.txt')
		#print('\n\n\n\n Press ENTER to continue...')
		a = input()
		self.level_main()

	def show_room(self, room):
		clear()
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
	def __init__(self, player, level):
		self.running = True
		self.title = 'The Game'
		self.game_levels = level
		self.player = player

	#run main loop
	def run_game(self):
		while self.running:
			self.main_menu()

	#displays the main menu of the game
	def main_menu(self):
		#Display
		clear()
		draw_anim_ascii('welcome.txt')
		print('\n \n \n \n')
		#print(self.title.upper() + '\n')
		print('Welcome ' + self.player.name)
		print('Health: ' + str(self.player.stats['health']['curh']) + "/" + str(self.player.stats['health']['maxh']) )
		print('					 Select:\n\n					  a.New Game\n					  b.Load Game\n					  c.Exit\n\n')

		#Take input
		inp = input('->')
		if inp == 'a':
			self.new_game_menu()

		elif inp == 'b':
			pass
		elif inp == 'c':
			quit()
		else:
			clear()
			print('Enter a valid option')
			time.sleep(1)

	#Start a new game at the level of the new player
	def new_game_menu(self):
		global player

		clear()
		print('Enter new character name:\n ')
		new_name = input('->')

		self.player.name = new_name
		self.start_level(self.player)

	#init the level
	def start_level(self, player):
		pass

class Item():
	def __init__(self, id, name, description):
		self.id = id
		self.name = name
		self.description = description

	def inspect():
		#Print out name, description and hints in narration section
		pass
