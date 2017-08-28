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
	if any(word in strip(intext) for word in data['yes']) or strip(intext) == "y":
		return True
	elif any(word in strip(intext) for word in data['no']) or strip(intext) == "n":
		return False
	else:
		return "?"

def tonumber( intext ):
	final_exp_digits = 0
	outtext = ""
	intext = intext.lower().strip().translate({ord(i):" " for i in  "?!@#$%^&*',.:;+=/\|][}{-_("}).split()
	tenifier = False
	for i in intext:
		if i == "and":
			continue

		suffix = ""

		#Places
		if i == "hundred":
			exp_digits = 3
		elif i == "thousand":
			exp_digits = 4 if not tenifier else 5
		elif i == "million":
			exp_digits = 7 if not tenifier else 8
		elif i == "billion":
			exp_digits = 10 if not tenifier else 11
		elif "ty" in i:
			exp_digits = 2
		else:
			exp_digits = 0

		#Numbers
		if i in ['one']:
			suffix = "1"
		elif i in ['two','twenty']:
			suffix = "2"
		elif i in ['three','thirty']:
			suffix = "3"
		elif i in ['four', 'forty']:
			suffix = "4"
		elif i in ['five','fifty']:
			suffix = "5"
		elif i in ['six', 'sixty']:
			suffix = "6"
		elif i in ['seven','seventy']:
			suffix = "7"
		elif i in ['eight', 'eighty']:
			suffix = "8"
		elif i in ['nine','ninety']:
			suffix = "9"

		# Teens
		if i == 'ten':
			suffix = "10"
			tenifier = True
		elif i == 'eleven':
			suffix = "11"
			tenifier = True
		elif i == 'twelve':
			suffix = "12"
			tenifier = True
		elif i == 'thirteen':
			suffix = "13"
			tenifier = True
		elif i == 'fourteen':
			suffix = "14"
			tenifier = True
		elif i == 'fifteen':
			suffix = "15"
			tenifier = True
		elif i == 'sixteen':
			suffix = "16"
			tenifier = True
		elif i == 'seventeen':
			suffix = "17"
			tenifier = True
		elif i == 'eighteen':
			suffix = "18"
			tenifier = True
		elif i == 'nineteen':
			suffix = "19"
			tenifier = True
		else:
			tenifier = False

		# Expected digits
		if exp_digits > final_exp_digits:
			final_exp_digits += exp_digits
		else:
			for i in range(final_exp_digits - len(outtext) - exp_digits):
				outtext += "0"

		outtext += suffix

	# Extra zeros
	for i in range(final_exp_digits-len(outtext)):
		outtext += "0"

	return outtext


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
