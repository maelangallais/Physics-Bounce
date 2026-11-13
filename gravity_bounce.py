#Créé le 14 Mai 2024
from math import cos,sin,radians,floor,pi,sqrt,fabs
from kandinsky import fill_rect as fr,get_pixel as gp,draw_string as ds
from time import sleep as sl,monotonic as mn

w,h=320,222
n,wh=(0,)*3,(255,)*3
ent=lambda n:floor(n)if n-floor(n)<0.5 else floor(n)+1
c,s=lambda x:cos(radians(x)),lambda x:sin(radians(x))

def draw(xp,yp,X,Y,Sz):
 for i in range(2):
  cx,cy,c=ent(X-Sz)if i else ent(xp-Sz),ent(Y-Sz)if i else ent(yp-Sz),n if i else wh
  for a in range(len(rond)):
   for b in range(len(rond[a])):
    if rond[a][b]==1:fr(cx+b,cy+a,1,1,c)
  if i==0:
   buffer.append([cx,cy])
   if len(buffer)>=15:
    fr(buffer[0][0],buffer[0][1],1,1,(255,0,0))
    buffer.remove([buffer[0][0],buffer[0][1]])
def ce(Ag,si,Ms,Gv):
 e=0.8 if si==0 else 0.66 if si==1 else 0.75
 fc=c if si==0 else s
 e=max(0,min(e*(1-Ms*Gv/1000),1))
 e=e+(1-e)*fabs(fc(Ag))
 return e
def cr(X,Y,Sz,Ag,Ms,Gv):
 global dx,dy,Em,dh
 if not Sz<Y<h-Sz:
  na=360-Ag
  dy=-dy
  e=ce(Ag,1 if Ag<180 else 2,Ms,Gv)
  Em*=e
  if Ag<180:dh=dy/(Em/Ms/Gv)
 if not Sz<X<w-Sz:
  if Ag<180:na=180-Ag
  else:na=360-(Ag-180)
  dx=-dx
  e=ce(Ag,0,Ms,Gv)
  Em*=e
 Ag=na
 return Ag

def simulation(X,Y,Sz,Ag,Sp,Gv,Ms):
 global dy
 game=True
 while game:
  xp,yp=X,Y
  X,Y=X+dx*Sp/50,Y+dy*Sp/50
  draw(xp,yp,X,Y,Sz)
  nx,ny=X+dx,Y+dy
  Sp=sqrt((Em-Ms*Gv*(222-Y))*2/Ms)if (Em-Ms*Gv*(222-Y))*2/Ms>=0 else Sp
  if not Sz<nx<w-Sz or not Sz<ny<h-Sz:Ag=cr(nx,ny,Sz,Ag,Ms,Gv)
  if Em/Ms/Gv<1:
   ds(str(round(mn()-tm,2)),0,0)
   break
  dy-=dh
  sl(0.001)

def start(X=320,Y=30,Sz=3,Ag=225,Sp=100,Gv=9.81,Ms=10):
 global dx,dy,rond,Em,dh,buffer,tm
 buffer,tm=[],mn()
 X,Y=min(max(X,Sz),w-Sz-1),min(max(Y,Sz),h-Sz)
 if Sz>57:Sz=57
 px,py=c(Ag),s(Ag)
 dx=min(max(px if Ag==0 else px/py if Ag<=180 else px/-py,-1),1)
 dy=min(max(py if Ag in[0,90]else py/-px if 90<Ag<=270 else py/px,-1),1)
# dx,dy=px,py
 Em=Ms*Gv*(222-Y)+0.5*Ms*Sp**2
 dh=dy/(Em/Ms/Gv)
 for i in range(16*Sz*pi):
  cx,o=160+cos(i)*Sz,sin(i)*Sz
  cy=111+o
  fr(ent(cx),ent(cy),1,-2*ent(o),n)
 rond=[[0]*(Sz*2+1) for i in range(Sz*2)]
 for a in range(len(rond)):
  for b in range(len(rond[a])):
   if gp(160-Sz+b,111-Sz+a)==n:rond[a][b]=1
 fr(0,0,320,222,wh)
 simulation(X,Y,Sz,Ag,Sp,Gv,Ms)

start()
