import sys
import matplotlib.pyplot as plt
import bump

#argments with sensorData from sensorData/lin-137XXXXXXXX.txt
argc=len(sys.argv)
if argc==1:
	sys.exit()

appdix=sys.argv[1].split('-').pop()
filename="./Download/output/"+appdix

data=[]
head=0
tail=0
for line in open(filename):
	parts=line.split('\t\t')
	if len(parts)!=6:
		break
	data.append(float(parts[2]))
	tail=long(parts[5])

for line in open(filename):
	parts=line.split('\t\t')
	head=long(parts[5])
	break

xAxis=list(range(0,len(data)))

bumpPrefix="./Download/bumps/bump-"
stamp=bump.xInterval(bumpPrefix + appdix)

size=tail-head
if size==0:
	sys.exit()
size=float(size)
rSize=len(data)-1
rSize=float(rSize)

bAxis=[.0]
for it in stamp:
	bAxis.append((it-head)*rSize/size)
bAxis.append(rSize)
bYs=[0]*len(bAxis)

plt.plot(xAxis,data)
plt.plot(bAxis, bYs, 'ro')
plt.show()
