#!/usr/bin/env python
# -*- coding: utf-8 -*-
import World
import pygame
import pdb
import math
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
		self.update(0)
		self.picture = Surface((self.width, self.length))
		self.picture.fill(Color("#FFFFFF"))
		
	def draw(self, screen):
		
		screen.blit(self.picture, (self.x, self.y))
	def update(self, dt):
		x, y, angle = self.robot.get_position()
		v, w = self.robot.get_dynamics()
		x = x + v*math.cos(math.radians(angle))*dt
		y = y - v*math.sin(math.radians(angle))*dt
		angle = angle + w*dt


		self.x = x * SCALE
		self.y = y * SCALE
		self.angle = angle
		self.width = self.robot.width * SCALE
		self.length = self.robot.length * SCALE

		self.robot.set_position(x,y,angle)
		self.robot.set_dynamics(v, w)
		



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
 		
		 	
 	def update(self, dt):
 		for r in self.robotList:
 			r.update(dt)
 		for e in pygame.event.get():
			if e.type == QUIT:
				self.running = False
			

	def draw(self):
		self.screen.blit(self.bg, (0,0))
		
		for r in self.robotList:
			r.draw(self.screen)
			pass
		pygame.display.flip()
	def process(self, dt):
		self.update(dt)
		self.draw()

		

		
	


