#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pdb
import sys
try:
    from sdl2 import *
    import sdl2.ext as sdl2ext
except ImportError:
    import traceback
    traceback.print_exc()
    sys.exit(1)
    
   
class SoftwareRenderer(sdl2ext.SoftwareSpriteRenderer):
	
	def render(self, components):
		sdl2ext.fill(self.surface, sdl2ext.Color(0,0,0))
		super(SoftwareRenderer, self).render(components)
	 
class SDLObject(sdl2ext.Entity):
	def __init__(self, world, sprite, posx=0, posy=0):
		self.sprite = sprite
		self.sprite.position = posx, posy
		
	def paint(self):
		pass
	def update(self):
		pass
		
class SDLEngine():
	
	def __init__(self):

		self.world = sdl2ext.World()
		
		

		
	def run(self):
		sdl2ext.init()
		window = sdl2ext.Window("Robot Sandbox", size=(640, 480))
		window.show()
		
		spriteRender = SoftwareRenderer(window)
		self.world.add_system(spriteRender)
		
		running = True
		while running:
			events = sdl2ext.get_events()
			for event in events:
				#pdb.set_trace()
				if event.type == SDL_QUIT:
					runnig = False
					break
			self.world.process()
			window.refresh()
		return 0
					
		
	def add(self, sdl_object):
		self.world.add_system(sdl_object);
		
	 

def main():
	engine = SDLEngine()
	sys.exit(engine.run())
	

if __name__ == '__main__':
	main()

