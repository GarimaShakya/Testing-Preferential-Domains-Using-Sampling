# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 18:01:28 2018

@author: garima
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 11:46:54 2018

@author: garima
"""


import math
import random
#import numpy as np
from itertools import permutations
#import matplotlib.pyplot as plt


profile2 = [0]
n = 10000
m = 5

l=[]


#--- epsilon_v --------------fraction of voters to be deleted 

e_v=[0.3,0.5,0.7,0.9]
print e_v


delta= 0.001


#------------------------storing the number of samples, list L--------------
max_l=[]
for i in range(0,len(e_v)):
    max_l.append(72/(math.pow(1-(e_v[i]), 2)) * math.log(6/delta))


t1=[]
t2=[]
t3=[]
t4=[]


for i in range(0,10):
    x=int(((10*i)+10)*max_l[0]/100)
    if(x>n):
        t1.append(n)
    else:
        t1.append(x)
        
for i in range(0,10):
    x=int(((10*i)+10)*max_l[1]/100)
    if(x>n):
        t2.append(n)
    else:
        t2.append(x)
     
for i in range(0,10):
    x=int(((10*i)+10)*max_l[2]/100)
    if(x>n):
        t3.append(n)
    else:
        t3.append(x)
     
for i in range(0,10):
    x=int(((10*i)+10)*max_l[3]/100)
    if(x>n):
        t4.append(n)
    else:
        t4.append(x)


l.append(t1)
l.append(t2)
l.append(t3)
l.append(t4)
       
print l




match=[]
unmatch=[]


for i in range(0,len(e_v)):
    match.append([0] * 10)
    unmatch.append([0] * 10)

all_profiles=[]  #---------to store 100 profiles





#---------------------------------------------------------tester---------------------------------------------------------
def tester(profile2,l2,threshold1):

    test_profile=[]
    count = [0,0,0,0,0,0]
    
    for i in range(0, l2):
        j = random.choice(range(1,n+1))
        test_profile.append(profile2[j])
        
    for i in range(0, l2):
        if(m==3):
            p=[]
        if(m==5):
            p=['d','e']
        if(m==9):
            p=['d','e','f','g','h','i']
        for ele in p:

            test_t=list((test_profile[i]))
            test_t.remove(ele)
            test_profile[i]=tuple(test_t)

        
    for i in range(0, l2):
        if(test_profile[i]==('a','b','c')):
            count[0] = count[0] + 1
            
        if(test_profile[i]==('a','c','b')):
            count[1] = count[1] + 1

        if(test_profile[i]==('b','a','c')):
            count[2] = count[2] + 1
  
        if(test_profile[i]==('b','c','a')):
            count[3] = count[3] + 1
           
        if(test_profile[i]==('c','a','b')):
            count[4] = count[4] + 1
          
        if(test_profile[i]==('c','b','a')):
            count[5] = count[5] + 1
            
    minimum = min(count)


    if(minimum<=threshold1):
        return 1
    else: 
        return 0


#----------------------------------------------------------tester finished----------------------------------------------


perm = []

if(m==3):
   A=['a','b','c']
   perm = list(permutations(A))
if(m==5):
    A=['a','b','c','d','e']
    perm = list(permutations(A))
if(m==9):
    A=['a','b','c','d','e','f','g','h','i']
    perm = list(permutations(A))
    
for k in range(0,100): #------------------for different profiles

    print k
    profile2 = [0]
    for i in range(1,n+1):
        j = int(random.uniform(0,math.factorial(m)))
        profile2.append(perm[j])
#            print profile2
    all_profiles.append(profile2)
#print all_profiles

   
for r in range(0,len(e_v)):  
    for q in range (0,len(l[r])):#-------------for different values of L-----------
        print l[r][q]
        for k in range(0,100): #---------------for 100 different profiles
            print k
            profile2=all_profiles[k]
            threshold=l[r][q]*(1+e_v[r])/12
            for s in range (0,100): #----------100 times for a profile and a value of L
               
                a= tester(profile2,l[r][q],threshold)
                if(a==profile2[0]):
                    
                    match[r][q] = match[r][q] + 1
                    
                else:    
                    
                    unmatch[r][q] =unmatch[r][q]+1

        if ((float(match[r][q]))/float((k+1)*(s+1))>=0.9990):
            print l[r]
            print str((q+1)*10)+'  percent of  ( '+str(l[r][9])+' )    is enough for ' +str(e_v[r])
#            print '---------------------------------------------------'
            for s in range(q+1,10):
                match[r][s]= 1*(100*100)
            break

  
        
#----------to print the result-----------------------------------            
for r in range (0,len(e_v)):
    for q in range (0,len(l[r])):
        print '%0.2f' % e_v[r], l[r][q], match[r][q],unmatch[r][q]           
            
            
mat1=[]
mat2=[]
mat3=[]             
mat4=[] 


to_normalise=float(100*100)


#.......  normalization-----------------------------------------
for q in range (0,10):
    mat1.append(float(match[0][q])/to_normalise)            
    mat2.append(float(match[1][q])/to_normalise)
    mat3.append(float(match[2][q])/to_normalise) 
    mat4.append(float(match[3][q])/to_normalise)      
            
            
 




           
#print mat1,mat2,mat3,mat4   

   
            
#x=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]

#y_pos = np.arange(len(x))
#y_pos = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]

y=[]

y.append(mat1)
y.append(mat2)
y.append(mat3)
y.append(mat4)

#y1=mat1
#y2=mat2
#y3=mat3
#y4=mat4


f = open('thm1_profile2_normalized.txt','a') 
f.write('l='+str(l)+'\n')
f.write('y='+str(y)+'\n')
f.write('n='+str(n)+'\n')
f.write('delta='+str(delta)+'\n')
f.write('m=' +str(m)+'\n')
f.write('e_v=' +str(e_v)+'\n')

f.close()
#f.write('---------------------------------------------------------'+'\n')
#f.write('(e_v)          (l)           match[e_v][l]        unmatch[e_v][l]'+'\n')
#f.write('---------------------------------------------------------'+'\n')

#for r in range (0,len(e_v)):
#    for q in range (0,len(l[r])):
#        f.write( '(' + str('%0.2f' %  e_v[r] )  + ')  ,  ('+ str( l[r][q]) + ')  ,  (' + str( match[r][q] ) + ')  ,  ('+ str(unmatch[r][q] ) +'\n')          
#            
#
#f.write('--------------------------------'+'\n')
#f.write(str('%0.2f' % e_v[0]) +'     normalised ( number of times tester is correct)  '+str(mat1)+'\n')
#f.write(str('%0.2f' % e_v[1])+'     normalised ( number of times tester is correct)  '+str(mat2)+'\n')
#f.write(str('%0.2f' % e_v[2])+ '     normalised ( number of times tester is correct)  '+str(mat3)+'\n')
#f.write(str('%0.2f' % e_v[3])+'     normalised ( number of times tester is correct)  '+str(mat4)+'\n')  
#f.write('---------------------------------------------------------------------------------------------'+'\n'+'\n'+'\n')

 

#
#
##print(len(x))
##print(len(y3))
#
#
#
#fig = plt.figure()
#ax = fig.add_subplot(1, 1, 1)
#
#plt.axis([0, 1, -0.01, 1.1])
#
#ax.grid(which='both')
#
#
#ax.grid(which='minor', alpha=0.2)
#ax.grid(which='major', alpha=0.5)
#
#ga=str(e_v[0])
#ga1=ga[0:5]
#go=str(e_v[1])
#go1=go[0:5]
#ge=str(e_v[2])
#ge1=ge[0:5]
#
#gi=str(e_v[3])
#gi1=gi[0:5]
#
#
#
#
#
#plt.plot(x, y1, color='red',linestyle='-',label='e_v='+ga1)
##plt.plot(x, y2, color='blue',linestyle='-',label ='e_v='+go1)
##plt.plot(x, y3, 'm-',label ='e_v='+ge1)
##plt.plot(x, y4,'c-',label ='e_v='+gi1)
#
#
#plt.xlabel('#profiles='+ str(100) + ',class=2 , for each profile, each value of L is experimented 100 times,',fontsize=10)
#plt.ylabel('probability of correctness of the tester',fontsize=10)
#
#plt.title('delta='+str(delta)+',n='+str(n)+'            ',fontsize=10)
#plt.legend(loc='best')
#
#
#plt.xticks(y_pos,x, rotation=90,fontsize=8)
#
#
#
#plt.grid(True,which="both",ls=":")
#
#
#
#plt.rcParams['figure.figsize']=(18,6)
#
#plt.savefig('theorem1_profile2_new(0.9)'+'.pdf')
#plt.show()
            





            
            
            
            
            
            