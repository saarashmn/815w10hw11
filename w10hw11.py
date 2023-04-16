import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

#coin flip central limit. 

def Sampler(rate):
    return stats.bernoulli.rvs(rate)

def Frequency(Infile):
    
    InputFile = Infile
    Nroll = 1
    Npass0 = []
    Npass_min = 1e8
    Npass_max = -1e8

    with open(InputFile) as ifile: #Opens files
        for line in ifile: #
            lineVals = line.split() #splits lines ups
            Nroll = len(lineVals) #obtains the number of rolls
            Npass = 0 #defines the number of experiments
            for v in lineVals: #Chance of getting a 1 i.e the house winining the game. 
                Npass += float(v)

            if Npass < Npass_min:
                Npass_min = Npass
            if Npass > Npass_max:
                Npass_max = Npass 
            Npass0.append(Npass)
            
    return (Npass0,Nroll)
#The actual Experiment
Nexp0 = 100
Nexp1 = Nexp0*10
Nexp2 = Nexp1*10
Roll = 100
rate = 0.5

outfile = open("Rolls_Central_100.txt", 'w+')
for e in range(0,Nexp0):
    for t in range(0,Roll):
        outfile.write(str(Sampler(rate)) +" ")
    outfile.write(' \n')
outfile.close()

outfile = open("Rolls_Central_1000.txt", 'w+')
for e in range(0,Nexp1):
    for t in range(0,Roll):
        outfile.write(str(Sampler(rate)) +" ")
    outfile.write(' \n')
outfile.close()

outfile = open("Rolls_Central_10000.txt", 'w+')
for e in range(0,Nexp2):
    for t in range(0,Roll):
        outfile.write(str(Sampler(rate)) +" ")
    outfile.write(' \n')
outfile.close()
#Data file name
InputFile0 = "Rolls_Central_100.txt"
InputFile1 = "Rolls_Central_1000.txt"
InputFile2 = "Rolls_Central_10000.txt"

#frequency of outputs
Output100   = Frequency(InputFile0)
Output1000  = Frequency(InputFile1)
Output10000 = Frequency(InputFile2)
print(Output100)
print("\n  ")
print(Output1000)
print("\n")
print(Output10000)



# make Npass figure

fig, ax = plt.subplots() 
plt.title("100(blue),1000(red),10000(yellow)experiments")
plt.xlabel("Frequency")
plt.ylabel("Probability")
hist1 = ax.hist(Output100[0], Output100[1], density=True, color='b', alpha=0.7)

title = str(Roll) +  " rolls / " + str(Nexp1) +" experiment"


# make Npass figure

plt.xlabel("Frequency")
plt.ylabel("Probability")
hist2 = ax.hist(Output1000[0], Output1000[1], density=True, color='r', alpha=0.7)

title = str(Roll) +  " rolls / " + str(Nexp2) +" experiment"


# make Npass figure

plt.xlabel("Frequency")
plt.ylabel("Probability")
hist3 = ax.hist(Output10000[0], Output10000[1], density=True, color='y', alpha=0.7)
plt.show()
