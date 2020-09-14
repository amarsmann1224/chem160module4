from random import random, choice
from math import exp
Temp= 2.3
n=20
n2 = n*n
nlist=list(range(n))
ntrials=200000
nequil=100000
Tmax = 4.0
Temp=0.0
dT=0.1
while Temp<Tmax:
    Temp+=dT
    E_sum = 0.0
    E2_sum= 0.0

    spins=[[1 for i in range(n)] for j in range(n)]

    for trial in range(1,(ntrials+nequil+1)):
        i=choice(nlist)
        j=choice(nlist)

        deltaE=2.*(spins[i][j]*\
                   (spins[i][(j+1)%n] + spins[i][(j-1+n)%n]+\
                    spins[(i+1)%n][j] + spins[(i+-1+n)%n][j]))

        if exp(-deltaE/Temp) > random():
            spins[i][j]=-spins[i][j]
        else:
            deltaE=0.0

        if trial==nequil:
            energy=0.0
            for i in range(n):
                for j in range(n):
                    energy-=(spins[i][j]*
                             (spins[i][(j+1)%n]+spins[i][(j-1+n)%n]+\
                              spins[(i+1)%n][j]+spins[(i+-1+n)%n][j]))
            energy/=n2

        if trial > nequil:
            energy+=deltaE/n2
            E_sum+=energy
            E2_sum+=energy*energy
    E_ave=E_sum/ntrials
    E2_ave=E2_sum/ntrials
    Cv=1/(Temp*Temp)*(E2_ave-E_ave*E_ave)
    print('%8.4f %10.6f %10.6f'%(Temp, E_ave,Cv))
