from Empleados import Empleados
arch = open("junio.txt","rt")
dat = 'dato'
while(dat != ('')):
    dat = arch.readline()
    print(dat)

em_1 = Empleados("317182260","Miguel","Monzon","Lucero","15","13000","2019")
print(em_1.to_string())
