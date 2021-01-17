"""

Input files:

 - MJD_times_A1.csv : MJD times at the beginning of each single pulse with A1
 - MJD_times_A2.csv : MJD times at the beginning of each single pulse with A2
 - pulses_merge_A1.npy : complete set of single pulses with A1
 - pulses_merge_A2.npy : complete set of single pulses with A2

Output files_

 - new_pulses_A1.npy : new set of single pulses with A1
 - new_pulses_A2.npy : new set of single pulses with A2

"""

import numpy as np

pulses_A1 = np.load("pulses_merge_A1.npy")          	# load the complete set of single pulses with A1
pulses_A2 = np.load("pulses_merge_A2.npy")          	# load the complete set of single pulses with A2

MJD_A1 = np.loadtxt("MJD_times_A1.csv", usecols=0)  	# load the MJD times of the single pulses with A1
MJD_A2 = np.loadtxt("MJD_times_A2.csv", usecols=0)  	# load the MJD times of the single pulses with A2

n = 0
m = 0

if MJD_A1[0] < MJD_A2[0]:                           	# if the observation with A1 starts earlier than the observation with A2

	while int(MJD_A1[n]*1e6) != int(MJD_A2[0]*1e6): # we search the single pulse with A1 that coincides with the first single pulse with A2

		n += 1

	start_A1 = n					# index of the new first single pulse with A1
	start_A2 = 0

	while n < len(MJD_A1)-1 and m < len(MJD_A2)-1:	# we search the last single pulse common to both antennas

		n += 1
		m += 1

	finish_A1 = n					# index of the new last single pulse with A1
	finish_A2 = m					# index of the new last single pulse with A2

elif MJD_A1[0] > MJD_A2[0]:			    	# if the observation with A2 starts earlier than the observation with A1

        while int(MJD_A1[0]*1e6) != int(MJD_A2[m]*1e6):	# we search the single pulse with A2 that coincides with the first single pulse with A1

                m += 1

	start_A1 = 0
	start_A2 = m					# index of the new first single pulse with A2

        while n < len(MJD_A1)-1 and m < len(MJD_A2)-1:	# we search the last single pulse common to both antennas

                n += 1
                m += 1

	finish_A1 = n					# index of the new last single pulse with A1
	finish_A2 = m					# index of the new last single pulse with A2
	
print("Length A1 observation = " + str(len(MJD_A1[start_A1:finish_A1]) + " pulses"))
print("Length A2 observation = " + str(len(MJD_A2[start_A2:finish_A2]) + " pulses"))

if(len(MJD_A1[start_A1:finish_A1]) == len(MJD_A2[start_A2:finish_A2])): # we now check that the lengts of the new datasets are the same

        print("Matching sucessful")

        np.savetxt("new_pulses_A1.csv", pulses_A1[start_A1:finish_A1,:], delimiter=',')
        np.savetxt("new_pulses_A2.csv", pulses_A2[start_A2:finish_A2,:], delimiter=',')

        np.save("new_pulses_A1.npy", pulses_A1[start_A1:finish_A1,:])
        np.save("new_pulses_A2.npy", pulses_A2[start_A2:finish_A2,:])


