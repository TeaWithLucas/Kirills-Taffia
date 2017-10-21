
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
		self.player = Actor('kirril_tag', 'yellow','Kirill',[])
		self.user_input = ""
		#self.current_stage = stg_start
		self.stage_man = Stage_Manager(stages,self,char_narrator)

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


		frame_middle = Frame(main, width = 200)
		frame_middle.grid(column = 2, row = 1)

		narration_widget = Text(frame_middle, bg = 'black', fg = 'yellow')
		choice_widget = Text(frame_middle, bg = 'black', fg = 'yellow', height = 10)
		console_widget = Entry(frame_middle, bg = 'black', fg = 'white')
		narration_widget.grid(row = 1, column = 1)
		choice_widget.grid(row = 2, column = 1)
		console_widget.grid(row = 3, column = 1)

		frame_right = Frame(main)
		frame_right.grid(column = 3, row = 1)

		map_widget = Label(frame_right,  image = map_sprite)
		map_widget.grid(row = 1, column = 1)
		room_items_widget = Text(frame_right, bg = '#262820',fg = 'white', width = 25, height = 15)
		room_items_widget.grid(row = 2, column = 1)

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
			'room_items':room_items_widget,
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
		self.clear_middle()
		self.refresh()
		self.set_title(self.stage_man.current_stage.name)
		self.stage_man.narrate_current_stage()



	#Event driven fuctions
	def rtn_pressed(self, event):
		print("Input - Enter Key")
		self.stage_man.take_input(self.get_input())
		self.navigate()



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

	def add_txt(self, location, input, tag, color):
		self.locations[location].config(state = NORMAL)
		self.locations[location].insert(END, input, tag)
		self.locations[location].tag_config(tag, foreground = color)
		self.locations[location].see(END)
		self.locations[location].config(state = DISABLED)

	def get_txt(self, location):
		return self.locations[location].get(1.0, END)

	def get_input(self):
		con_input = self.locations['console'].get()
		norm_input = normalise(con_input, self.stage_man.current_stage.choicesinput)
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

		update_txt_room = ''
		update_txt_room += '     [YOU CAN PICK]\n\n'
		for item in self.stage_man.current_stage.location.items:
			update_txt_room += ' --- ' + item.itemid + '\n'
		self.update_txt('room_items', update_txt_room)

	def update_choices(self):
		for choice in self.current_stage.choices:
			self.add_txt('choice', "\t\t\t\t" + choice + "\n", self.player.tag, self.player.speech_color)

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
