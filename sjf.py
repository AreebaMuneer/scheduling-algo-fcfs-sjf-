                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         

import operator
from array import *
from operator import sub
def board():
	print("     ------------- SJF ----------    ")
	n=int(raw_input("   Enter total no. of processes")) 
	print("")
	p=[]
	wt=[]
	tat=[]
	i=0
	j=0
	total=[]
	pos=0
	temp=0
	burst=[]
	a=1
	while (i!=n ):		
		at=int(raw_input('Arrival Time'))
		bt=int(raw_input('enter process burst time'))
		burst.append(bt)
		p.insert(i,i+1)
		i=i+1
	while (j!= n ):
		pos=j
		k=j+1
		while k!=n :
			if( burst[k] < burst[pos]):
				pos=k
			k=k+1
		if(j==0):
			temp=burst[j+1]
			burst[j+1]=burst[pos]
			burst[pos]=temp

			temp=p[j+1]
			p[j+1]=p[pos]
			p[pos]=temp
			
		temp=burst[j]
		burst[j]=burst[pos]
		burst[pos]=temp
		temp=p[j]
		p[j]=p[pos]
		p[pos]=temp
	
		j=j+1
	burst.insert(0,0)	
	l=1   
	m=0	
	tot=[]
	
	while l!=n+1 :
		print(burst)
		total.append((burst[l-1]+burst[l]))
		l=l+1
	print(total)

board()
	