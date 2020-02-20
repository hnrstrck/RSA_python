#!/usr/bin/python3

import math
import random
import fractions
import decrypt
import encrypt

def keygen():
	print '\033[1;34mGeneriere Schluesselpaar:\033[1;m'                
	p = int(raw_input('Gib p ein (Primzahl): '))
	q = int(raw_input('Gib q ein (Primzahl): '))

	print ''
	print '\033[1;34mBerechne:\033[1;m'                
	n = p*q
	print 'n = p*q = ' + str(n)	

	phi = (p-1)*(q-1)
	print 'phi = (p-1)*(q-1) = ' + str(phi)

	e = random.randint(2,phi);
	while(fractions.gcd(phi,e) != 1):
		e = random.randint(2,phi)
	print 'e = ' + str(e)

	d = mulinv(e, phi)
	print 'd = e^(-1) mod phi = ' + str(d)

	print ''
	print '\033[1;34mSchluesselpaar:\033[1;m'    
	print '\033[1;32moeffentlicher Schluessel\033[1;m (n, e):    \033[1;32m(' + str(n) + ', ' + str(e) + ')\033[1;m'     
	print '\033[1;31mprivater Schluessel\033[1;m (n, d):         \033[1;31m(' + str(n) + ', ' + str(d) + ')\033[1;m'

	print ''
	print '\033[1;34mBeispiel:\033[1;m'   
	M = int(raw_input('Gib eine zu verschluesselnde Zahl M ein (M < n): '))

	print ''
	print '\033[1;34mErgebnisse:\033[1;m'   
	C = encrypt.encrypt(M, n, e)
	M2 = decrypt.decrypt(C, n, d)


# Source: http://codegists.com/snippet/python/extgcdpy_jimzhong_python 
def mulinv(b, n):
    g, x, _ = xgcd(b, n)
    if g == 1:
        return x % n

# Source: http://codegists.com/snippet/python/extgcdpy_jimzhong_python 
def xgcd(b, n):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, b, n = b // n, n, b % n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return  b, x0, y0