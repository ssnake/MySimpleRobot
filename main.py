#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyGameWorld import *
from MySimpleAI import *
from MySimpleRobot import *
import time


def main():
	rob = MySimpleRobot(1, 1, 90)
	ai = MySimpleAI()
	ai.inputs.v = 2
	ai.inputs.angle_d = 45
	ai.inputs.x_d = 2
	ai.inputs.y_d = 3


	world = PyGameWorld()
	world.add(rob)
	dt = 0.001
	while world.run():
		#t = time.clock()
		ai.process(rob, dt)		
		world.process(dt)
		time.sleep(dt)
		#dt = time.clock() - t
		

	

if __name__ == '__main__':
	main()
