#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import *

class GoToGoal(object):

	def __init__(self):
		self.Kp = 5
		self.Ki = 0.01
		self.Kd = 0.1	
		self.E_I = 0
		self.e_k_prev = 0

	def execute(self, robot, inputs, outputs, dt):
		x, y, angle = robot.get_position()
		x_g = inputs.x_d
		y_g = inputs.y_d
		v = inputs.v
		diff_x = x_g - x
		diff_y = y_g - y
#		print("diff_x", diff_x)
#		print("diff_y", diff_y)


		angle_g = atan2(diff_y, diff_x)
		e_k = angle_g - radians(angle)
		e_k = atan2(sin(e_k), cos(e_k))
		e_P = e_k

		e_I = self.E_I + e_k * dt
		self.E_I = e_I

		e_D = (e_k - self.e_k_prev) / dt
		self.e_k_prev = e_k

		w = self.Kp * e_P + self.Ki * e_I + self.Kd * e_D
		outputs.v = v
		outputs.w = degrees(w)
		



		

