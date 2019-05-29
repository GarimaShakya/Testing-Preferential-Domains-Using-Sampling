
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt


#import matplotlib
#matplotlib.rcParams['pdf.fonttype'] = 42
#matplotlib.rcParams['ps.fonttype'] = 42

### open the data file and loading the data
fWCO = open('thm5_profile2.txt', 'r')
#fWCO = open('thm5_profile2_constant_L_t(5_to_40).txt', 'r')

for line in fWCO.readlines():
    exec(line)
fWCO.close()



plt.figure('Theorem 5')

#fig_size = plt.rcParams["figure.figsize"]
#fig_size[0] = 8
#fig_size[1] = 5.7
#
#plt.rcParams["figure.figsize"] = fig_size
#x=np.arange(0.1, 1.1, 0.1)

x=np.arange(0.05, 0.45, 0.05)
plt.axis([0.02, 0.41, 0.0, 1.02])
for index in xrange(len(e_a)):
    current_e_a = e_a[index]
    print current_e_a
    
    plt.plot(x, y[index],label=r'$\epsilon_a='+str(current_e_a)+'$', linewidth=2)
#    plt.plot(l, y[index],label=r'$\epsilon_v='+str(current_e_v)+'$')


plt.yticks(fontsize=25)
plt.xticks(x,rotation=45,fontsize=25)
plt.xlabel('The normalized value of '+ r'$ \tau $, '+ r'( $\frac{\tau}{t}$ ) ' , fontsize=25)
plt.ylabel(r'$\rho$',fontsize=25) 
#plt.xlabel(r'$\ell$')
plt.grid()
plt.tight_layout() 
plt.legend(loc='lower right',fontsize=25 )
plt.savefig('thm5_profile2_fontsize25_Type3.pdf')

plt.show()

plt.show()
