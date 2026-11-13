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

def fil(x,y,a,n,dx,dy,i):
  cx,cy=x+ent(dx*n),y+ent(dy*n)
  set_pixel(cx,cy,bl)
  nx,ny=cx+dx,cy+dy
  if not lbx<nx<lhx or not lby<ny<lhy:
    if not lbx<nx<lhx:ad=rebond(a,0)
    if not lby<ny<lhy:ad=rebond(a,90)
    x,y,a,n=cx,cy,ad,0
    dx,dy=cos(radians(ad)),-sin(radians(ad))
    al[i][0],al[i][1],al[i][2],al[i][3],al[i][4],al[i][5]=x,y,a,n,dx,dy

al,nb=[],20 #372 max
for i in range(nb):
  xd,yd,ad=(lhx-lbx)//2,(lhy-lby)//2,randint(0,360)
  dx,dy=cos(radians(ad)),-sin(radians(ad))
  al.append([xd,yd,ad,0,dx,dy,i])
#100,60,19,13,225
while True:
  for x,y,a,n,dx,dy,i in al:
    fil(x,y,a,n,dx,dy,i)
    al[i][3]+=1
  sleep(0.01)
