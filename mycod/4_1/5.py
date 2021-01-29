command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"
set1 = set(command1.split()[-1].split(','))
set2 = set(command2.split()[-1].split(','))
list1 = sorted(list(set1 & set2))
print(list1)

