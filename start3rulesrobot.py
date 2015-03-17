from __future__ import division
from pygamehelper import *
from pygame import *
from pygame.locals import *
from vec2d import *
from math import e, pi, cos, sin, sqrt
from random import uniform

R = 18      #Radius of circles (Both robots and plates are circles with the same size)
RNUM = 10   #Number of robots
PNUM = 80   #Number of plates
V = 20      #Velocity of movement (Velocity are actually controlled by distance of every movement)

def AvoidOverlap(i,j,r,dis):
    #avoid overlap
    dis = i.pos.get_distance(j.pos)                
    if dis < r*2:
        overlap = r*2 - dis
        dir = j.pos - i.pos
        dir.length = overlap/2
        i.pos = i.pos - dir
        j.pos = j.pos + dir

class Robot():
    def __init__(self):
        self.pos = vec2d(0,0)
        self.dir = vec2d(0,0)
        self.occupied = 0
        
class Plate():
    def __init__(self):
        self.pos = vec2d(0,0)
        self.dir = vec2d(0,0)

class Starter(PygameHelper):
    def __init__(self):
        self.w, self.h = 800, 600
        PygameHelper.__init__(self, size=(self.w, self.h), fill=((255,255,255)))
        
        #generate robots
        self.robots = []
        for i in range(RNUM):
            a = Robot()
            a.pos = vec2d(uniform(R,self.w-R),uniform(R,self.h-R))                                  
            a.dir = vec2d((uniform(-1,1),uniform(-1,1)))
            a.dir.length = V
            self.robots.append(a)
            
        #generate plates
        self.plates = []
        while len(self.plates)<PNUM:
            p = Plate()
            p.pos = vec2d(uniform(R,self.w-R),uniform(R,self.h-R))                 
            if all(p.pos.get_distance(i.pos)>R-3+R-3 for i in self.plates):
                self.plates.append(p)    
            
		
    def update(self):
      
        #wall detection
        for a in self.robots:
            if a.pos[0] < R or a.pos[0] > self.w - R :
                #avoid overlap
                if a.pos[0] < R:
                    dis_w = R - a.pos[0]
                    a.pos[0] = a.pos[0] + dis_w
                if a.pos[0] > self.w-R:
                    dis_w = R-(self.w-a.pos[0])
                    a.pos[0] = a.pos[0] - dis_w
                
                a.dir[0] = -a.dir[0]
            elif a.pos[1] <R or a.pos[1] > self.h - R:
                #avoid overlap
                if a.pos[1] < R:
                    dis_h = R - a.pos[1]
                    a.pos[1] = a.pos[1] + dis_h
                if a.pos[1] > self.h-R:
                    dis_h = R-(self.h-a.pos[1])
                    a.pos[1] = a.pos[1] - dis_h
                
                a.dir[1] = -a.dir[1]
            #move robots
            a.pos = a.pos + a.dir
            
        for a in self.plates:
            if a.pos[0] < R or a.pos[0] > self.w - R :
                #avoid overlap
                if a.pos[0] < R:
                    dis_w = R - a.pos[0]
                    a.pos[0] = a.pos[0] + dis_w
                if a.pos[0] > self.w-R:
                    dis_w = R-(self.w-a.pos[0])
                    a.pos[0] = a.pos[0] - dis_w
                
            elif a.pos[1] <R or a.pos[1] > self.h - R:
                #avoid overlap
                if a.pos[1] < R:
                    dis_h = R - a.pos[1]
                    a.pos[1] = a.pos[1] + dis_h
                if a.pos[1] > self.h-R:
                    dis_h = R-(self.h-a.pos[1])
                    a.pos[1] = a.pos[1] - dis_h

            
        #robot meets robot detection
        for i in self.robots:
            for j in self.robots:
                if i == j: continue
                #avoid overlap
                dis = i.pos.get_distance(j.pos)                
                if dis < R*2:
                    AvoidOverlap(i,j,R,dis)
                    #robots turn around
                    i.dir , j.dir = -i.dir , -j.dir
                    
               
        #robot meets plate detection
        for r in self.robots:
            for p in self.plates:
                dis = r.pos.get_distance(p.pos)
                if dis < R+R-3:
                    
                    #avoid overlap
                    AvoidOverlap(r,p,R-1.5,dis)
                    
                    if r.occupied == 0:
                        #pick up plate and turn around
                        r.occupied = 1
                        r.pos = p.pos
                        self.plates.remove(p)
                        r.dir = -r.dir
                        
                    else:
                        #drop down plate and turn around
                        r.occupied = 0
                        q = Plate()
                        q.pos = r.pos
                        self.plates.append(q)
                        r.dir.length = 2*R-3
                        r.pos = r.pos - r.dir
                        r.dir.length = V
                        r.dir = -r.dir
                        
        #avoid plate-plate overlap
        for i in self.plates:
            for j in self.plates:
                if i==j: continue
                #avoid overlap
                dis = i.pos.get_distance(j.pos)                
                if dis < (R-3)*2:
                    AvoidOverlap(i,j,R-3,dis)
      
        
    def keyUp(self, key):
        if key == K_p:
            self.waitForKey()
        
    def mouseUp(self, button, pos):
        pass
        
    def mouseMotion(self, buttons, pos, rel):
        pass
        
    def draw(self):
        self.screen.fill((255,255,255))
        for a in self.robots:
            if a.occupied == 0:
                pygame.draw.circle(self.screen, (255,0,0), a.pos.inttup(), R)
            else:
                pygame.draw.circle(self.screen, (255,0,0), a.pos.inttup(), R)
                pygame.draw.circle(self.screen, (0,255,0), a.pos.inttup(), R-3)

        for p in self.plates:
            pygame.draw.circle(self.screen, (0,255,0), p.pos.inttup(), R-3)
        
s = Starter()
s.mainLoop(50)
