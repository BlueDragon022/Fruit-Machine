import random
import time
import math
import clearScreen
import asciiArt

width = 27
height = 15

txtBuffer = ["="] * width * height

def renderToScreen():
	clearScreen.clearScreen()
	for y in range(0, height, 1):
		line = ""
		for x in range(0, width, 1):
			line += str(txtBuffer[x + y * width])
		print(line)

def renderToBuffer(x, y, chars, w, h):
	for yc in range(0, h, 1):
		if yc > height:
			continue
		for xc in range(0, w, 1):
			if xc > width:
				continue
			txtBuffer[(x + xc) + (y + yc) * width] = chars[xc + yc * w]

def clearBuffer():
	for a in range(0, len(txtBuffer), 1):
		txtBuffer[a] = " "

def winnings(winnings):
	if winnings == None:
		renderToBuffer(0, 7, "You have lost everything!", 25, 1)
	elif winnings > 0:
		renderToBuffer(0, 7, "You have won £" + str(winnings) + "!" , 15 + len(str(winnings)), 1)
	elif winnings == 0:
		renderToBuffer(0, 7, "You have won nothing!", 21, 1)
	elif winnings < 0:
		renderToBuffer(0, 7, "You have lost £" + str(winnings * -1) + "!", 16 + len(str(winnings * -1)), 1)

def game():
	credit = 1
	
	clearScreen.clearScreen()

	print ("Welcome to this fruit machine!\nIf you get 2 fruit you win 50p\nand if you get 3 fruit you win £1\nbut if you're lucky enough and\nget 3 bell's you win £5!\nhowever if you get\ntwo skulls you will lose £2\nand if you're unluckyy enough to get 3..\nYou lose everything.\nEach roll costs 20p.")
	input("Press enter to start...")

	while credit > 0:
		#Each roll costs 20p
		credit = math.floor((credit * 100) - 20) / 100

		clearBuffer()

		fruit = [0]*3
		print (fruit)
		for i in range(0, len(fruit), 1):
			fruit[i] = random.randrange(0, 6)

		for f in range(0, len(fruit), 1):		
			renderToBuffer(f * asciiArt.asciiWidth, 1, asciiArt.asciiArt[fruit[f]].chars, asciiArt.asciiWidth, asciiArt.asciiHeight)

		winningFruit = -1
		same = 0
		for x in fruit:
			if (same == 3) or (same == 2):
				break
			else:
				same = 0
			
			for y in fruit:
				if x == y:
					same += 1

				if (same == 3) or (same == 2):
					winningFruit = y

		win = asciiArt.asciiArt[winningFruit].same3 if same == 3 else asciiArt.asciiArt[winningFruit].same2 if same == 2 else 0
		winnings(win)
		if win == None:
			credit = 0
		else:
			credit = math.floor((credit * 100) + (win * 100)) / 100
	
		renderToBuffer(18 - len(str(credit)), 0, "Credit: £" + str(credit), 9 + len(str(credit)), 1)

		renderToScreen()
		if credit >= 0.2:
			while True:
				inp = input("Would you like to roll again it costs 20p?").lower()
				if inp in ["yes", "y"]:
					break
				elif inp in ["no", "n"]:
					print ("You are leaving with", credit)
					time.sleep(5)
					quit()
				else:
					print ("Not a valid answer...")
		else:
			print ("Sorry you don't have enough money...")
			time.sleep(5)
			quit()
			
game()
