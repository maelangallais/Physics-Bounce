#Créé le 20 Décembre 2023
from math import *
from kandinsky import *
from time import *

def ent(n):
  if n-floor(n)<0.5:n=floor(n)
  else:n=ceil(n)
  return int(n)

bl,wh=(0,0,0),(255,255,255)
c=100

def fil(x,y,a,r):
  an=radians(a)
  px,py=cos(an),sin(an)
  if a==0:
    ax,ay=px,py
  elif a<90:
    ax,ay=px/py,py/px
  elif a==90:
    ax,ay=px/py,py
  elif a<=180:
    ax,ay=px/py,py/-px
  elif a<=270:
    ax,ay=px/-py,py/-px
  elif a<=360:
    ax,ay=px/-py,py/px
  if ax>1:ax=1
  elif ax<-1:ax=-1
  if ay>1:ay=1
  elif ay<-1:ay=-1
  for i in range(r):
    set_pixel(x+ent(ax*i),y+ent(ay*i),bl)

for i in range(0,361):
#  fill_rect(110,61,100,100,wh)
  fil(160,111,i,160)
#  sleep(0.01)
