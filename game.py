
""" THIS IS THE MAIN GAME CLASS IT CONTAINS THE MAIN GAME LOOP AND LOGIC ASWELL AS MENU FUNCTIONS"""
from classes import *
from functions import *
from data import *
from tkinter import *

class gui():
	#constructor called on creation
	def __init__(self, player, title = 'the game'):
		self.running = True
		self.title = 'The Game'
		self.player = player
		self.user_input = ""
		self.current_stage = stg_start

		#TK gui window
		self.main = Tk ()
		main = self.main
		main.resizable(width = False, height = False)
		main.title('Taffi Warz')

		bg_image = PhotoImage(file = "bg3.png")
		map_sprite = PhotoImage(file = "map.png")

		#window background
		frame = Label(main, image = bg_image)
		frame.place(x=0, y=0, relwidth=1, relheight=1)

		#creating each widget
		console_widget = Entry(main, bg = '#6a8c87', fg = 'white', width = 100)
		map_widget = Label(main,  image = map_sprite)
		inv_widget = Text(main, bg = '#262820',fg = 'white', width = 25, height = 15)
		stat_widget = Text(main, bg = '#262820', fg = 'green', width = 25, height = 15)
		hp_widget = Text(stat_widget, bg = 'black', fg = 'red')
		narration_widget = Text(main, bg = 'black', fg = 'yellow', width = 100)
		choice_widget = Text(main, bg = 'black', fg = 'yellow', width = 100, height = 10)

		frame.image = bg_image
		map_widget.image = map_sprite

		#Display and layout of all widgets
		console_widget.grid(row = 4, column = 1, columnspan = 3)
		map_widget.grid(row = 1, column = 1)
		inv_widget.grid(row = 1, column = 3, rowspan = 2)
		stat_widget.grid(row = 2, column = 1)
		hp_widget.place(x=0, y=0, relwidth =1, relheight = 0.1)
		narration_widget.grid(row = 1, column = 2, rowspan = 2)
		choice_widget.grid(row = 3, column = 1, columnspan = 3)

		inv_widget.config(state = DISABLED)
		choice_widget.config(state = DISABLED)
		narration_widget.config(state = DISABLED)
		stat_widget.config(state = DISABLED)
		hp_widget.config(state = DISABLED)

		self.locations = {
			'frame' : frame,
			'console' : console_widget,
			'map' : map_widget,
			'inv' : inv_widget,
			'stats' : stat_widget,
			'hp' : hp_widget,
			'narration' : narration_widget,
			'choice' : choice_widget
		}

		console_widget.bind('<Return>', self.rtn_pressed)

		#Set focus on the console
		console_widget.focus_set()

		#Start
		self.navigate()

	def rtn_pressed(self, event):
		print("Input - Enter Key")
		self.user_input = self.get_input()
		user_input = self.user_input
		if user_input == 'back':
			#return to main menu
			self.current_stage = main_menu
		elif user_input == 'attack':
			#TESTING HP BAR
			self.player.stats['health']['curh'] -= 1
			self.update_hp_bar()

		self.navigate()

	def navigate(self):
		self.refresh()
		stage = self.current_stage
		if not(stage):
			print("Error - Stage not set")
			self.main_menu()
		elif stage == stg_start:
			self.main_menu()
		elif stage == stg_main_menu:
			self.main_menu()
		elif stage == stg_other_menu:
			pass
		elif stage == stg_new_game:
			self.main_menu()
		elif stage == stg_load_game:
			self.main_menu()
		elif stage == stg_exit:
			self.main_menu()
		else:
			print("Error - Stage not defined: " + stage)
			self.main_menu()

	def update_txt(self, location, input):
		self.locations[location].config(state = NORMAL)
		self.locations[location].delete(1.0, END)
		self.locations[location].insert(END, input)
		self.locations[location].config(state = DISABLED)

	def add_txt(self, location, input):
		self.locations[location].config(state = NORMAL)
		self.locations[location].insert(END, input)
		self.locations[location].config(state = DISABLED)

	def get_txt(self, location):
		return self.locations[location].get(1.0, END)

	def get_input(self):
		con_input = self.locations['console'].get()
		#!!!!!! Normalise input neded
		normized_input = con_input
		self.locations['console'].delete(0, END)
		return normized_input

	def update_stat_display(self):

		update_txt = ""
		update_txt += '\t[STATISTICS]\n\n'
		for desc, amount in self.player.stats['special'].items():
			num_spaces = 13 - (len(desc) + 2)
			spaces = ''
			for a in range(0,num_spaces):
				spaces += ' '

			update_txt += ' ' + desc.upper() + ': '+ spaces + str(amount) + '\n'

		self.update_txt('stats', update_txt)

		#self.update_txt(player.name + "\n" + str(player.stats['special']))

	def update_hp_bar(self):
		update_txt = ""
		player_vitals = self.player.stats['health']

		full_sym = '♥'
		half_sym = '💛'
		none_sym = 'x'

		full_sym_num=int(player_vitals['curh']/2)
		half_sym_num=int((full_sym_num*2 - player_vitals['curh']))
		none_sym_num=int(player_vitals['maxh']-player_vitals['curh'])

		symbols = full_sym_num * full_sym + half_sym_num * half_sym + none_sym_num * none_sym
		print (symbols)
		self.update_txt('hp', symbols)

	def update_inv_display(self):
		update_txt = ""
		update_txt += '\t[INVENTORY]\n\n'
		for item in self.player.inv:
			update_txt += '  ---  ' + item.id + '\n'
		self.update_txt('inv', update_txt)

	def refresh(self):
		self.update_stat_display()
		self.update_inv_display()
		self.update_hp_bar()
		self.update_txt('narration', "")
		self.update_txt('choice', "")

	#displays the main menu of the game
	def main_menu(self):
		#Display
		self.current_stage = stg_main_menu

		user_input = self.user_input

		if user_input == "":
			narration_out = ""
			choice_out = ""
			narration_out += draw_ascii('welcome.txt') + '\n'
			narration_out += '\n\n\n\n'
			#narration_out += self.title.upper() + '\n'
			narration_out += 'Welcome ' + self.player.name + '\t\t\t\t\t\t\t'
			choice_out += 'Select:\n\n\t\t\ta.New Game\n\t\t\tb.Load Game\n\t\t\tc.Exit'

			self.add_txt('narration', narration_out)
			self.add_txt('choice', choice_out)
			time.sleep(1)
		else:

			self.user_input = ""
			if user_input == 'a':
				self.current_stage = stg_new_game
			elif user_input== 'b':
				self.current_stage = stg_load_game
			elif user_input == 'c':
				self.current_stage = stg_exit
			elif user_input == '':
				pass
			else:
				self.update_txt('choice', "Invalid, You said: " + user_input + "\n")
			self.navigate()

	def load_game(self):
		update_text(out_console, 'Load game menu')
		update_text(choice_console, 'Updated')


	def new_game(self):
		update_text(out_console, 'New game')
		update_text(choice_console, 'Updated')

	def exit(self):
		print("exiting")
		quit()

def init():

	window = gui(player, 'Taffi Warz')

	window.main.mainloop()



init()
