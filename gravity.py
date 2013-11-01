#!/usr/bin/env python
# -*- coding: utf-8 -*-

import PyGameWorld
from pygame import *
import time
from math import *
magn = 384403 / 300
class Planet(object):
	def __init__(self, pos, vel, mass):
		self.pos = pos
		self.vel = vel
		self.prev_pos = pos
		self.prev_vel = vel
		self.f = [0, 0]
		self.mass = mass
		
		self.picture = Surface((10, 10))
		self.picture.fill(Color("#FFFFFF"))
		
	def draw(self, screen):
		
		screen.blit(self.picture, (self.pos[0] / magn, self.pos[1]/magn))
	def update(self, dt):
		self.vel[0] = self.prev_vel[0] + self.f[0]*dt
		self.vel[1] = self.prev_vel[1] + self.f[1]*dt

		self.pos[0]=self.prev_pos[0]+self.vel[0]*dt
		self.pos[1]=self.prev_pos[1]+self.vel[1]*dt

	def addForce(self, f):
		self.f = f
	def calc_dist(self, planet):
		return sqrt(pow(planet.pos[0] - self.pos[0],2)+pow(planet.pos[1] - self.pos[1],2))
	def calc_angle(self, planet):
		
		angle = atan2((self.pos[1] - planet.pos[1]),(-self.pos[0] + planet.pos[0]))
		#moonangle = atan2(sin(angle), cos(angle))
		return angle

def main():
	world = PyGameWorld.PyGameWorld()
	earth = Planet([4e5,3e5], [0,0], 6e24)
	moon = Planet([6e5,3e5], [0,10], 1e22)
	world.add(earth)
	world.add(moon)
	g = 7e-11
	dt = 0.0001
	while world.run():		
		r = earth.calc_dist(moon)

		angle = moon.calc_angle(earth)

		fp = g*earth.mass*moon.mass/r/r/10000000000
		f = [0,0]
		f[0]=fp*cos(angle)
		f[1]=fp*sin(angle)
		print r, degrees(angle), f[0]
		moon.addForce(f)
		world.process(dt)
		#time.sleep(dt)
	
	return 0

if __name__ == '__main__':
	main()