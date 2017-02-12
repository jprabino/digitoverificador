#!/usr/bin/python3

import re
import sys
#Si se está usando python2 en lugar de python3, reeplazo la funcion raw_input por input.
try:
    input=raw_input
except NameError:
    pass


def sum_digits(digits):    
    while digits=>10:
        digstrstr = str(digits)
        digits = sum([int(o) for o in digstrstr])
    return digits

#Diccionario de caracteres.
dv_dict={'A':'14', 'B':'01','C':'00','D':'16','E':'05','F':'20','G':'19',
'H':'09', 'I':'24','J':'07', 'K':'21', 
'L':'08','M':'04' ,'N':'13' ,'O':'25' ,
'P':'22' ,'Q':'18','R':'10','S':'02' ,
'T':'06' ,'U':'12','V':'23' ,'W':'11' ,
'X':'03','Y':'15','Z':'17',}

#Toma el dominio (patente) del automotor y verifica que teng el formato ABC123
m=None
while not m:
    dom = input('INGRESE EL DOMINIO (q para salir):').upper()
    
    if dom=='Q':
        sys.exit(0)
    m = re.match('([A-Z]{3})([0-9]{3})',dom)

    if not m:
        print('Formato de dominio no válido. Por favor ingrese nuevamente en formato ABC123')

#Toma las letras del dominio y los numeros.
dom_letters = m.group(1)
dom_numbers = m.group(2)

dv_wholestring = ''.join([dv_dict[l] for l in dom_letters]+[n for n in dom_numbers])


oddsum = 0
evsum = 0   
for k,v in enumerate(dv_wholestring[::-1]):
    if k%2:
        evsum+=int(v)
    else:
        oddsum+=int(v)

oddsum = sum_digits(oddsum)
evsum = sum_digits(evsum)

print('DIGITO VERIFICADOR: {}{}'.format(oddsum,evsum))
