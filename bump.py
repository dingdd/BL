import sys

def xInterval(bf):
	stamp=[]
	for line in open(bf):
		stamp.append(long(line))
	appdix=bf.split('-')
	appdix=appdix.pop()
	return stamp
