#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MySimpleRobot
class MySimpleAI(MySimpleRobot.MySimpleRobot):
	def __init__(self, x=0, y=0, angle=0):
		super(MySimpleAI, self).__init__( x, y, angle)
		self.desired_velocity = 0
	def process(self):
		if self.desired_velocity > self.velocity:
			self.velocity += .001
		self.x += self.velocity
		print("robot x ", self.x)
		print("robot velocity ", self.velocity)
		