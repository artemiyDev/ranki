# from googletrans import Translator
#
# translator = Translator()
#
# print(translator.translate(text='thinking', src='en', dest='ru').pronunciation)
from PyDictionary import PyDictionary

dictionary = PyDictionary()


print (dictionary.translate("perhaps",'ru'))