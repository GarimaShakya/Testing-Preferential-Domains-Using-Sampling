# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 11:46:54 2018

@author: garima
"""


import math
import random
import numpy as np
from itertools import permutations


profile2 = [0]
n = 10000
m = 11

l=[]


 #--- epsilon_v --------------fraction of voters to be deleted 

e_a=[0.3,0.5,0.7]


delta= 0.001




l=[]

max_l=[]

for i in range(0,len(e_a)):
    c=[]
    a=(1-e_a[i])*m

    b=2*math.log((1/delta),(1/e_a[i]))
    c.append(a)
    c.append(b)
    max_l.append(int(min(c)))

#print max_l

all_profiles=[]


l=max_l
print l


#-------------------------------------the varible k is for varible t in the algorithm

k=[]
max_k=[]

for i in range(0,len(e_a)):

    a=2*math.log((1/delta),(1/e_a[i]))
    b= a/delta
    c=18*math.log(b)

    max_k.append(c)


k=[]

t1=[]
t2=[]
t3=[]


for i in range(1,9):
    x=int((5*i)*max_k[0]/100)
    t1.append(x)

#        
for i in range(1,9):
    x=int((5*i)*max_k[1]/100)
    t2.append(x)
     
for i in range(1,9):
    x=int((5*i)*max_k[2]/100) 
    t3.append(x)


k.append(t1)
k.append(t2)
k.append(t3)

        
print k




match =[]
unmatch=[]

for i in range(0,len(e_a)):
    match.append([0 ] *10)
    unmatch.append([0] *10)
    
print match, unmatch


#---------------------------------------------------------tester---------------------------------------------------------
def tester(profile2,l2,k2):
    Q=[]
    B=[]
    count = [0,0,0,0,0,0]
    A=list(range(1, m+1))

              
    B = np.random.choice(A,l2,replace=False)
#    print B
    a=B[0]
    b=B[1]
    c=B[2]
#    print B
    for i in range(0,k2):
        j= np.random.choice(range(1,len(profile2)))
        Q.append(profile2[j])
#    print Q

        
    p=list(set(A)-set(B))
    
    for i in range(0, len(Q)): 
        for ele in p:
            test_t=list(Q[i])
            test_t.remove(ele)
            Q[i]=tuple(test_t)
            
#    print 'restricted Q'
#    print Q
    p=list(set(B)-{a,b,c})
    for i in range(0, len(Q)): 
        for ele in p:
            test_t=list(Q[i])
            test_t.remove(ele)
            Q[i]=tuple(test_t) 
#    print Q
    for i in range(0, k2):
        if(Q[i]==(a,b,c)):
            count[0] = count[0] + 1
            
        if(Q[i]==(a,c,b)):
            count[1] = count[1] + 1

        if(Q[i]==(b,a,c)):
            count[2] = count[2] + 1
  
        if(Q[i]==(b,c,a)):
            count[3] = count[3] + 1
           
        if(Q[i]==(c,a,b)):
            count[4] = count[4] + 1
          
        if(Q[i]==(c,b,a)):
            count[5] = count[5] + 1
    print count        
    minimum = min(count)
    print 'minimum='+str(minimum)

    if(minimum==0):
        return 1
    else: 
        return 0
##---------------------------------------------------------tester completed---------------------------------------------------------



perm = []


A=list(range(1, m+1))
perm = list(permutations(A))




#--------------------to generate n preferences randomly----------------------------   
for i in range(0,100): #------------------for different profiles

#    print i
    profile2 = [0]
    for i in range(1,n+1):
        j = int(random.uniform(0,math.factorial(m)))
        profile2.append(perm[j])
#            print profile2
    all_profiles.append(profile2)
    
#print all_profiles
#
  
for p in range(0,len(e_a)):  
#    for q in range (0,len(l[p])):#-------------for different values of L-----------
    for r in range (0,len(k[p])):
        print 'r is :' + str(r)        
        for s in range(0,len(all_profiles)):
            profile2=all_profiles[0]
            print e_a[p]
            
#                                                       for s in range (0,100): #----------100 times for a profile and a  value of L
            print l[p],k[p][r]
            for itr in range(0,100):
                print '['+str(p)+']['+str(l[p])+']['+str(r)+']['+str(s)+']['+str(itr)+']'
                a=tester(profile2,l[p],k[p][r])
        
                if(a==0):              
                    match[p][r] = match[p][r] + 1
                else:    
                    unmatch[p][r] = unmatch[p][r]+1
        match[p][r] = float(match[p][r])/float(len(all_profiles)*100)
        unmatch[p][r] = float(unmatch[p][r])/float(len(all_profiles)*100)
            
print match
print unmatch




f = open('thm5_profile2_constant_L_t(5_to_40)(m=5).txt','w') 
f.write('l='+str(l)+'\n')
f.write('k='+str(k)+'\n')
f.write('y='+str(match)+'\n')
f.write('n='+str(n)+'\n')
f.write('delta='+str(delta)+'\n')
f.write('m=' +str(m)+'\n')
f.write('e_a=' +str(e_a)+'\n')

f.close()  
            
