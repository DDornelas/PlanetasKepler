import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation as animation
import math

class Planeta:
	def __init__(self, massT, xt, yt, vxt, vyt):
		self.mt=massT
		self.xt=xt
		self.yt=yt
		self.r=math.sqrt((self.xt**2)+(self.yt**2))
		self.vxt=vxt
		self.vyt=vyt
		self.et=0.5*self.mt*(math.sqrt((self.vxt**2)+(self.vyt**2)))
		
	def accel(self, r, p):
		return -p*(GM/(r**3))
		
	def move(self):
		axt = self.accel(self.r, self.xt)
		self.xt += self.vxt*dt+0.5*axt*dt**2
		self.vxt += axt*dt
		self.r = math.sqrt((self.xt**2)+(self.yt**2))
		ayt = self.accel(self.r, self.yt)
		self.yt += self.vyt*dt+0.5*ayt*dt**2
		self.vyt += ayt*dt
		self.r = math.sqrt((self.xt**2)+(self.yt**2))
		
GM=4*np.pi**2
dt=0.0001

tmax=2
t=np.arange(0, tmax, dt)
xTerra=np.zeros(t.size)
yTerra=np.zeros(t.size)
vxTerra=np.zeros(t.size)
vyTerra=np.zeros(t.size)
rTerra=np.zeros(t.size)
eTerra=np.zeros(t.size)

z=0
exc=[]
v0=[]

while z<1:
	
	p1=Planeta(1, 1, 0, 0, 2*np.pi+z)
	for i in range(t.size):
		p1.move()
		xTerra[i], yTerra[i], vxTerra[i], vyTerra[i], rTerra[i], eTerra[i] = p1.xt, p1.yt, p1.vxt, p1.vyt, p1.r, p1.et
	
	a=(math.sqrt((max(xTerra)**2)+(min(xTerra)**2))/2)
	b=(math.sqrt((max(yTerra)**2)+(min(yTerra)**2))/2)
	exc.append(math.sqrt(1-((b**2)/(a**2))))
	v0.append(z)
	z+=0.1
	
plt.figure(figsize=(6,5), dpi=96)

ax=plt.gca()
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.autoscale()
plt.axes().set_aspect('equal','datalim')

plt.rc('text', usetex=True)
plt.rc('font', **{'sans-serif' : 'Arial', 'family' : 'sans-serif'})
plt.xlabel(r'Excentricidade')
plt.ylabel(r'$Vx_{(0)}(\frac{AU}{Ano})$')

plt.title(r'Excentricidade Terra Sol',fontsize=12)
plt.grid()
plt.plot(v0, exc,'r-', linewidth=1)
plt.savefig("EXC.pdf", dpi=96)
plt.show()
