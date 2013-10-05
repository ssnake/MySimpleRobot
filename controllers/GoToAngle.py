#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import *

class GoToAngle(object):
	def __init__(self, Kp=10):
		self.Kp = Kp
	def execute(self, robot, inputs, outputs, dt):
		x, y, angle = robot.get_position()
		v = inputs.v
		angle_d = inputs.angle_d

		e_k = radians(angle_d - angle - 90)
		e_k = degrees(atan2(sin(e_k), cos(e_k)))
		w = self.Kp*e_k
		outputs.v = v
		outputs.w = w



		

