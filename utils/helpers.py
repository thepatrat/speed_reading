import time
import rich

def _load_txt(filename):
    with open(filename, "r") as file:
        text = file.read()
    return text

def _txt_2_words(text):
    words = text.split()
    return words

def _print_interface()

def _speed_reader(filename):
    wpm = int(input("How fast you wanna go? \n"))
    words = _txt_2_words(_load_txt(filename))
    for word in words:
        print(f"        {word}                   ", end='\r')
        time.sleep(float(60 / wpm))

_speed_reader("bible.txt")