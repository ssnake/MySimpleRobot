#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MySimpleRobot
import sys
#add controllers folder
sys.path.append('controllers' )
import GoToAngle

class Inputs(object):
	def __init__(self):
		self.x_d = 0
		self.y_d = 0
		self.angle_d = 0
		self.v = 0
		self.w = 0
class Outputs(object):
	def __init__(self):
		self.v = 0
		self.w = 0

#container for different strategies and controllers
class MySimpleAI(object):
	def __init__(self):
		self.inputs = Inputs()
		self.outputs = Outputs()
		self.controllers = [GoToAngle.GoToAngle()];
		self.current_controller= self.controllers[0]
	def process(self, robot, dt):
		if self.current_controller is None:
			return

		#print('inputs.v', self.inputs.v)
		self.current_controller.execute(robot, self.inputs, self.outputs, dt)
		robot.set_outputs(self.outputs)
		