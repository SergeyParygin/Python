#!/usr/bin/env python
import socket
import struct

from sys import argv

ip = input('Enter ip addres (0.0.0.0/0): ')
ch_ip = ip.replace('.',' ')
ch_ip = ch_ip.replace('/',' /')
ch_ip = ch_ip.split()
print('Network:\n',
    "%15s %15s %15s %15s" %
    (ch_ip[0], ch_ip[1], ch_ip[2], ch_ip[3] )
    )
print(
    "%15s %15s %15s %15s" %
    (bin(int(ch_ip[0])), bin(int(ch_ip[1])), bin(int(ch_ip[2])), bin(int(ch_ip[3])) )
)
print('Mask:\n', ch_ip[4])

#def cidr_to_netmask(ip)
network, net_bits = ip.split('/')
host_bits = 32 - int(net_bits)
netmask = socket.inet_ntoa(struct.pack('!I', (1 << 32) - (1 << host_bits)))
#return network, netmask
print(netmask)