
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt


#for type 1 fonts uncomment the below 3 lines ---------------
#import matplotlib
#matplotlib.rcParams['pdf.fonttype'] = 42
#matplotlib.rcParams['ps.fonttype'] = 42
#-------------------------
### open the data file and loading the data

fWCO = open('thm2_profile2_normalized.txt', 'r')
for line in fWCO.readlines():
    exec(line)
fWCO.close()



plt.figure('Theorem 1')
x=[0.02,0.05, 0.1, 0.15,0.2, 0.25, 0.3, 0.35,0.4, 0.45, 0.5, 0.55, 0.6]
plt.axis([0.0, 0.6, 0.0, 1.05])
for index in xrange(len(e_v)):
    current_e_v = e_v[index]
    print current_e_v
    
    plt.plot(x, y[index],label=r'$\epsilon_v='+str(current_e_v)+'$',linewidth=2.0)
#    plt.plot(l, y[index],label=r'$\epsilon_v='+str(current_e_v)+'$')



plt.yticks(fontsize=25)
plt.xticks(x,rotation=45,fontsize=25)
plt.ylabel(r'$\rho$',fontsize=25)
plt.xlabel('The normalized value of ' + r'$l,(\frac{l}{\ell})$',fontsize=25)
plt.grid()
plt.tight_layout() 
plt.legend(loc='best',fontsize=25)
plt.savefig('thm2_profile2_normalized_fontsize25_type3.pdf')
plt.show()
