asciiWidth = 9
asciiHeight = 6

class art:
	
	chars = ""
	same2 = 0.5
	same3 = 1

	def __init__(self, chars, same2, same3):
		self.chars = chars
		self.same2 = same2
		self.same3 = same3
	
#Cherry
asciiArt = [art("  __       \_\        \        /\      0  0           ", 0.5, 1),
	#Bell
	art("    _       / \     /   \   /__ __\     0             ", 0.5, 5),
	#Lemon
	art("           _____   /     \ <       > \_____/          ", 0.5, 1),
	#Orange
	art("           .---.   /#    \  \     /   '---'           ", 0.5, 1),
	#Star
	art("    '     __/ \__  \     /  /_   _\    \ /       '    ", 0.5, 1),
	#Skull
	art("          /     \ | () () | \  ^  /   |||||    |||||  ", -1, None)]
