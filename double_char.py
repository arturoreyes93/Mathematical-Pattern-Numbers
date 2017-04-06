def xyz_there(s):

    if len(s)<3:

        return False
  
    for i in range(len(s)):

        print(s[i-1])
        print(s[i:i+3])



        if s[i:i+3] == 'xyz' and not(s[i-1]=='.'):


            return True
    
        else:

            return False
   
