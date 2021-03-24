import sys

def split( string ):
	return [ char for char in string ]

filename = sys.argv[1]
sourceCode = open(filename,'r').read()
sourceCode = sourceCode.replace( "\n", "" ).replace( "\t", "" ).replace( " ", "" )

letters = split( sourceCode )
comment = False
printNext = False
assigning = False

varList = [ "a", "b", "d", "g", "h", "j", "k", "l", "t", "u", "v", "w", "y", "z" ]
variables = {}

for letter in letters:

	if comment:
		comment = False
		continue
	elif assigning:
		assigning = False
		variables[ lastLett ] = letter
		continue
	elif printNext:
		printNext = False
		print( variables[ lastLett ] )
		continue

	if letter in varList:
		lastLett = letter

	if letter == "c":
		comment = True
	elif letter == "e":
		assigning = True
	#elif letter == "f":
	#
	#elif letter == "i":
	#
	#elif letter == "m":
	#
	#elif letter == "n":
	#
	#elif letter == "o":
	#
	elif letter == "p":
		printNext = True
	#elif letter == "q":
	#
	#elif letter == "r":
	#
	#elif letter == "s":
	#
	#elif letter == "x":
	#