# import numpy as np 
# import cv2
from moviepy.editor import *
import pygame

def initMenu():
	pygame.display.set_caption('Pls work')

	clip = VideoFileClip('Opening-Crawl.mp4')

	clip.preview(fps = 60)

	pygame.quit()