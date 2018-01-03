s = [1,2,3,4,5,6,7,8,9]

def board():
	print("     ------------- TIC TAC  TOE ----------    ")
	print("     plyaer-1 (x)   and      player-2(0)    ")
	print(" ")
	print("")
	print( "       |            |        " )
#	print "   " ,"-------------------------" 

	print  "    " , s[0]   , "|" ,"     " ,     s[1]  ,  "   |"  ,   s[2]	
	print "   " ,"-------------------------" 
	
	print("")
	print  "    " , s[3]   , "|" ,"     " ,     s[4]  ,  "   |"  ,   s[5]	
	print "   " ,"-------------------------" 
	
	print("")
	print  "    " , s[6]   , "|" ,"     " ,     s[7]  ,  "   |"  ,   s[8]	
def  isvectory():
	count=0
	if(s[0]==s[1] and s[1]==s[2]):
	   s[0]=s[1]=s[2]='-'
	   count=count+1
	   return 1
	elif(s[3]==s[4] and s[4]==s[5]):
	   s[3]=s[4]=s[5]='-'
	   count=count+1
	   return 1
	elif(s[6]==s[7] and s[7]==s[8]):
	   s[6]=s[7]=s[8]='-'
	   count=count+1
	   return 1
	elif(s[0]==s[3] and s[3]==s[6]):
	   s[0]=s[3]=s[6]='|'
	   count=count+1
	   return 1
	elif(s[1]==s[4] and s[4]==s[7]):
	   s[1]=s[4]=s[7]='|'
	   count=count+1
	   return 1
	elif(s[2]==s[5] and s[5]==s[8]):
	   s[2]=s[5]=s[8]='|'
	   count=count+1
	   return 1
	elif(s[0]==s[4] and s[4]==s[8]):
	   s[0]=s[4]=s[8]='*'
	   count=count+1
	   return 1
	elif(s[2]==s[4] and s[4]==s[6]):
	   s[2]=s[4]=s[6]='/'
	   count=count+1
	   return 1
	elif(s[0]!=1 and s[1]!=2 and s[2]!=3 and  s[3]!=4 and s[4]!=5 and s[5]!=6 and s[6]!=7 and s[7]!=8 and s[8]!=9):
		count=count+1
		return 2
	else:
		return 0
		
		
def game():	   
	player=1
	i=0	
	w=0
	while i!=1 or i!=2 :
		board()	
		if( player%2 ):
			player=1
		else:	
			player=2
		if(player == 1):
			m ='x'
		else:	
			m ='O'
		print "player-",player 
		choice = raw_input("   Enter a number")   
		if choice == '1'   :
			s[0] = m
			i=isvectory()
		elif choice == '2' :
			s[1] = m
			i=isvectory()
		elif choice == '3' :
			s[2] = m
			i=isvectory()
		elif choice == '4' :
			s[3] = m
			i=isvectory()
		elif choice == '5' :
			s[4] = m
			i=isvectory()
		elif choice == '6' :
			s[5] = m
			i=isvectory()
		elif choice == '7' :
			s[6] = m
			i=isvectory()
			print i
		elif choice == '8' :
			s[7] = m
			i=isvectory()
			print i
		elif choice == '9':
			s[8] = m
			i=isvectory()
		else: 
			print"   invalid move "
			player = player-1
		player=player+1
		
		

	
		board()		
		if(i==1 ): 
			player=player-1
			print "player " , player , "  Win "
			break			
                  			
		elif(i==2 ):
			print "       Game is Draw   "
			break
		
		
	
	
	
game()