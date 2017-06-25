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
M=1.9*10**30
GM=4*np.pi**2
dt=0.0002

p1=Planeta(1, 1, 0, 0, 2*np.pi)
p2=Planeta(1, 2, 0, 0, 2.7576)

tmax=6.4
t=np.arange(0, tmax, dt)
xT=np.zeros(t.size)
yT=np.zeros(t.size)
vxT=np.zeros(t.size)
vyT=np.zeros(t.size)
xOP=np.zeros(t.size)
yOP=np.zeros(t.size)
vxOP=np.zeros(t.size)
vyOP=np.zeros(t.size)

for i in range(t.size):
	axt = -p1.xt*(GM/(p1.r**2))-(p1.xt-p2.xt)*((G*p2.mt)/((math.sqrt(((p1.xt-p2.xt)**2)+((p1.yt-p2.yt)**2)))**3))
	p1.xt += p1.vxt*dt+0.5*axt*dt**2
	p1.vxt += axt*dt
	p1.r=math.sqrt((p1.xt**2)+(p1.yt**2))
	ayt = -p1.yt*(GM/(p1.r**2))-(p1.yt-p2.yt)*((G*p1.mt)/((math.sqrt(((p1.xt-p2.xt)**2)+((p1.yt-p2.yt)**2)))**3))
	p1.yt += p1.vyt*dt+0.5*ayt*dt**2
	p1.vyt += ayt*dt
	p1.r=math.sqrt((p1.xt**2)+(p1.yt**2))
	
	axt = -p2.xt*(GM/(p2.r**2))-(p2.xt-p1.xt)*((G*p1.mt)/((math.sqrt(((p1.xt-p2.xt)**2)+((p1.yt-p2.yt)**2)))**3))
	p2.xt += p2.vxt*dt+0.5*axt*dt**2
	p2.vxt += axt*dt
	p2.r=math.sqrt((p2.xt**2)+(p2.yt**2))
	ayt = -p2.yt*(GM/(p2.r**2))-(p2.yt-p1.yt)*((G*p1.mt)/((math.sqrt(((p1.xt-p2.xt)**2)+((p1.yt-p2.yt)**2)))**3))
	p2.yt += p2.vyt*dt+0.5*ayt*dt**2
	p2.vyt += ayt*dt
	p2.r=math.sqrt((p2.xt**2)+(p2.yt**2))
	
	xT[i], yT[i], vxT[i], vyT[i], xOP[i], yOP[i], vxOP[i], vyOP[i] = p1.xt, p1.yt, p1.vxt, p1.vyt, p2.xt, p2.yt, p2.vxt, p2.vyt
	

fig = plt.figure()
plt.title('Dois Planetas e Uma Estrela ao Centro', fontsize=14)

plt.xticks(np.linspace(-3, 3, 2,endpoint=True))
plt.yticks(np.linspace(-3, 3, 2, endpoint=True))
P1=fig.add_subplot(111, xlim=(-3, 3), ylim=(-3, 3))
plt.xlabel('$X_{(t)}$(AU)')
plt.ylabel('$Y_{(t)}$(AU)')
plt.grid()
line1, = P1.plot([], [], 'r-', lw=1)

P2=fig.add_subplot(111, xlim=(-3, 3), ylim=(-3, 3))
line2, = P2.plot([], [], 'b-', lw=1)

def init():
	line1.set_data([],[])
	line2.set_data([],[])
	return line1, line2,
	
def animate(i):
	x=xT[:i]
	y=yT[:i]
	z=xOP[:i]
	t=yOP[:i]
	line1.set_data(x, y)
	line2.set_data(z, t)
	return line1, line2,
		
anim=animation.FuncAnimation(fig, animate, init_func=init, frames=64000,
interval=0, blit=True)

anim.save('PR2.mp4', fps=200)

plt.show()
