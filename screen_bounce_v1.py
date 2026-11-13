#Cree le 23 Decembre 2023
from math import cos,sin,ceil,floor,radians
from kandinsky import set_pixel,fill_rect
from time import sleep
from random import randint

def ent(n):
  if n-floor(n)<0.5:n=floor(n)
  else:n=ceil(n)
  return int(n)
def rebond(ri,si):
  def nearer(ri,n1,n2):
    if n1>=n2:b,c=n1,n2
    else:b,c=n2,n1
    m=(b+c)/2
    if ri>=m+180:ri-=180
    elif ri<=m-180:ri+=180
    r=b if ri>=m else c
    return r
  n1,n2=si-90,si+90
  n1=n1+360 if n1<0 else n1-360 if n1>359 else n1
  n2=n2+360 if n2<0 else n2-360 if n2>359 else n2
  n=nearer(ri,n1,n2)
  ar=n+(n-ri) if n>=ri else n-(ri-n)
  ar=ar-360 if ar>359 else ar+360 if ar<0 else ar
  return ar

lhx,lbx,lhy,lby=320,0,222,0
lhx,lhy=lhx-1,lhy-1
bl,wh=(0,0,0),(255,255,255)

def fil(x,y,a,n):
  global xd,yd,ad,i
  an=radians(a)
  px,py=cos(an),sin(an)
  if a==0:ax,ay=px,py
  elif a<90:ax,ay=px/py,py/px
  elif a==90:ax,ay=px/py,py
  elif a<=180:ax,ay=px/py,py/-px
  elif a<=270:ax,ay=px/-py,py/-px
  elif a<=360:ax,ay=px/-py,py/px
  if ax>1:ax=1
  elif ax<-1:ax=-1
  if ay>1:ay=1
  elif ay<-1:ay=-1
  set_pixel(x+ent(ax*n),y+ent(ay*n),bl)
  nxd,nyd=x+ent(ax*(n+1)),y+ent(ay*(n+1))
  if nxd<lbx or nxd>lhx or nyd<lby or nyd>lhy:
    xd,yd,i=x+ent(ax*n),y+ent(ay*n),0
    if nyd<lby or nyd>lhy:ad=360-a
    if nxd<lbx or nxd>lhx:
      if a<180:ad=180-a
      else:ad=360-(a-180)

xd,yd,ad,i=(lhx-lbx)//2,(lhy-lby)//2,randint(0,360),0
print(ad)
#ad=
#100,60,19,13,225
while True:
  fil(xd,yd,ad,i)
  i+=1
#  sleep(0.01)
