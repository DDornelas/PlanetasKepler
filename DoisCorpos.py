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
		
G=6.67*10**(-11)
GM=4*np.pi**2
dt=0.0001

p1=Planeta(1, 1, 0, 0, 2*np.pi+1)

tmax=2
t=np.arange(0, tmax, dt)
xTerra=np.zeros(t.size)
yTerra=np.zeros(t.size)
vxTerra=np.zeros(t.size)
vyTerra=np.zeros(t.size)
rTerra=np.zeros(t.size)
eTerra=np.zeros(t.size)

for i in range(t.size):
	p1.move()
	xTerra[i], yTerra[i], vxTerra[i], vyTerra[i], rTerra[i], eTerra[i] = p1.xt, p1.yt, p1.vxt, p1.vyt, p1.r, p1.et
	
plt.figure(figsize=(6,5), dpi=96)

ax=plt.gca()
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.autoscale()
plt.axes().set_aspect('equal','datalim')

plt.rc('text', usetex=True)
plt.rc('font', **{'sans-serif' : 'Arial', 'family' : 'sans-serif'})
plt.xlabel(r'$Raio_{(t)}$(m)')
plt.ylabel(r'$Vx_{(t)}$(m)')

plt.title(r'Espa\c{c}o de Fases Terra Sol Velocidade Inicial 2$\pi$+1',fontsize=12)
plt.grid()
plt.plot(rTerra, vxTerra,'r-', linewidth=1)
plt.savefig("EFR1.pdf", dpi=96)
plt.show()
	

