#!/usr/bin/env python
import sys
import getopt
import pyperclip
from substitute import fullSub
from substitute import basicSub
from substitute import appendNumbers
import argparse


def printPasswords(passwords):
	for password in passwords:
		print(password)
	print('%s passwords generated.' % len(passwords))

def writePasswordsToClipboard(passwords):
	pwList = '\n'.join(passwords)
	print('%s passwords copied to the clipboard.' % (len(passwords)))
	pyperclip.copy(pwList)

def writePasswordsToFile(outputFile, passwords):
    with open(outputFile, 'w') as f:
        f.write('\n'.join(passwords) + '\n')
    print('%s passwords written to %s' % (len(passwords), outputFile))

parser = argparse.ArgumentParser()

if __name__ == '__main__':
	parser.add_argument("-o", "--outputFile", help="The file that the password list will be written to.")
	parser.add_argument("-f", "--full", help="Full password list flag.  This can generate a very large password", action="store_true")
	parser.add_argument("-c", "--copy", help="Copy password list result to the clipboard.", action="store_true")
	parser.add_argument("-n", "--numbers", help="Append numbers flag.", action="store_true")
	parser.add_argument("password",nargs="*")
	args = parser.parse_args()

	if not args.password:
	    parser.error('provide a password word to generate variations')

	password = args.password[0]

	#load full or basic password list based on arguments passed in
	if args.full:
		passwords = fullSub(password)
	elif args.numbers:
		passwords = appendNumbers(password)
	else:
		passwords = basicSub(password)

	#save passwords to file
	if args.outputFile != None:
		writePasswordsToFile(args.outputFile, passwords)
	#copy passwords to clipboard
	elif args.copy:
		writePasswordsToClipboard(passwords)
	else:
		printPasswords(passwords)
