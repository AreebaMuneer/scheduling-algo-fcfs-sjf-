

import operator
from array import *
from operator import sub
def board():
	print("     ------------- FCFS ----------    ")
	n=int(raw_input("   Enter total no. of processes"))   
	print("")
	i=0
	lst=[]
	lst2=[]
	burst=[]
	at=[]
	Tat=[]
	for i in range (n):
		at=int(raw_input('Arrival Time'))
		bt=int(raw_input('enter process burst time'))
		burst.append(bt)
		lst2.append(at)
		lst.append(sum(burst)) # Complition time
		Tat = map(sub, lst, lst2) # Turn around time= Complition - arrival time
		print("")
		
		if(i==n-1):
			print(' Turn around time: ', Tat)
			print(' Waiting Time: ',  map(sub, Tat, burst)) # Waiting time = Turn around - Burst time
		
	
board()
	