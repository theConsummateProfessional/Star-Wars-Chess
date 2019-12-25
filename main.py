# Ethan Hood
# Star Wars Chess
# Project Start Date: December 14, 2019
# Project End Date: 
# Issue to work on: Add chess pieces tomorrow
import pygame
import menu
import multiprocessing

menu.initMenu()
menu.initCrawl()
pygame.init()

win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Star Wars Chess")


run = True

while run:
	pygame.time.delay(100)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	#pygame.draw.rect(win, (255, 255, 255), (0, 0, 75, 75))

	for y in range(600):
		if((y // 75) % 2 != 0 and y % 75 == 0):
			for x in range(600):
				if(x % 75 == 0 and (x // 75) % 2 != 0):
					pygame.draw.rect(win, (255, 255, 255), (x, y, 75, 75))
		elif((y // 75) % 2 == 0 and y % 75 == 0):
			for x in range(600):
				if(x % 75 == 0 and (x // 75) % 2 == 0):
					pygame.draw.rect(win, (255, 255, 255), (x, y, 75, 75))

	pygame.display.update()


pygame.quit()