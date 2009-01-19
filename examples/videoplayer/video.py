from pymt import *
import os
import random
from pyglet.media import *

class MTVideoObj(MTScatterWidget):
    """MTScatteredObj is a zoomable Image widget with a possibility of providing rotation during spawning"""
    def __init__(self, parent=None, pos=(0,0), size=(0,0), rotation=0):
        MTScatterWidget.__init__(self,parent,pos,size)
        self.rotation = rotation
        self.x = pos[0]
        self.y = pos[1]
        self.player = Player()
        self.source = pyglet.media.load('video.avi')
        self.player.queue(self.source)
        self.width = self.player.get_texture().width
        self.height = self.player.get_texture().height
  
    def play(self):
        self.player.play()

    def draw(self):
        glPushMatrix()
        glColor3d(1,1,1)
        self.player.get_texture().blit(0,0)
        glPopMatrix()   

                


if __name__ == '__main__':
    w = MTWindow()
    w.set_fullscreen()
    video = MTVideoObj()
    w.add_widget(video)
    video.play()
    runTouchApp()
