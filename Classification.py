import numpy as  np 
data=[[100,0],[110,0],[400,0],[550,1],[570,1],[690,1]]
test=[550]
w1=200
b=100
lr=0.01
def sigmoid(x):
	return 1/(1+np.exp(-x))
def sigmoid_p(x):
	return sigmoid(x)*(1-sigmoid(x))

for i in range(1000000):
		ri=np.random.randint(len(data))
		point=data[ri]
		z=w1*point[0]+b
		pred=sigmoid(z)
		target=point[1]
		cost=np.square(pred-target)
		dcost=2*(pred-target)
		dz=sigmd_p(z)
		doiw1=point[0]
		db=1
		total_deriv=dcost*dw1*db
		w1=w1-lr*total_deriv
		b=b-lr*total_deriv
		#if i%100000==0:
			#print point
			#print pred	
tester=w1*test[0]+b
res=sigmoid(tester)
print res