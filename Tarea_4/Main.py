from Empleados import Empleados
from Arrays import Array

arch = open("junio.txt","rt")
dat = 'dato'
while(dat != ('')):
    dat = arch.readline()
    dat_2 = dat.strip().split(',')
    print(dat_2)
