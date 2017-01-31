import pygame, sys, time, os




pygame.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()
screen = pygame.display.set_mode((400,300))


	

interval = 0.1
try:
	run = True
	while run:
		events = pygame.event.get()
		for event in events:

			# Check if one of the joysticks has moved
			if event.type == pygame.JOYAXISMOTION:
				if event.axis == 1:
					print "event.axis == 1"
				
				if event.axis == 2:
					print "event.axis == 2"

				if event.axis == 3:
					print "event.axis == 3"
					
			if event.type == pygame.JOYBUTTONDOWN:
				if event.button == 0:	#select
					run = False
				if event.button == 3:	#start
					reset()
				if event.button == 12:	#triangle
					sc.setAngle(grip, 90)
				if event.button == 14:	#X
					sc.setAngle(grip, 30)
				else:
					print event.button
					
		time.sleep(interval)
except KeyboardInterrupt:
	pass

except Exception as e:
	print e
	pass


sc.clean_up()
