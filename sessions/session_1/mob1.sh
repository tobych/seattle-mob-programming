#!/bin/bash
echo "Hello world"
mkdir -p dunno
cd dunno
rm -f master.zip
wget https://github.com/tobych/disaster/archive/master.zip 
rm -fR disaster-master
unzip master.zip
rm master.zip
ls
