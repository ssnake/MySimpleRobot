#!/usr/bin/env python
# -*- coding: utf-8 -*-
import World
import pygame
import pdb
import MySimpleRobot
from pygame import *

WIN_WIDTH = 800 #Ширина создаваемого окна
WIN_HEIGHT = 640 # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT) # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = "#000000"
SCALE = 100.0;

class PyGameRobot(object):
	def __init__(self, robot):
		self.robot = robot;
		self.update()
		self.picture = Surface((self.width, self.length))
		self.picture.fill(Color("#FFFFFF"))
		self.update()
	def draw(self, screen):
		
		screen.blit(self.picture, (self.x, self.y))
	def update(self):
		self.x = self.robot.x * SCALE
		self.y = self.robot.y * SCALE
		self.angle = self.robot.angle
		self.width = self.robot.width * SCALE
		self.length = self.robot.length * SCALE
		



class PyGameWorld(World.World):
	def __init__(self):
		super(PyGameWorld, self).__init__()
		self.robotList = [];
		#World.World.__init__(self)
		pygame.init()
		self.screen = pygame.display.set_mode(DISPLAY)
		pygame.display.set_caption("Emulated World") 
		self.bg = Surface((WIN_WIDTH,WIN_HEIGHT)) 
 		self.bg.fill(Color(BACKGROUND_COLOR))   
 	def add(self, robot):
 		self.robotList += [PyGameRobot(robot)]
 		
		 	
 	def update(self):
 		for r in self.robotList:
 			r.update()
 		for e in pygame.event.get():
			if e.type == QUIT:
				self.running = False
			

	def draw(self):
		self.screen.blit(self.bg, (0,0))
		
		for r in self.robotList:
			r.draw(self.screen)
			pass
		pygame.display.flip()
	def process(self):
		self.update()
		self.draw()

		

		
	


