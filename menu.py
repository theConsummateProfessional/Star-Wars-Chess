#Issue to work on: get the menu to actually work now
from moviepy.editor import *
import pygame

def createFont(t, s = 72, c = (255, 255, 0), b = False, i = False):
	font = pygame.font.SysFont("Arial", s, bold = b, italic = i)
	text = font.render(t, True, c)
	return text

def initCrawl():
	bg = pygame.image.load('Death-Star.png')
	win = pygame.display.set_mode((958, 540))
	pygame.display.set_caption('Star Wars Chess')

	clip = VideoFileClip('Opening-Crawl.mp4')

	clip.preview(fps = 60)


	white = (255, 255, 255)
	play = createFont("Play Now")
	settings = createFont("Settings")
	quit = createFont("Quit")

	run = True

	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()

		win.blit(bg, (0,0))


		#pygame.draw.rect(win, (0, 0, 0), (50, 50, 200, 60))
		win.blit(play, (50, 50))
		win.blit(settings, (50, 197))
		win.blit(quit, (50, 344))
		pygame.display.update()


	pygame.quit()



