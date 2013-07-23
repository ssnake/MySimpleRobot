#!/usr/bin/env python
# -*- coding: utf-8 -*-
#sys.path.append('/')
import sys
import pdb

try:
    import sdl2.ext as sdl2ext
except ImportError:
    import traceback
    traceback.print_exc()
    sys.exit(1)

from sdl2.ext import Resources
RESOURCES = Resources(__file__, "resources")

from MySimpleRobot import *

class MySimpleSDLRobot(MySimpleRobot):
	def __init__(self):
		pdb.set_trace();
		sdl2ext.init ()
		window = sdl2ext.Window("Hello World!", size=(640, 480))
		window.show()

		factory = sdl2ext.SpriteFactory(sdl2ext.SOFTWARE)
		sprite = factory.from_image(RESOURCES.get_path("DifferentialDriveRobot.png"))

		spriterenderer = factory.create_sprite_renderer(window)
		spriterenderer.render(sprite)
		processor = sdl2ext.TestEventProcessor()
		processor.run(window)
	def paint(self):
		pass;
	def update(self):
		pass;
	pass;


def main():
	
	r = MySimpleSDLRobot();
	return 0

#if __name__ == '__main__':
main()

