#!/bin/bash

dataPrefix=`pwd`
datapath="$dataPrefix/Download"
adb pull /sdcard/Download/ $datapath
if [ $? -ne 0 ]
then
	echo "pulling data from sdcard error"
	exit
fi

clear
echo "data pulling successfully done"

sensorPrefix="$datapath/sensorData/lin-*"
filenum=`ls -l $sensorPrefix |wc -l`
echo "filenum" + $filenum

if [ "$filenum" = "0" ]
then
	echo "Require Files are not exist"
	exit
fi

echo "trying tranform raw data.............."

java -jar tabletmerge.jar

files=`ls -r $sensorPrefix`
for item in $files
do
	arr=(${item//-/ })
	echo "processing file lin-${arr[1]} .."
	python readData.py "$item"
	exit
done
