import time
def pwb(x,initial,tail,head,up,down):
  print(" ")
  #the top
  hu="*"
  for cv in range(x+1):
       hu=hu+"*"
  print
  
    
  #blank on snake body.
  for po in range(1,up):
      hu="*"
      for vf in range(1,x+1):
          if vf>=1 and vf<=x:
               hu=hu+" "
      hu=hu+"*"
  #if the head position is out of bounds
  #it will print an error otherwise it will
  #print normolly.
  if head<=0 or head>=x:
     return 12345 
  else:
       print(hu)              
   

  for ptr in range(2):
    #The first part of the snake.
    hu="*"
    #The second part of the snake.
    for hg in range(1,tail):
        
        if hg>=1 and hg<=tail-1:
               hu=hu+" "
    hu=hu+"*"
    
    #The third part of the snake.      
    for kl in range(tail,head):
          
         if kl>=tail and kl<=head-1:
              hu=hu+"*"
    
                  
    #The fourth part of the snake.
    for hb in range(head,x):
        if hb>=head and hb<=x-1:
                hu=hu+" "
    #The fifth part of the snake.
    hu=hu+"*"
    
   
   
    #if the head position is out of bounds
    #it will print an error otherwise it will
    #print normolly.
    if head<=0 or head>=x:
       return 12345 
    else:
       print(hu)              
    
  #part two asterisk   
  for po in range(3,x-1):
      hu="*"
      for vf in range(1,x+1):
          if vf>=1 and vf<=x:
               hu=hu+" "
        
      hu=hu+"*"
      print(hu)     
              
  #part three bottom	      
  for ws in range(x):  
       hu="*"    
       for pm in range(1,x+1):
            if pm>=2 and pm<=x:
              hu=hu+"*"
       hu=hu+"**"
  print(hu)  

import time
def fbi():
    sx=0
    yh=0
    for nv in range(20):
       time.sleep(1)

       ass=pwb(20,3,1+sx,6+yh,0+sx,1+sx)
       if ass==12345:
           sx=0 
           yh=0 
              
       yh=yh+2 
       sx=sx+1
       
fbi()
