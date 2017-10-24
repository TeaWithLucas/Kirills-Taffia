from time import sleep
#from data import global_game_items
import os
import re
import string
import decimal

#Displaying ASCII drawing
def draw_ascii(path):
	out = ''
	ascii_file = open(path, 'r')
	for line in ascii_file:
		out += line
	return out
#Displaying ascii drawing with effect
def draw_anim_ascii(path, gui, output_widget):
	out = ''
	a_file = open(path, 'r')
	line_len_list = []
	for line in a_file:
		line_len_list.append(len(line))

	max_len = max(line_len_list)
	for i in range(0, max_len):
		ascii_file = open(path, 'r')
		for line in ascii_file:
			new_line = line
			gui.update_txt(output_widget,new_line[0:i])

#Norm input by removing spaces and punct
def normalise(text, keep_words):
	print()
	no_punct = re.sub(r'[^\w\s]','',text)
	no_space = re.sub(r'^\s+|\s+$','',text)
	final = filter_input(no_space, keep_words)
	return no_space.lower()


#Filter to remove uselees words
def filter_input(text, keep_words):
	print('Flitering...')
	words = text.split(' ')
	new_words = []
	for word in words:
		if word in keep_words:
			new_words.append(word)
	if len(new_words) < 1:
		new_words = [""]
	return new_words
