# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 14:33:53 2018

@author: swaprava

plotting the files for testing domains
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 18:34:07 2016

@author: swaprava

plot the results got from the simulation
"""

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
#
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



'''
budget = 1.0
k = 4 # for the k approval PB Stan

debug = False
fillRest = 'knapsack'
inputFormat = 'Randomly generated values' # 'Value-for-money', 'k-Approval', 'Knapsack', 'Randomly generated values'
fileSuffix = 'randVal' # 'kApp', 'VFM', 'Knap', 'randVal'
kind = ['truncnorm', 1.0]
valThresType = 'reverse' # 'forward', 'reverse'

finalSuffix = fileSuffix + '_' + kind[0] + '_' + str(kind[1])


if fileSuffix == 'randVal':
    titleText = 'Distortion for Voting Rules\n'+'Input format: ' + inputFormat + ', Random type: ' + kind[0] + '_' + str(kind[1]) + ', cost-val pairs: ' +str(costCounts*valCounts)+ ', randRepeatCount: ' + str(randRepeatCount)
else:
    titleText = 'Distortion for Voting Rules\n'+'Input format: ' + inputFormat



plt.figure('Randomized Mechanisms + PB Stan')
plt.title(titleText)

ax = plt.subplot(111)

# RANDOMIZED MECHANISMS

plt.errorbar(numOfAltsList, distRandValueMean, yerr=np.array(distRandValueConf).T, fmt='ko--', linewidth=2, capsize=2,markersize=8, label='Rand Value (filled)')
#plt.errorbar(numOfAltsList, distRandValueMean_WOFilling, yerr=np.array(distRandValueConf_WOFilling).T, capsize=2, label='Rand Value (unfilled)')
#plt.plot(numOfAltsList, 4 * np.sqrt(numOfAltsList) * (np.log2(numOfAltsList) + 1), 'ro-', label='Rand Value, VFM (bound)')

plt.errorbar(numOfAltsList, distRandVFMMean, yerr=np.array(distRandVFMConf).T, fmt='kd-',linewidth=2, capsize=2,markersize=8, label='Rand VFM (filled)')
#plt.errorbar(numOfAltsList, distRandVFMMean_WOFilling, yerr=np.array(distRandVFMConf_WOFilling).T, capsize=2, label='Rand VFM (unfilled)')


plt.errorbar(numOfAltsList, distRandApprovalMean, yerr=np.array(distRandApprovalConf).T, fmt='kv--',linewidth=2, capsize=2,markersize=8, label='Rand Approval (filled)')
#plt.errorbar(numOfAltsList, distRandApprovalMean_WOFilling, yerr=np.array(distRandApprovalConf_WOFilling).T, capsize=2, label='Rand Approval (unfilled)')
#plt.plot(numOfAltsList, 4 * (np.log2(numOfAltsList)**2 + 1), 'ro-', label='Rand Approval (bound)')


plt.errorbar(numOfAltsList, distPBSTANKnapsackMean, yerr=np.array(distPBSTANKnapsackConf).T, fmt='ks-.',linewidth=2, capsize=2,markersize=8, label='PB STAN (knapsack)')

plt.errorbar(numOfAltsList, distPBSTANkApprovalMean, yerr=np.array(distPBSTANkApprovalConf).T, fmt='k^--',linewidth=2, capsize=2,markersize=8, label='PB STAN ('+str(k)+'-appr)')


ax.set_xlim(xmin=min(numOfAltsList)-1, xmax=max(numOfAltsList)+1)
ax.set_ylabel('Distortion', fontsize=15)

ax.set_xlabel(r'Number of Alternatives, $m$', fontsize=15)
#plt.ylabel('Distortion', fontsize=15)
ax.grid()

plt.legend(loc='best')
#plt.grid()




plt.figure('Deterministic WCOs')
ax = plt.subplot(111)
#plt.title('Distortion for Voting Rules')
ax.set_title(titleText)

### DET WCO

plt.errorbar(numOfAltsList, distDetWCOValueMean, yerr=np.array(distDetWCOValueConf).T,  fmt='ko--', linewidth=2, capsize=2,markersize=8, label='Det WCO Value (avg)')
#plt.errorbar(numOfAltsList, distDetWCOValueWorstMean, yerr=np.array(distDetWCOValueWorstConf).T, capsize=2, label='Det WCO Value (worst)')

plt.errorbar(numOfAltsList, distDetWCOVFMMean, yerr=np.array(distDetWCOVFMConf).T, fmt='kd-',linewidth=2, capsize=2,markersize=8, label='Det WCO VFM (avg)')
#plt.errorbar(numOfAltsList, distDetWCOVFMWorstMean, yerr=np.array(distDetWCOVFMWorstConf).T, capsize=2, label='Det WCO VFM (worst)')

plt.errorbar(numOfAltsList, distDetWCOKnapMean, yerr=np.array(distDetWCOKnapConf).T, fmt='kv--',linewidth=2, capsize=2,markersize=8, label='Det WCO Knapsack (avg)')
#plt.errorbar(numOfAltsList, distDetWCOKnapWorstMean, yerr=np.array(distDetWCOKnapWorstConf).T, capsize=2, label='Det WCO Knapsack (worst)')

plt.errorbar(numOfAltsList, distDetWCORandAppMean, yerr=np.array(distDetWCORandAppConf).T, fmt='ks-.',linewidth=2, capsize=2,markersize=8, label='Det WCO RandApp (avg)')
#plt.errorbar(numOfAltsList, distDetWCORandAppWorstMean, yerr=np.array(distDetWCORandAppWorstConf).T, capsize=2, label='Det WCO RandApp (worst)')

#ax.set_yscale('log', nonposy='clip')
ax.set_xlim(xmin=min(numOfAltsList)-1, xmax=max(numOfAltsList)+1)
ax.set_ylabel('Distortion', fontsize=15)

ax.set_xlabel(r'Number of Alternatives, $m$', fontsize=15)
#plt.ylabel('Distortion', fontsize=15)
ax.grid()
plt.legend(loc='best')

### RAND WCO

plt.figure('Randomized WCOs')
ax = plt.subplot(111)
#plt.title('Distortion for Voting Rules')
ax.set_title(titleText)

plt.errorbar(numOfAltsList, distRandWCOValueMean, yerr=np.array(distRandWCOValueConf).T, fmt='ko--', linewidth=2, capsize=2,markersize=8, label='Rand WCO Value (avg)')
#plt.errorbar(numOfAltsList, distRandWCOValueWorstMean, yerr=np.array(distRandWCOValueWorstConf).T, capsize=2, label='Rand WCO Value (worst)')

plt.errorbar(numOfAltsList, distRandWCOVFMMean, yerr=np.array(distRandWCOVFMConf).T, fmt='kd-',linewidth=2, capsize=2,markersize=8, label='Rand WCO VFM (avg)')
#plt.errorbar(numOfAltsList, distRandWCOVFMWorstMean, yerr=np.array(distRandWCOVFMWorstConf).T, capsize=2, label='Rand WCO VFM (worst)')

plt.errorbar(numOfAltsList, distRandWCOKnapMean, yerr=np.array(distRandWCOKnapConf).T, fmt='kv--',linewidth=2, capsize=2,markersize=8, label='Rand WCO Knapsack (avg)')
#plt.errorbar(numOfAltsList, distRandWCOKnapWorstMean, yerr=np.array(distRandWCOKnapWorstConf).T, capsize=2, label='Rand WCO Knapsack (worst)')

plt.errorbar(numOfAltsList, distRandWCORandAppMean, yerr=np.array(distRandWCORandAppConf).T, fmt='ks-.',linewidth=2, capsize=2,markersize=8, label='Rand WCO RandApp (avg)')
#plt.errorbar(numOfAltsList, distRandWCORandAppWorstMean, yerr=np.array(distRandWCORandAppWorstConf).T, capsize=2, label='Rand WCO RandApp (worst)')


#ax.set_yscale('log', nonposy='clip')
ax.set_xlim(xmin=min(numOfAltsList)-1, xmax=max(numOfAltsList)+1)
ax.set_ylabel('Distortion', fontsize=15)

ax.set_xlabel(r'Number of Alternatives, $m$', fontsize=15)
#plt.ylabel('Distortion', fontsize=15)
ax.grid()
plt.legend(loc='best')



### FILLED VS UNFILLED
plt.figure('Filled vs Unfilled')
ax = plt.subplot(111)
#plt.title('Distortion for Voting Rules')
ax.set_title(titleText)


# RANDOMIZED MECHANISMS

plt.errorbar(numOfAltsList, distRandValueMean, yerr=np.array(distRandValueConf).T, fmt='ko-.', linewidth=2, capsize=2,markersize=8, label='Rand Value (filled)')
#plt.plot(numOfAltsList, 4 * np.sqrt(numOfAltsList) * (np.log2(numOfAltsList) + 1), 'ro-', label='Rand Value, VFM (bound)')

plt.errorbar(numOfAltsList, distRandVFMMean, yerr=np.array(distRandVFMConf).T, fmt='kd-', linewidth=2, capsize=2,markersize=8, label='Rand VFM (filled)')


plt.errorbar(numOfAltsList, distRandApprovalMean, yerr=np.array(distRandApprovalConf).T, fmt='ks--', linewidth=2, capsize=2,markersize=8, label='Rand Approval (filled)')
#plt.plot(numOfAltsList, 4 * (np.log2(numOfAltsList)**2 + 1), 'ro-', label='Rand Approval (bound)')



plt.errorbar(numOfAltsList, distRandValueMean_WOFilling, yerr=np.array(distRandValueConf_WOFilling).T, fmt='kv--', linewidth=2, capsize=2,markersize=8, label='Rand Value (unfilled)')
plt.errorbar(numOfAltsList, distRandVFMMean_WOFilling, yerr=np.array(distRandVFMConf_WOFilling).T, fmt='k^--', linewidth=2, capsize=2,markersize=8, label='Rand VFM (unfilled)')
plt.errorbar(numOfAltsList, distRandApprovalMean_WOFilling, yerr=np.array(distRandApprovalConf_WOFilling).T, fmt='kx--', linewidth=2, capsize=2,markersize=8, label='Rand Approval (unfilled)')


#ax.set_yscale('log', nonposy='clip')
ax.set_xlim(xmin=min(numOfAltsList)-1, xmax=max(numOfAltsList)+1)
ax.set_ylabel('Distortion', fontsize=15)

ax.set_xlabel(r'Number of Alternatives, $m$', fontsize=15)
#plt.ylabel('Distortion', fontsize=15)
ax.grid()
plt.legend(loc='best')




ax2 = plt.subplot(122)
ax2.set_title('Distortion for Voting Rules\n'+'Input format: ' + inputFormat)

# DETERMINISTIC MECHANISMS

plt.errorbar(numOfAltsList, distValueMean, yerr=np.array(distValueConf).T, capsize=2, label='Det Value (simulation)')
#plt.plot(numOfAltsList, numOfAltsList**2, 'kd-', label='Det Value (bound)')
'''
'''
plt.errorbar(numOfAltsList, distBordaKnapsackMean, yerr=np.array(distBordaKnapsackConf).T, capsize=2, label='Borda Knapsack (simulation)')
plt.errorbar(numOfAltsList, distHarmonicKnapsackMean, yerr=np.array(distHarmonicKnapsackConf).T, capsize=2, label='Harmonic Knapsack (simulation)')
plt.errorbar(numOfAltsList, distPluralityKnapsackMean, yerr=np.array(distPluralityKnapsackConf).T, capsize=2, label='Plurality Knapsack (simulation)')
'''


'''
plt.errorbar(numOfAltsList, distBordaGreedyMean, yerr=np.array(distBordaGreedyConf).T, capsize=2, label='Borda Greedy (simulation)')
plt.errorbar(numOfAltsList, distHarmonicGreedyMean, yerr=np.array(distHarmonicGreedyConf).T, capsize=2, label='Harmonic Greedy (simulation)')
plt.errorbar(numOfAltsList, distPluralityGreedyMean, yerr=np.array(distPluralityGreedyConf).T, capsize=2, label='Plurality Greedy (simulation)')


ax2.set_xlabel(r'Number of Alternatives, $m$', fontsize=15)

#ax2.set_yscale('log', nonposy='clip')
ax2.set_xlim(xmin=min(numOfAltsList)-1, xmax=max(numOfAltsList)+1)


#### PART 2: PLOTTING THE DISTORTIONS WITH THE REAL DATA

fData = open('dist_output_dataset_boston2015yltc_sampled.txt', 'r')
for line in fData.readlines():
    exec(line)
fData.close()




selectedToPlotIndices = []

for index in xrange(len(distMean)):
    if selectedMechs[index] != 'Det Val' and selectedMechs[index] != 'Det Plurality Gr' and selectedMechs[index] != 'Det Harmonic Gr' and selectedMechs[index] != 'Det Borda Gr' and selectedMechs[index] != 'Det Plurality Kn' and selectedMechs[index] != 'Det Harmonic Kn' and selectedMechs[index] != 'Det Borda Kn':
        selectedToPlotIndices.append(index)

distMean = [distMean[index] for index in selectedToPlotIndices]
distConf = [distConf[index] for index in selectedToPlotIndices]
selectedMechs = [selectedMechs[index] for index in selectedToPlotIndices]

##  PLOTTING PART
opacity = 0.4
error_config = {'ecolor': '0.3'}

inputFormat = 'Boston YLTC 2015 (4-Approval)'


plt.figure('Distortion from the datasets')
ax = plt.subplot(111)
plt.title('Distortion for Voting Rules\nInput: '+inputFormat+', randRepeatCount = '+str(randRepeatCount)+', repeatConsistentValProfile = '+str(repeatConsistentValProfile))

yPositions = np.arange(len(distMean))
stepSize = min(np.diff(yPositions))
individualBarwidth = 0.8 * stepSize

plt.barh(yPositions, distMean, individualBarwidth, alpha=opacity, xerr=np.array(distConf).T, error_kw=error_config, color='b', label='Distortion')


plt.yticks(yPositions + individualBarwidth * 0.5, selectedMechs, rotation='horizontal', horizontalalignment='right')

xMax = int(np.ceil(max(distMean) + max(np.array(distConf)[:,0]) + 0.1))
plt.xticks(range(xMax+1))
#plt.xlabel('Mechanisms', fontsize=15)
plt.xlabel('Distortions', fontsize=15)
#ax.set_yscale('log', nonposy='clip')
ax.set_ylim(ymin=min(yPositions)-0.2*stepSize, ymax=max(yPositions)+1.2*stepSize)
plt.grid()
#plt.legend(loc='best')


figure = plt.gcf() # get current figure
figure.set_size_inches(20, 25)
#plt.savefig(filename+'.eps')
plt.savefig('dist_output_dataset_boston2015yltc_sampled.png', dpi=100)

plt.show()
'''