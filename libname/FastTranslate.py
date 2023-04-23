from mtranslate import translate

def Translator(text, lang):
	result = translate(text, lang)
	return result 