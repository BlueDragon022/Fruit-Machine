import os
import platform

#Function to clear the screen
def clearScreen():
	#This goes through different os's and uses the correct command to clear the terminal/console
	if platform.system() == "Windows":
		os.system("cls")
	elif platform.system() == "Linux":
		os.system("clear")
	elif platform.system() == "Darwin": #MacOS
		os.system("clear")
	else:
		os.system("clear")
