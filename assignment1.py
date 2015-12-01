import sys

infile = sys.argv[1]
outfile = sys.argv[2]
firstline = True

with open(infile,'r') as filein, open(outfile, 'w') as fileout:
	for line in filein.readlines(): 
		if firstline:
			msg = '%s'
			firstline = False
		else:
			msg = '\n%s'
		if not line.strip():
			words_count = 0
			fileout.write(msg % words_count)
		else:
			words=line.split()
			words_count=len(words)
			fileout.write(msg % words_count)
