#!/usr/bin/env python
# -*- coding: utf-8 -*-
#sys.path.append('/')
import sys
import pdb
import SDLEngine as sdlengine


try:
    import sdl2.ext as sdl2ext
except ImportError:
    import traceback
    traceback.print_exc()
    sys.exit(1)

from sdl2.ext import Resources
RESOURCES = Resources(__file__, "resources")

from MySimpleRobot import *

class MySimpleSDLRobot(sdlengine.SDLObject):

		
	def __init__(self, world, sdlEngine, posx, posy):
		
		super.__init__(self, world)
	pass



def main():
	pdb.set_trace() 
	engine = sdlengine.SDLEngine()
	r = MySimpleSDLRobot(engine.world, engine, 0 ,0)
	engine.add(r)
	sys.exit(engine.run())
	

		

		
	return 0

#if __name__ == '__main__':
main()

