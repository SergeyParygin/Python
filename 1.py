NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload";
ch_NAT = NAT.split();
ch_NAT[7] = ch_NAT[7].replace('Fast', 'Gigabit');
rez_NAT = ' '.join(ch_NAT);
#print(rez_NAT);


MAC = 'AAAA:BBBB:CCCC'
ch_MAC = MAC.replace(':','.')
#print (ch_MAC)

CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100'
ch_CONFIG = CONFIG.split()
vlan = ch_CONFIG[4].split()
print (vlan)