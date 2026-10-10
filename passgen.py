#!/usr/bin/env python
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
    with open(outputFile, 'w', encoding='utf-8') as f:
        f.write('\n'.join(passwords) + '\n')
    print('%s passwords written to %s' % (len(passwords), outputFile))

parser = argparse.ArgumentParser()

if __name__ == '__main__':
	output_group = parser.add_mutually_exclusive_group()
	output_group.add_argument("-o", "--outputFile", help="Write the candidate list to a UTF-8 file.")
	output_group.add_argument("-c", "--copy", help="Copy the candidate list to the clipboard.", action="store_true")
	mode_group = parser.add_mutually_exclusive_group()
	mode_group.add_argument("-f", "--full", help="Generate all character substitutions (maximum 1,000,000 candidates).", action="store_true")
	mode_group.add_argument("-n", "--numbers", help="Append numeric suffixes.", action="store_true")
	parser.add_argument("password", help="Input word; quote it if it contains spaces")
	args = parser.parse_args()

	try:
		if args.full:
			passwords = fullSub(args.password)
		elif args.numbers:
			passwords = appendNumbers(args.password)
		else:
			passwords = basicSub(args.password)
	except ValueError as exc:
		parser.error(str(exc))

	#save passwords to file
	if args.outputFile != None:
		writePasswordsToFile(args.outputFile, passwords)
	#copy passwords to clipboard
	elif args.copy:
		writePasswordsToClipboard(passwords)
	else:
		printPasswords(passwords)
