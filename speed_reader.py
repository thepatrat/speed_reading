from utils.helpers import _load_txt, _txt_2_words, _speed_reader
from kivy.app import App
from kivy.uix.button import Button
 
class Speed_Reader(App):
    def build(self):
        return Button(text= " Hello Kivy World ")

    def _get_words(self, filename):
        """ Gets a word list from a txt file """
        words = _txt_2_words(_load_txt(filename))
        return words

    def _print_words_to_button(self, words):
        for word in words:
            return Button(text= word)
    
