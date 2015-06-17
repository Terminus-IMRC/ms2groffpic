#!/usr/bin/env python3

import math
import sys

def error(str, exitcode=1):
	print(sys.argv[0] + ": error: " + str, file=sys.stderr)
	exit(exitcode)

def main():
	while True:
		try:
			s=input()
		except EOFError:
			break

		s=s.split()

		if len(s)==0 or math.modf(math.sqrt(len(s)))[0]!=0:
			error("invalid length of input line: " + str(len(s)))
		Ceilings=len(s)
		X=int(math.sqrt(Ceilings))

		print(".PS")
		for i in range(Ceilings):
			if i%X==0:
				print("T%d: "%(i/X), end="")
			print("box \"%s\" height 0.25 width 0.25"%(s[i]), end="")
			if i!=0 and i%X==0:
				print(" with .nw at T%d.sw"%(i/X-1), end="")
			print("")
		print(".PE")

if __name__=='__main__':
	main()
