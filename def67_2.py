def sum67(n):
 
 if len(n)==0:
  return 0
 i=0
 a=[]
 while i<= len(n):
 
  while n[i] != 6:
  
   a.append(n[i])
  
   i+=1
   if i>=(len(n)-1):
	   break
     
  i+=2
  if i>=(len(n)-1):
	   break
    while n[i] !=7:
   i+=1
   if i>=(len(n)-1):
	   break
      
  i+=2
  if i>=(len(n)-1):
	   break
 
  	 
	 
 return sum(a)
