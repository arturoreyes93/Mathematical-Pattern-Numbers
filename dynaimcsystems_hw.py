def main():

	import math

	m=10
	k=40
	b=4

	wn=(k/m)**(0.5)

	delta=(2*math.pi)/(100*wn)

	p=[0]
	x=[0.2]
	t=[]
	pdot=[-k*0.2]
	xdot=[0]


	for i in range(0,5,delta):

		p.append(p[i]+(pdot[i]*delta))
		x.append(x[i]+(xdot[i]*delta))

		pdot.append(((-b/m)*p[i+1])-k*x[i+1])
		xdot.append(p[i+1]/m)

	print(x)

main()






