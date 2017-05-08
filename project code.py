#This program teaches the scribler to write sentenses
#The user can enter a sentence and the robot will type it letter by letter
def d(size , word):
	#function that finds the each letter intividualy and calls
	#that letter's function with the commands that the S2 will
	#draw the letter on the paper
	def find(xy,letter):
		if letter=='A' or letter=='a':
			a(xy)
		elif letter=='B' or letter=='b':
			b(xy)
		elif letter=='C' or letter=='c':
			c(xy)
		elif letter=='D' or letter=='d':
			d(xy)
		elif letter=='E' or letter=='e':
			e(xy)
		elif letter=='F' or letter=='f':
			f(xy)
		elif letter=='G' or letter=='g':
			g(xy)
		elif letter=='H' or letter=='h':
			h(xy)
		elif letter=='I' or letter=='i':
			i(xy)
		elif letter=='J' or letter=='j':
			j(xy)
		elif letter=='K' or letter=='k':
			k(xy)
		elif letter=='L' or letter=='l':
			l(xy)
		elif letter=='M' or letter=='m':
			m(xy)
		elif letter=='N' or letter=='n':
			n(xy)
		elif letter=='O' or letter=='o':
			o(xy)
		elif letter=='P' or letter=='p':
			p(xy)
		elif letter=='Q' or letter=='q':
			q(xy)
		elif letter=='R' or letter=='r':
			r(xy)
		elif letter=='S' or letter=='s':
			s(xy)
		elif letter=='U' or letter=='u':
			u(xy)
		elif letter=='V' or letter=='v':
			v(xy)
		elif letter=='W' or letter=='w':
			w(xy)
		elif letter=='X' or letter=='x':
			x(xy)
		elif letter=='Y' or letter=='y':
			y(xy)
		elif letter=='Z' or letter=='z':
			z(xy)
		elif letter==' ' or letter=='_':
			space()
		else:
			print "Wrong entry. Please enter only letters from A-Z"
	#A
	def a():
		turnRight(0.5,0.4)
		forward(0.5,2*xy)
		turnRight(0.5,2.2)
		forward(0.5,xy)
		turnRight(0.5,2)
		forward(0.4,xy)
		turnRight(0.5,3.2)
		forward(0.4,xy)
		turnRight(0.5,1)
		forward(0.5,xy)
		turnLeft(0.5,1)
		forward(0.3,xy)
		markerspace(1)
	
	#H
	def h(xy):
		forward(0.3,2*xy)
		turnLeft(0.5,1.6)
		forward(0.5,2*xy)
		turnRight(0.5,3.2)
		forward(0.5,xy)
		turnLeft(0.5,1.6)
		forward(0.5,xy)
		turnLeft(0.5,1.6)
		forward(0.5,xy)
		turnRight(0.5,3.2)
		forward(0.5,2*xy)
		turnLeft(0.5,1.6)
		markerspace(1)

	#D
	def d(xy):
		turnLeft(0.5,1.6)
		forward(0.5,2*xy)
		turnRight(0.5,1.6)
		if xy==0.5:
			startTime = currentTime()
			while (currentTime() - startTime) < 3.8:
				motors(0.6,-0.2)
			stop()
		elif xy==1:
			startTime = currentTime()
			while (currentTime() - startTime) < 6:
				motors(0.5,0)
			stop()
		turnLeft(0.5,3)
		markerspace(0)
	
	#E
	def e(xy):
		turnLeft(0.5,1.6)
		forward(0.5,2*xy)
		turnRight(0.5,1.5)
		forward(0.5,xy)
		turnRight(0.5,3.1)
		forward(0.5,xy)
		turnLeft(0.5,1.5)
		forward(0.5,xy)
		turnLeft(0.5,1.5)
		forward(0.5,xy)
		turnRight(0.5,3.2)
		forward(0.5,xy)
		turnLeft(0.5,1.6)
		forward(0.5,xy)
		turnLeft(0.5,1.6)
		forward(0.5,xy)
		backward(0.5,xy)
		forward(0.5,xy)
		markerspace(1)

	#L	
	def l(xy):
		turnLeft(0.5,1.6)
		forward(0.5,2*xy)
		turnRight(0.5,3.2)
		forward(0.5,2*xy)
		turnLeft(0.5,1.6)
		forward(0.5,xy)
		markerspace(1)

	#O
	def o(xy):
		if xy==0.5:
			startTime = currentTime()
			while (currentTime() - startTime) < 8.3:
				motors(-0.2,0.6)
			stop()
			markerspace(0)
		elif xy==1:
			startTime = currentTime()
			while (currentTime() - startTime) < 8.3:
				motors(-0.1,0.6)
			stop()
			markerspace(0)

	#W
	def w(xy):
		turnLeft(0.5,2)
		forward(0.5,2*xy)
		turnRight(0.5,3.2)
		forward(0.5,2*xy)
		turnLeft(0.5,2)
		forward(0.5,xy)
		turnRight(0.5,1.5)
		forward(0.5,xy)
		turnLeft(0.5,1.8)
		forward(0.5,2*xy)
		turnRight(0.5,3.2)
		forward(0.5,2*xy)
		turnLeft(0.5,2)
		markerspace(2)

	#R
	def r(xy):
		turnLeft(0.5,1.6)
		forward(0.5,2*xy)
		turnRight(0.5,1.6)
		if xy==0.5:
			startTime = currentTime()
			while (currentTime() - startTime) < 3.5:
				motors(0.6,-0.3)
			stop()
		elif xy==1:
			startTime = currentTime()
			while (currentTime() - startTime) < 3.5:
				motors(0.6,-0.2)
			stop()
		turnLeft(0.5,2.3)
		forward(0.5,xy)
		turnLeft(0.5,0.7)
		forward(0.5,2*xy)
		markerspace(1)


	#Space between words		
	def space():
		markerspace(0)
		changeline()


	def markerspace(number):
		if number==1:
			beep(2,500)
			forward(0.3,0.5)
			beep(0.5,500)
			beep(0.5,700)
			beep(0.5,900)
		elif number==0:
			beep(2,500)
			forward(0.3,1)
			beep(0.5,500)
			beep(0.5,700)
			beep(0.5,900)
		elif number==2:
			beep(2,500)
			forward(0.5,1)
			beep(0.5,500)
			beep(0.5,700)
			beep(0.5,900)

	def checkforobstacle(bn):
		bool = True
		x =0
		y =0
		while True:
			if bn==0:
				if getObstacle() == [0, 0, 0]:
					x=3
				else:
					stop()
					print "I see an obstacle"
					if y==0:
						beep(0.5,900)
						beep(0.5,700)
						beep(0.5,500)
						y=y+1
					x = x+1
					wait(1)
			elif bn==1:
				if getObstacle() == [0,0,0]:
					forward()
				else:
					stop()
					turnRight(0.5,3.2)
					x=3
				
				
			if x==3:
				break
				break
			continue
		
	def party():
		def goround():
			startTime=currentTime()
			while(currentTime()-startTime)<3.5:
				motors(1,-1)
			stop()
		def shake():
			motors(1,0)
			motors(-1,0)
			motors(0,1)
			motors(0,-1)
			motors(1,0)
			motors(-1,0)
			motors(0,1)
			motors(0,-1)
			stop()
		def soundme():
			beep(0.5,1100)
			beep(0.5,900)
			beep(0.5,700)
			beep(0.5,500)
			beep(0.5,600)
			beep(0.5,700)
			beep(0.5,800)
			beep(0.5,900)
		soundme()
		goround()
		shake()
		shake()
		shake()
		shake()

	def changeline():
		turnRight(0.5,1.6)
		forward(0.5,2.5)
		turnRight(0.5,1.6)
		checkforobstacle(1)


	#Main
	x=0
	if size=="large" or size=="l" or size=="L" or size=="Large" or size=="LARGE":
		xy=1
	else:
		xy=0.5
	loop=True
	while loop:
		if word[x]!="&":
			checkforobstacle(0)
			print "writing letter..... ", word[x]
			find(xy,word[x])
			x=x+1
		else:
			party()
			print "End of the process"
			loop=False