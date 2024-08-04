def e(p,b):
   u=p
   m=1
   for xs in range(u):
        z=""
        character_string="#"
        u=u-1
        for aw in range(u+b):

            z=z+character_string

        for ds in range(m):

            z=z+"*"

        m=m+2

        print(z)
   #Now m=p*2+1.
   m=m-2

    
   bg=p-2 #bg=p-2 it means empty the extra asterisk after the second triangle.    
   vb=b
   #cd equal first line of the second triangle.
   cd=m-2
   for nh in range(cd-bg):        
        m=""
        vb=vb+1
        for dj in range(vb):
            m=m+character_string
        for bt in range(cd):
            m=m+"*"
        cd=cd-2
        print(m)


e(3,0)
