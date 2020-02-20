#!/usr/bin/python3

import math
import random

def encrypt(M, n, e):
	C = (M**e) % n
	print 'Verschluessele Nachricht mit M^e mod n: ' + str(C)
	return C
