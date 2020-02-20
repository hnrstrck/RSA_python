#!/usr/bin/python3

import keygen
import decrypt
import encrypt

def main():
    #\033c loescht das Terminal
	print '\033c\033[1;31m   ******************\033[1;m'
	print '\033[1;31m   *\033[1;33m  RSA-Programm  \033[1;m\033[1;31m*\033[1;m'
	print '\033[1;31m   ******************\033[1;m'
	print ''
	print 'Was moechtest du?'
	print '[1]   Schluesselpaar generieren (mit Beispiel)'
	print '[2]   Verschluesseln'
	print '[3]   Entschluesseln'

	auswahl = raw_input('Auswahl [1..3]: ')

        #Weiterleiten
	if auswahl is '1':
		print ''
		keygen.keygen()
	elif auswahl is '2':
		print ''
		M = int(raw_input('Gib M ein: '))
		n = int(raw_input('Gib n ein: '))
		e = int(raw_input('Gib e ein: '))
		print ''
		encrypt.encrypt(M, n, e)
	elif auswahl is '3':
		print ''
		C = int(raw_input('Gib C ein: '))
		n = int(raw_input('Gib n ein: '))
		d = int(raw_input('Gib d ein: '))
		print ''
		decrypt.decrypt(C, n, d)
	else:
		main()

		
if __name__ == "__main__":
	main()
