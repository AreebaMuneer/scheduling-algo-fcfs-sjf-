

import operator
from array import *
from operator import sub
def board():
	print("     ------------- FCFS ----------    ")
	n=int(raw_input("   Enter total no. of processes")) 
	print("")
	p=[]
	wt=[]
	tat=[]
	i=0
	j=0
	total=0
	pos=0
	temp=0
	burst=[]
	a=1
	while (i!=n ):		
		at=int(raw_input('Arrival Time'))
		bt=int(raw_input('enter process burst time'))
		burst.append(bt)
		p.append(i)
		i=i+1
	while (j!= n ):
		pos=j
		k=j+1
		while k!=n :
			if( burst[k] < burst[pos]):
				pos=k
			k=k+1
			

		temp=burst[j]
		burst[j]=burst[pos]
		burst[pos]=temp

		temp=p[j]
		p[j]=p[pos]
		p[pos]=temp
		j=j+1
	l=1   
	m=0	
	while l!=n :
		total.append(sum(burst))
		l=l+1


board()
	