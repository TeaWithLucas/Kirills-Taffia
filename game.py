
""" THIS IS THE MAIN GAME CLASS IT CONTAINS THE MAIN GAME LOOP AND LOGIC ASWELL AS MENU FUNCTIONS"""
from stages import *
from data import *
import PIL.Image
import PIL.ImageTk
import secrets
from tkinter import font

class gui():
	#constructor called on creation
	def __init__(self, title = 'the game'):
		print('initialisng gui')
		self.running = True
		self.title = title
		self.player = actors['Kirill_Sidorov'] #The protagonist actor object
		self.narrator = actors['Nikeen_Patel'] #The narrato actor
		self.system_text = actors['Dmytro_Kaduba'] #System text display actor

		#User input (global)
		self.user_input = ""

		#Stage manager to navigate through the game
		start_stage = stg_main_menu
		self.stage_man = Stage_Manager(self,stages,start_stage,self.narrator,self.system_text)

		#health and location initialisation
		self.cur_health_symbols = "<health>"
		self.cur_loc = "<location>"

		#Text display speeds
		self.narration_speed = 0.01
		self.waittime = 0.5

		#TK gui window
		self.main = Tk ()
		main = self.main
		main.resizable(width = False, height = False)
		main.title(self.title)

		font.Font(root=self.main, font="./fonts/AbydosR.ttf", name="Abydos")

		#Loading images from files
		bg_image = PIL.ImageTk.PhotoImage(PIL.Image.open("./assets/back.jpg"))
		map_sprite = PIL.ImageTk.PhotoImage(PIL.Image.open("./assets/map.bmp"))
		loc_sprite = PIL.ImageTk.PhotoImage(PIL.Image.open("./assets/queens.bmp"))

		#main frame
		frame = Frame(main, width = 250)
		frame.pack()

		#window background
		background = Label(frame, image = bg_image, bg = 'black')
		background.place(x=0, y=0, relwidth=1, relheight=1)

		#creating each widget
		frame_left = Frame(frame, background = 'black')
		frame_left.pack( side = LEFT, fill=X)

		stat_desc_widget = Label(frame_left, text="Stats", bg = 'black', fg = 'White', font = (16), width = 25)
		stat_widget = Text(frame_left, bg = '#262820', fg = 'lightgreen', height = 10, width = 25)
		hp_desc_widget = Label(frame_left, text="HP:", bg = 'black', fg = 'White', font = (16), width = 5)
		hp_widget = Label(frame_left, text='<health>', bg = 'black', fg = 'red', font = (20), width = 15)
		wallet_desc_widget = Label(frame_left, text="Wallet:", bg = 'black', fg = 'White', font = (16), width = 5)
		wallet_widget = Label(frame_left, text='<wallet>', bg = 'black', fg = 'red', font = ("Abydos", 12), width = 15)
		inv_desc_widget = Label(frame_left, text="Inventory", bg = 'black', fg = 'White', font = (16), width = 25)
		inv_widget = Text(frame_left, bg = '#262820',fg = 'white', height = 15, width = 25)

		stat_desc_widget.grid(row = 1, column = 1, columnspan=2)
		stat_widget.grid(row = 2, column = 1, columnspan=2)
		hp_desc_widget.grid(row = 3, column = 1)
		hp_widget.grid(row = 3, column = 2)
		wallet_desc_widget.grid(row = 4, column = 1)
		wallet_widget.grid(row = 4, column = 2)
		inv_desc_widget.grid(row = 5, column = 1, columnspan=2)
		inv_widget.grid(row = 6, column = 1, columnspan=2)

		frame_middle = Frame(frame, background = 'black')
		frame_middle.pack( side = LEFT, fill=X)

		narration_widget = Text(frame_middle, bg = 'black', fg = '#D3D3D3', padx = 20, pady = 20, wrap = WORD)
		choice_widget = Text(frame_middle, bg = 'black', fg = '#D3D3D3', height = 10, width = 85)
		console_widget = Entry(frame_middle, bg = 'black', fg = 'white', width = 75, insertwidth = 10 , insertbackground ='white')
		narration_widget.grid(row = 1, column = 1)
		choice_widget.grid(row = 2, column = 1)
		console_widget.grid(row = 3, column = 1)

		frame_right = Frame(frame, background = 'black')
		frame_right.pack( side = LEFT, fill=X)

		map_desc_widget = Label(frame_right, text="Map", bg = 'black', fg = 'White', font = (16))
		map_desc_widget.grid(row = 1, column = 1)
		map_widget = Label(frame_right,  image = map_sprite)
		map_widget.grid(row = 2, column = 1)
		loc_desc_widget = Label(frame_right, text='<curloc>', bg = 'black', fg = 'White', font = (16))
		loc_desc_widget.grid(row = 3, column = 1)
		loc_widget = Label(frame_right,  image = loc_sprite)
		loc_widget.grid(row = 4, column = 1)

		#items_widget = Text(frame_right, bg = '#262820', fg = 'white', height = 15, width = 25)
		#items_widget.grid(row = 3, column = 1)

		#Reseting images to avoid them disapearing
		background.image = bg_image
		map_widget.image = map_sprite
		loc_widget.image = loc_sprite

		#Disable all widgets so they become read only
		inv_widget.config(state = DISABLED)
		choice_widget.config(state = DISABLED)
		narration_widget.config(state = DISABLED)
		stat_widget.config(state = DISABLED)

		#Widget dictionary for access
		self.widgets = {
			'background' : background,
			'console' : console_widget,
			'map_desc' : map_desc_widget,
			'map' : map_widget,
			'loc_desc': loc_desc_widget,
			'loc_img': loc_widget,
			'inv' : inv_widget,
			#'items' : items_widget,
			'stats' : stat_widget,
			'hp' : hp_widget,
			'wallet' : wallet_widget,
			'narration' : narration_widget,
			'choice' : choice_widget

		}

		#Bind the button press to a function
		console_widget.bind('<Return>', self.rtn_pressed)

		#Set focus on the console
		console_widget.focus_set()
		self.setup_tags(actors)

		#Start
		self.navigate()

	#Function to update consoles
	def navigate(self):
		self.clear_middle() #Clear consoles
		self.refresh() #Update secondary consoles
		self.set_title(self.stage_man.current_stage.name) #Set correct window title
		self.stage_man.narrate_current_stage() #Start narration of the stage



	#Event driven fuctions
	def rtn_pressed(self, event):
		print("Input - Enter Key")
		self.stage_man.take_input(self.get_input())
		self.navigate()


	#Game clock update
	def update_clock(self):
		now = time.strftime("%H:%M:%S")
		self.label.configure(text=now)
		self.main.after(1000, self.update_clock)

	#Update GUI widgets

	#sets the proper tags for text formating
	def setup_tags(self, actors):
		for actor in actors.values():
			print(actor.tags)
			self.widgets['narration'].tag_config(actor.tag, actor.tags)
			self.widgets['choice'].tag_config(actor.tag, actor.tags)

	#adds a tag to text
	def add_tag(self, tag, **kw):
		self.widgets['narration'].tag_config(tag, kw)
		self.widgets['choice'].tag_config(tag, kw)

	#Updates the text in a widget
	def update_txt(self, widget, inputstr):
		self.widgets[widget].config(state = NORMAL) # Enable/Diable widgets after use to keep them read only
		self.widgets[widget].delete(1.0, END)
		self.widgets[widget].insert(END, inputstr)
		self.widgets[widget].config(state = DISABLED)

	#Updates the text on a label
	def update_label(self, widget, inputstr):
		self.widgets[widget].configure(text=inputstr)
		#self.widgets[widget].text = inputstr

	#Appends text at the end of a widget
	def add_txt(self, widget, inputstr, tag):
		self.widgets[widget].config(state = NORMAL)
		self.widgets['console'].config(state = DISABLED)
		print(tag)
		for l in inputstr: #Display character by character
			self.widgets[widget].insert(END, l , tag)
			self.widgets[widget].see(END)
			time.sleep(self.narration_speed) #Delay
			self.main.update() #Update main window to avoid freezing
		#if tag == 'on_drugs':
		#	color_list = ['red','blue','green','lightreen','yellow','pink','white','gray']
		#	direction_list = [LEFT, RIGHT, CENTER]
		#	for l in inputstr:
		#		self.widgets[widget].insert(END, l , tag)
		#		self.widgets[widget].tag_config(tag, foreground = secrets.choice(color_list), justify = secrets.choice(direction_list))
		#		self.widgets[widget].see(END)
		#		time.sleep(self.narration_speed)
		#		self.main.update()
		time.sleep(self.waittime)
		self.widgets['console'].config(state = NORMAL)
		self.widgets[widget].config(state = DISABLED)

	#Returns the text in a widget
	def get_txt(self, widget):
		return self.widgets[widget].get(1.0, END)

	#Get input from a widget and normalises it
	def get_input(self):
		con_input = self.widgets['console'].get()
		norm_input = normalise(con_input, self.stage_man.current_stage.choicesinput)
		self.widgets['console'].delete(0, END)
		return norm_input

	#Format and set the window title
	def set_title(self, subtitle = ""):
		if subtitle != "":
			self.main.title(self.title + " - " + subtitle)
		else:
			self.main.title(self.title)

	#Updates the statistics display after every cycle
	def update_stat_display(self):

		update_txt = ""
		for desc, amount in self.player.stats['special'].items():
			num_spaces = 13 - (len(desc) + 2)
			spaces = ''
			for a in range(0,num_spaces):
				spaces += ' '

			update_txt += ' ' + desc.upper() + ': '+ spaces + str(amount) + '\n'
		print ('updating stats:' + str(self.player.stats['special']))
		self.update_txt('stats', update_txt)

		#self.update_txt(player.name + "\n" + str(player.stats['special']))

	#Updates hp bar widget after every cycle
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
		self.update_label('hp', symbols)
		#self.cur_health_symbols = symbols

	#Updates wallet widget after every cycle
	def update_wallet(self):
		global bitcoin_values
		player_wallet = self.player.wallet
		best_symb = ""
		best_val = 100000000000000000000.00
		cur_val = 0.00
		for currency in bitcoin_values:
			cur_val = float(player_wallet/currency['value'])
			if cur_val < best_val and cur_val > 0.10:
				best_val = cur_val
				best_symb = currency['symbol']


		self.update_label('wallet', str(best_val) + " " + str(best_symb))
		#self.cur_health_symbols = symbols

	#Updates inventory display after every cycle
	def update_inv_display(self):
		update_txt = ""
		for item in self.player.inv:
			update_txt += '  ---  ' + item.itemid + '\n'
		self.update_txt('inv', update_txt)

		update_txt_room = ''
		update_txt_room += '     [YOU CAN PICK]\n\n'
		#for item in self.stage_man.current_stage.location.items:
		#	update_txt_room += ' --- ' + item.itemid + '\n'
		#self.update_txt('items', update_txt_room)

	#def update_choices(self):
		#for choice in self.current_stage.choices:
			#self.add_txt('choice', "\t\t\t\t" + choice + "\n", self.player.tag)

	#Refresh displays
	def refresh(self):
		print('refreshing windows')
		self.update_stat_display()
		self.update_inv_display()
		self.update_hp_bar()
		self.update_wallet()

	#Clear the main input/output consoles
	def clear_middle(self):
		print('clearing narration and choice widgets')
		self.update_txt('narration', "")
		self.update_txt('choice', "")

	#Change the image of a widget
	def change_image(self, widget, image_loc):
		new_image = PIL.ImageTk.PhotoImage(PIL.Image.open(image_loc))
		self.widgets[widget].configure(image=new_image)
		self.widgets[widget].image = new_image
		
#Start game
def init():
	window = gui(game_title)
	window.main.mainloop()

init()
