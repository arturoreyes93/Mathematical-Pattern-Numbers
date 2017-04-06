# Return the sum of the numbers in the array, except ignore
#sections of numbers starting with a 6 and extending to the next 7
#(every 6 will be followed by at least one 7). Return 0 for no numbers.

def sum67(n):
 
 if len(n)==0:
  return 0
 i=0
 a=[]
 while i<= len(n)-1:
 
  while n[i] != 6:
  
   a.append(n[i])
  
   i+=1
   if i>=(len(n)):
     break
   
   
  i+=1
  if i>=(len(n)):
     break
  
    
  while n[i] !=7:
   i+=1
   if i>=(len(n)):
     break
   
   
  i+=1
  if i>=(len(n)):
     break
  
     
   
 return sum(a)

