#!/usr/bin/env python
# -*- coding: utf-8 -*-
class MySimpleRobot(object):
	"""a container of current params of robot"""
	def __init__(self, x=0, y=0, angle=0):
		self._x = x
		self._y = y
		self._angle  = angle
		self._width  = .2
		self._length = .2
		self._velocity = 0
	def get_x(self):
		return self._x
	def set_x(self, x):
		self._x = x
	x = property(get_x, set_x)
	def get_y(self):
		return self._y
	def set_y(self, y):
		self._y = y
	y = property(get_y, set_y)
	def get_angle(self):
		return self._angle
	def set_angle(self, angle):
		self._angle = angle
	angle = property(get_angle, set_angle)
	def get_width(self):
		return self._width
	def set_width(self, width):
		self._width = width
	width = property(get_width, set_width)	
	def get_length(self):
		return self._length
	def set_length(self, length):
		self._length = length
	length = property(get_length, set_length)		
	def get_velocity(self):
		return self._velocity
	def set_velocity(self, velocity):
		self._velocity = velocity
	velocity = property(get_velocity, set_velocity)			




def main():
	r = MySimpleRobot();
	
	return 0

if __name__ == '__main__':
	main()

