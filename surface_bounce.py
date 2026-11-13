#Créé le 22 Octobre 2026

from math import fabs as va,floor,ceil,cos as C,sin as S,atan2,pi,radians,degrees
from kandinsky import fill_rect as fr,set_pixel as sp,get_pixel as gp
from random import randint as rd
from time import sleep as sl

n=(0,)*3
#ent=lambda n:floor(n)if n-floor(n)<0.5 else floor(n)+1
ent=lambda n:round(n)
add, sub=lambda a,b:a+b, lambda a,b:a-b

lhx,lbx,lhy,lby=320,0,222,0
lhx,lhy=lhx-1,lhy-1

#algorithme draw_line amélioré pour la 8-connectivité
def dl(x1,y1,x2,y2,t=1):
 w=h=1
 dx=min(max((x2-x1)/va(y2-y1)if va(y2-y1)!=0 else x2-x1,-1),1)
 dy=min(max((y2-y1)/va(x2-x1)if va(x2-x1)!=0 else y2-y1,-1),1)
 c=va(x2-x1)if va(x2-x1)>va(y2-y1)else va(y2-y1)
 if va(dx)<va(dy):w,x1,x2=t,x1-(t-1)//2,x2-(t-1)//2
 else:h,y1,y2=t,y1-(t-1)//2,y2-(t-1)//2
 px,py=x1,y1
 hb=not rd(0,1)
 for i in range(c):
  nx,ny=x1+dx*i,y1+dy*i
  fr(ent(nx),ent(ny),w,h,n)
  if t==1:
   if nx!=px and ny!=py:
    if hb:fr(ent(px),ent(ny),w,h,n)
    else:fr(ent(nx),ent(py),w,h,n)
   px,py=nx,ny

def d(x,y,r,a=0,c=0,d=1):
  s=ceil(2*pi*r)
  st=s//2 if d else s
  ai=radians(a)
  op=add if c else sub
  for i in range(st):
    ag=op(ai,i/s*2*pi)
    xp=x+r*C(ag)
    yp=y-r*S(ag)
    if not d:
     sp(ent(xp),ent(yp),n)
     continue
    if gp(ent(xp),ent(yp))==n:
      return (xp,yp)
    #sp(ent(xp),ent(yp),(0,0,255))
    #sl(0.01)
  return None

class Rayon:
 c=(255,0,0)
 def __init__(s,x,y,a):
  s.x=x
  s.y=y
  s.sa(a)
 def m(s): #move
  s.x+=s.vx
  s.y+=s.vy
 def d(s): #draw
  sp(ent(s.x),ent(s.y),s.c)
 def sa(s,a): #set angle
  s.a=a%360
  a=radians(a)
  s.vx=C(a)
  s.vy=-S(a)
 def f(s): #forecast
  ix,iy=ent(s.x+s.vx),ent(s.y+s.vy)
  if ix<lbx or ix>lhx or iy<lby or iy>lhy:
   na=s.a
   if iy<lby or iy>lhy:na=360-na
   elif ix<lbx or ix>lhx:na=180-na
   s.sa(na)
  elif gp(ix,iy)==n:
   s.c=(rd(10,200), rd(10,200),rd(10,200))
   ta=(s.a+180)%360
   p1=d(ix,iy,6,ta,0)
   p2=d(ix,iy,6,ta,1)
   if not p1 and not p2:
    na=(s.a+180)%360
   elif not p1 or not p2:
    p=p1 if p1 else p2
    wd=(degrees(atan2(p[1]-iy,p[0]-ix))+360)%360
    df=abs((s.a-wd+180)%360-180)
    if df>135:
     wa=(wd+90)%360
     na=(2*wa-s.a)%360
    else:
     nl=(degrees(atan2(s.y-iy,s.x-ix))+360)%360
     na=(2*nl-s.a+180)%360
   else:
    x1,y1=p1
    x2,y2=p2
    wa=(degrees(atan2(-(y2-y1),x2-x1))+360)%360
    na=(2*wa-s.a)%360
   s.sa(na)
 def u(s): #update
  s.m()
  s.f()
  s.d()

for _ in range(3):
 dl(rd(20,300),rd(20,202),rd(20,300),rd(20,202),3)
for i in range(5):
 d(160,111,100-i*0.5,0,0,0)

r=Rayon(rd(60,260),rd(11,211),rd(0,360))
#r=Rayon(rd(125,130),111,rd(265,275))
while True:
  r.u()
  #sl(0.001)
