"""

Input files:

 - MJD_times_A1.csv : MJD times at the beginning of each single pulse with A1
 - MJD_times_A2.csv : MJD times at the beginning of each single pulse with A2
 - pulses_merge_A1.npy : single pulses with A1
 - pulses_merge_A2.npy : single pulses with A2

Output files_

 - new_pulses_A1.npy
 - new_pulses_A2.npy

"""

import numpy as np
import csv

pulses_A1 = np.load("pulses_merge_A1.npy")
pulses_A2 = np.load("pulses_merge_A2.npy")

MJD_A1 = np.loadtxt("MJD_times_A1.csv", usecols=0)
MJD_A2 = np.loadtxt("MJD_times_A2.csv", usecols=0)

n = 0
m = 0

if MJD_A1[0] < MJD_A2[0]:

	while int(MJD_A1[n]*1e6) != int(MJD_A2[0]*1e6):

		n += 1

	start_A1 = n
	start_A2 = 0

	while n < len(MJD_A1)-1 and m < len(MJD_A2)-1:

		n += 1
		m += 1

	finish_A1 = n
	finish_A2 = m

elif MJD_A1[0] > MJD_A2[0]:

        while int(MJD_A1[0]*1e6) != int(MJD_A2[m]*1e6):

                m += 1

	start_A1 = 0
	start_A2 = m

        while n < len(MJD_A1)-1 and m < len(MJD_A2)-1:

                n += 1
                m += 1

	finish_A1 = n
	finish_A2 = m
	
print("Length A1 observation = " + str(len(MJD_A1[start_A1:finish_A1]) + " pulses"))
print("Length A2 observation = " + str(len(MJD_A2[start_A2:finish_A2]) + " pulses"))

if(len(MJD_A1[start_A1:finish_A1]) == len(MJD_A2[start_A2:finish_A2])):

        print("Funciona")

        np.savetxt("new_pulses_A1.csv", pulses_A1[start_A1:finish_A1,:], delimiter=',')
        np.savetxt("new_pulses_A2.csv", pulses_A2[start_A2:finish_A2,:], delimiter=',')

        np.save("new_pulses_A1.npy", pulses_A1[start_A1:finish_A1,:])
        np.save("new_pulses_A2.npy", pulses_A2[start_A2:finish_A2,:])


