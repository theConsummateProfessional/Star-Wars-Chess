#Issue to work on: get the menu to actually work now
from moviepy.editor import *
import pygame

def initMenu():
	pygame.display.set_caption('Star Wars Chess')

	clip = VideoFileClip('Opening-Crawl.mp4')

	clip.preview(fps = 60)

	pygame.quit()