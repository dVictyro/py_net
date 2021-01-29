ospf_route = "       10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"

list1 = ospf_route.replace(',','').replace('[','').replace(']','').split()


templ = '\n{:25} {}'*5
#'''
#Prefix t {:<20}
#AD {:>20}
#Next-hop {:>20}
#Last Update {:>20}3
#Out interface {:>20}
#'''


print(templ.format(
'Prefix', list1[0],
'AD', list1[1],
'Next-hop', list1[3],
'Last upd', list1[4],
'Out interface', list1[5]))
