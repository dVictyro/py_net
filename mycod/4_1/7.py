mac = "AAAA:BBBB:CCCC"

mac1 = mac.split(':')




print('{:b}{:b}{:b}'.format(int(mac1[0],16),int(mac1[1],16),int(mac1[2],16)))
