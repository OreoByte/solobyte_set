#!/usr/bin/python3
import base64
i = 0

r = input("Base: ")

option = int(input("Select Base16(1), Base32(2), Base64(3): "))

number = int(input("Number of times to decode: "))

if option == 1:
    while i <= number:
        b = r.encode('ascii')
        db = base64.b16decode(b)
        m = db.decode('ascii')
        r = m
        i += 1
        if i == number:
            break

elif option == 2:
    while i <= number:
        b = r.encode('ascii')
        db = base64.b32decode(b)
        m = db.decode('ascii')
        r = m
        i += 1
        if i == number:
            break
elif option == 3:
    while i <= number:
        b = r.encode('ascii')
        db = base64.b64decode(b)
        m = db.decode('ascii')
        r = m
        i += 1
        if i == number:
            break
else:
    print("Select a valid number")

print(m)
