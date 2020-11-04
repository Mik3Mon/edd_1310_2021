from Empleados import Empleados
from Arrays import Array

arch = open("junio.txt","rt")
dat = 'ddd'

while(dat != ('')):
    dat = arch.readline()
    dat_2 = dat.strip().split(',')
