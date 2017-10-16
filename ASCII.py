from utilities import clear
from time import sleep


def draw_ascii(path):
    ascii_file = open(path, 'r')
    for line in ascii_file:
        new_line = line[:-1]
        print(new_line)

def draw_anim_ascii(path):

    a_file = open(path, 'r')
    line_len_list = []
    for line in a_file:
        line_len_list.append(len(line))

    max_len = max(line_len_list)
    for i in range(0, max_len):
        clear()

        ascii_file = open(path, 'r')
        for line in ascii_file:
            new_line = line[:-1]
            print(new_line[0:i])

        sleep(0.005)
