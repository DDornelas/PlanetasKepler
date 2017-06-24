import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation as animation
import math

class Planeta:
	def __init__(self, massT, xt, yt, vxt, vyt):
		self.mt=massT
		self.xt=xt
		self.yt=yt
		self.r1=math.sqrt(((-1-self.xt)**2)+(self.yt**2))
		self.r2=math.sqrt(((1-self.xt)**2)+(self.yt**2))
		self.vxt=vxt
		self.vyt=vyt
		self.et=0.5*self.mt*(math.sqrt((self.vxt**2)+(self.vyt**2)))
		
	def accel(self, r1, r2, p):
		return -p*(GM/(r1**3))-p*(GM/(r2**3))
		
	def move(self):
		axt = self.accel(self.r1, self.r2, self.xt)
		self.xt += self.vxt*dt+0.5*axt*dt**2
		self.vxt += axt*dt
		self.r1=math.sqrt(((-1-self.xt)**2)+(self.yt**2))
		self.r2=math.sqrt(((1-self.xt)**2)+(self.yt**2))
		ayt = self.accel(self.r1, self.r2, self.yt)
		self.yt += self.vyt*dt+0.5*ayt*dt**2
		self.vyt += ayt*dt
		self.r1=math.sqrt(((-1-self.xt)**2)+(self.yt**2))
		self.r2=math.sqrt(((1-self.xt)**2)+(self.yt**2))
		
GM=4*np.pi**2
dt=0.0001

p1=Planeta(1, 0.1, 1, 0, -np.pi/2)

tmax=10
t=np.arange(0, tmax, dt)
xTerra=np.zeros(t.size)
yTerra=np.zeros(t.size)
vxTerra=np.zeros(t.size)
vyTerra=np.zeros(t.size)
rTerra=np.zeros(t.size)
eTerra=np.zeros(t.size)

for i in range(t.size):
	p1.move()
	xTerra[i], yTerra[i], vxTerra[i], vyTerra[i], eTerra[i] = p1.xt, p1.yt, p1.vxt, p1.vyt, p1.et
	
	
plt.figure(figsize=(6,5), dpi=96)
plt.axis([-2,2,-2,2])

ax=plt.gca()
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.autoscale()
#plt.axes().set_aspect('equal','datalim')

plt.rc('text', usetex=True)
plt.rc('font', **{'sans-serif' : 'Arial', 'family' : 'sans-serif'})
plt.xlabel(r'$X_{(t)}$(AU)')
plt.ylabel(r'$Y_{(t)}$(AU)')

plt.title(r'Posi\c{c}\~{a}o Planeta e Duas Estrelas Velocidade Inicial $\frac{\pi}{2}$',fontsize=12)
plt.grid()
plt.plot(xTerra, yTerra,'r-', linewidth=1)
plt.savefig("TC4.pdf", dpi=96)
plt.show()
