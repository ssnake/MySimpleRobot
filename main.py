#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyGameWorld import *
from MySimpleAI import *

rob = MySimpleAI(1, 1, 90)

def main():
	world = PyGameWorld()
	world.add(rob)
	rob.desired_velocity = 0.01 #1 cm per sec
	while world.run():
		world.process()
		rob.process()

	

if __name__ == '__main__':
	main()
