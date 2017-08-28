# jtext -- A library to handle your text-based needs.
# Jake Ledoux, 2017
import os, re

data = {}

for dataset in os.listdir(os.path.realpath(__file__)[:-11]):
	if ".txt" in dataset:
		with open(os.path.realpath(__file__)[:-11]+dataset,"r") as f:
			data[dataset[:-4]] = f.read().strip().split("\n")

def strip( intext ):
	return intext.lower().strip().translate({ord(i):None for i in  "?!@#$%^&*',.:;+=/\|][}{-_( "})

def censor( intext ):
	outtext = ""
	for word in re.split(r'(\s+)', intext):
		if word.lower() in data['curses']:
			censored_word = ""
			for i in range(len(word)):
				censored_word += "*"
			outtext += censored_word
		else:
			outtext += word
	return outtext

def getnames( intext ):
	outtext = []
	for word in intext.split():
		if word.upper() in data['names_first_f']+data['names_first_m']+data['names_last']:
			outtext += [word.title()]
	return outtext

def capitalizenames( intext ):
	outtext = ""
	for word in re.split(r'(\s+)', intext):
		if word.upper() in data['names_first_f']+data['names_first_m']+data['names_last']:
			outtext += word.title()
		else:
			outtext += word
	return outtext

def gender( intext ):
	if intext.upper() in data['names_first_f'] and intext.upper() in data['names_first_m']:
		return "?"
	elif intext.upper() in data['names_first_f']:
		return "female"
	elif intext.upper() in data['names_first_m']:
		return "male"
	else:
		return "?"

def yesno( intext ):
	if any(word in strip(intext) for word in data['yes']):
		return True
	elif any(word in strip(intext) for word in data['no']):
		return False
	else:
		return "?"

def main():
	quit = False
	while not quit:
		intext = input("> ")
		if intext == "quit":
			quit == True
		else:
			print(yesno(intext))

if __name__ == '__main__':
	main()
