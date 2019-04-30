#!/usr/bin/env python
p = str(input('Enter ip adress:'))
p = p.replace('.',' ')
p = p.split()
for ip in p:
    if int(ip)>255:
        print('Incorrect IPV4')
        break
    elif len(p)!= 4:
        print('Incorrect IPV4')
        break    
    
if int(ip[0])<127:
    print('Class A')
elif int(ip[0])<191:
    print('Class B')
        elif int(ip[0])<223:
            print('Class C')
        elif int(ip[0])<239:
            print('Class D')





