# guess-the-number

import random

print('Hello! what is your name')
name=input()

print('well,',name,'I am thinking a number between 1 and 20')
secretnum = random . randint (1,20)

for guesstaken in range(1,7):
	print('take a guess')
	guess =int(input())
	
	if guess<secretnum:
		print('your guess is too low')
		
	elif guess>secretnum:
		print('your guess is too high ')
	
	else :
		break #if it is correct
		
if guess == secretnum:
	print ('you find my number in '+str(guesstaken)+'  guess')

else :
	print(' nope, your guess is wrong the correct number is '+str(secretnum))
	
