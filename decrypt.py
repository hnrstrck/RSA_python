#!/usr/bin/python3

import math
import random

def decrypt(C, n, d):
	M = C**d % n
	print 'Entschluesselte Nachricht mit C^d mod n: ' + str(M)
	return M
