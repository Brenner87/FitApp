#!/usr/local/bin/python3
import re
def Main():
	line='I think I understand regular expressions'
	matchResult=re.match(r'think',line)
	print (matchResult)
	matchResult=re.search(r'think',line)
	print (matchResult)


Main()
