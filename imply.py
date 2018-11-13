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

cr8dict(51, '/Users/srai/Documents/imply/access.log')
