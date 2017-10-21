
""" THIS IS THE MAIN GAME CLASS IT CONTAINS THE MAIN GAME LOOP AND LOGIC ASWELL AS MENU FUNCTIONS"""
from classes import *
from functions import *
from data import *
import PIL.Image
import PIL.ImageTk

class gui():
	#constructor called on creation
	def __init__(self, title = 'the game'):
		print('initialisng gui')
		self.running = True
		self.title = title
		self.player = Actor('Kirill',[book_item, gun_item])
		self.user_input = ""
		self.current_stage = stg_start

		#TK gui window
		self.main = Tk ()
		main = self.main
		main.resizable(width = False, height = False)
		main.title(self.title)

		bg_image = PIL.ImageTk.PhotoImage(PIL.Image.open("./assets/back.jpg"))
		map_sprite = PhotoImage(file = "map.png")

		#window background
		frame = Label(main, image = bg_image)
		frame.place(x=0, y=0, relwidth=1, relheight=1)

		#creating each widget
		frame_left = Frame(main)
		frame_left.grid(column = 1, row = 1)

		stat_widget = Text(frame_left, bg = '#262820', fg = 'green', width = 25, height = 15)
		hp_widget = Text(stat_widget, bg = 'black', fg = 'red', font = (20))
		inv_widget = Text(frame_left, bg = '#262820',fg = 'white', width = 25, height = 15)

		stat_widget.grid(row = 1, column = 1)
		hp_widget.place(x=0, y=0, relwidth =1, relheight = 0.1)
		inv_widget.grid(row = 2, column = 1)

		frame_middle = Frame(main)
		frame_middle.grid(column = 2, row = 1)

		narration_widget = Text(frame_middle, bg = 'black', fg = 'yellow', width = 100)
		choice_widget = Text(frame_middle, bg = 'black', fg = 'yellow', width = 100, height = 10)
		console_widget = Entry(frame_middle, bg = '#6a8c87', fg = 'white', width = 100)
		narration_widget.grid(row = 1, column = 1)
		choice_widget.grid(row = 2, column = 1)
		console_widget.grid(row = 3, column = 1)

		frame_right = Frame(main)
		frame_right.grid(column = 3, row = 1)

		map_widget = Label(frame_right,  image = map_sprite)
		map_widget.grid(row = 1, column = 1)
		

		frame.image = bg_image
		map_widget.image = map_sprite
		

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

	def navigate(self):
		self.refresh()
		print('navigating')
		stage = self.current_stage
		user_input = self.user_input
		if user_input == "":
			self.set_title(stage.name)
			self.clear_middle()
			self.remaining_narration = stage.narration
			self.narrate()
		else:
			print('user_input - ' + user_input[0])
			self.user_input = ""
			if user_input == 'start':
				self.current_stage = stg_act1
			elif user_input== 'load game':
				self.current_stage = stg_load_game
			elif user_input == 'exit':
				self.current_stage = stg_exit
			elif user_input == '':
				pass
			else:
				self.update_txt('choice', "Invalid, You said: " + user_input[0] + "\n")
				if not(stage):
					print("Error - Stage not set")
					#self.main_menu()
				elif stage == stg_start:
					#self.main_menu()
					pass
				elif stage == stg_main_menu:
					#self.main_menu()
					pass
				elif stage == stg_other_menu:
					pass
				elif stage == stg_new_game:
					#self.new_game()
					pass
				elif stage == stg_load_game:
					pass
					#self.load_game()
				elif stage == stg_exit:
					pass
					#self.exit()
				else:
					print("Error - Stage not defined: " + str(stage))
					#self.main_menu()
			self.navigate()


	#Event driven fuctions
	def rtn_pressed(self, event):
		print("Input - Enter Key")
		self.user_input =self.get_input()
		user_input = self.user_input
		if user_input[0] == 'back':
			#return to main menu
			print('going back')
			self.current_stage = stg_main_menu
		elif user_input[0] == 'attack':
			#TESTING HP BAR
			amount = 1
			if len(user_input) > 1:
				amount = int(user_input[1])
			print('testing taking ' + str(amount) + ' hp')
			self.player.stats['health']['curh'] -= amount
			self.update_hp_bar()

		self.navigate()

	def narrate(self):
		narration = self.remaining_narration
		print(narration[0]['speaker'].name + ':\t\t\"' + narration[0]['dialog'] + '\"')
		output = "\n\n"
		output2 = narration[0]['dialog'] + ''
		if narration[0]['speaker'] == char_narrator:
			output += '\t' + output2
		else:
			output += narration[0]['speaker'].name + ':\t\t\"' + output2 + '\"'
		
		self.add_txt('narration', output)
		if len(narration) > 1:
			self.remaining_narration = narration[1:]
			self.main.after(1000, self.narrate)
		else:
			self.update_choices()


	def update_clock(self):
		now = time.strftime("%H:%M:%S")
		self.label.configure(text=now)
		self.main.after(1000, self.update_clock)

	#Update GUI widgets

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
		norm_input = normalise(con_input, self.current_stage.choicesinput)
		self.locations['console'].delete(0, END)
		return norm_input
		

	def set_title(self, subtitle = ""):
		if subtitle != "":
			self.main.title(self.title + " - " + subtitle)
		else:
			self.main.title(self.title)

	def update_stat_display(self):

		update_txt = ""
		update_txt += '\t[STATISTICS]\n\n'
		for desc, amount in self.player.stats['special'].items():
			num_spaces = 13 - (len(desc) + 2)
			spaces = ''
			for a in range(0,num_spaces):
				spaces += ' '

			update_txt += ' ' + desc.upper() + ': '+ spaces + str(amount) + '\n'
		print ('updating stats:' + str(self.player.stats['special']))
		self.update_txt('stats', update_txt)

		#self.update_txt(player.name + "\n" + str(player.stats['special']))

	def update_hp_bar(self):
		update_txt = ""
		player_vitals = self.player.stats['health']

		if player_vitals['curh'] <= 0:
			print("Player Dead")
			self.user_input = ""
			self.current_stage = stg_lost
			player_vitals['curh'] = 0

		full_sym = '\u2665'
		half_sym = '\u2661'
		none_sym = 'x'

		full_sym_num=int(player_vitals['curh']/2)
		half_sym_num=int(player_vitals['curh']%2)
		none_sym_num=int(player_vitals['maxh']/2-half_sym_num-full_sym_num)
		print ('updating health, full_sym_num: ' + str(full_sym_num) + ',half_sym_num: ' + str(half_sym_num) + ', none_sym_num: '+ str(none_sym_num))
		symbols = full_sym_num * full_sym + half_sym_num * half_sym + none_sym_num * none_sym
		print ('updating health, cur hp: ' + str(player_vitals['curh']) + ', max hp: ' + str(player_vitals['curh']) + ', symbols: '+ symbols)
		self.update_txt('hp', symbols)

	def update_inv_display(self):
		update_txt = ""
		update_txt += '\t[INVENTORY]\n\n'
		for item in self.player.inv:
			update_txt += '  ---  ' + item.itemid + '\n'
		self.update_txt('inv', update_txt)

	def update_choices(self):
		for choice in self.current_stage.choices:
			self.add_txt('choice', "\t\t\t\t" + choice + "\n")

	def refresh(self):
		print('refreshing windows')
		self.update_stat_display()
		self.update_inv_display()
		self.update_hp_bar()

	def clear_middle(self):
		print('clearing narration and choice widgets')
		self.update_txt('narration', "")
		self.update_txt('choice', "")

def init():
	window = gui('Taffi Warz')
	window.main.mainloop()


init()
