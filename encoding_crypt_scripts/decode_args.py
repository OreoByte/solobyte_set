#!/usr/bin/python3
import base64
import argparse
'''
  ___                 ____        _           _          _                _ 
 / _ \ _ __ ___  ___ | __ ) _   _| |_ ___    | |__   ___| |_ __   ___  __| |
| | | | '__/ _ \/ _ \|  _ \| | | | __/ _ \   | '_ \ / _ \ | '_ \ / _ \/ _` |
| |_| | | |  __/ (_) | |_) | |_| | ||  __/   | | | |  __/ | |_) |  __/ (_| |
 \___/|_|  \___|\___/|____/ \__, |\__\___|___|_| |_|\___|_| .__/ \___|\__,_|
                            |___/       |_____|           |_|  
'''

parser = argparse.ArgumentParser(description='Decode base encrypted strings.')
parser.add_argument("-b64", type=str, required=False, help='Decode base64. EX ./decode.py -b64 YmFzZTY0IHRlc3Q= -n 1')
parser.add_argument('-b32', type=str, required=False, help='Decode base32. EX ./decode.py -b32 MJQXGZJTGIQHIZLTOQ====== -n 1')
parser.add_argument('-b16', type=str, required=False, help='Decode base16. EX ./decode.py -b16 626173653136206865 78 -n 1')
parser.add_argument("-n", type=int, required=False, help='Number of times to decode.')

args = parser.parse_args()
number = args.n
i = 0

base_64 = args.b64
base_32 = args.b32
base_16 = args.b16
#r = [base_64, base_32, base_16]

if base_16:
    while i <= number:
        r = base_16
        b = r.encode('ascii')
        db = base64.b16decode(b)
        m = db.decode('ascii')
        i += 1
        if i == number:
            break
elif base_32:
    while i <= number:
        r = base_32
        b = r.encode('ascii')
        db = base64.b32decode(b)
        m = db.decode('ascii')
        i += 1
        if i == number:
            break
elif base_64:
    while i <= number:
        r = base_64
        b = r.encode('ascii')
        db = base64.b64decode(b)
        m = db.decode('ascii')
        i += 1
        if i == number:
            break
else:
    print("Select a valid number")
print(m)
