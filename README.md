# imply
Imply IO evaluation [https://gist.github.com/gianm/f7c2ae5e8bb7d9f318c3b83fda563cac]

## Solution: Coding Challenge

### To run the program

- Ensure that python 3 or above is installed
- Change to a new/existing directory on your computer
- Download the file imply.py OR just copy & paste the following code into a file with name of your choice
```
# !/usr/bin/env python

import zipfile ,sys, hashlib

user = {}

def cr8dict(iter, filename):
    with open(filename, 'r') as f:
        for line in f:
            row = line.split(",")
            if row[1] in user:
                user[row[1]].append(row[2])
            else:
                user[row[1]] = [row[2]]
    f.close()

    with open('/tmp/users.txt','w') as f1:
       for k, v in user.items():
          if (len(set(v))) >= int(iter):
            #print k, len(set(v))
             f1.write(k + "\n")
    f1.close()

cr8dict(sys.argv[1],sys.argv[2])
```
- Download the source file in your desired location, making note of its absolutely path
- Unzip the file access.log.gz after it is downloaded
- Execute the program using syntax similar to the following, here 50 is the N paths within /tmp/access.log 
```
python <filename> 50 /tmp/access.log
```
- Execpected output can be found in the /tmp/users.txt directory

### Approach for this solution
Python dictionaries are closest things to Hashmap in Java and iterating through items and performing recursive searches are simple to perform, as compared to bash

### Any alternative approach
I would have considered bash or awk, however, there are not enough examples or references as compared to python

### Resource needs and performance analysis
The program is not really optimized for files with huge size, dictionary may or may not be a good approach. 

### Possible future improvements
Introduce exception handling, provisioning for variant data sizes, provisioning for handling compressed/uncompressed input file.

