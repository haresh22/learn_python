# Logical "AND" 
# OPT 1 (True) and OPT 2 (True ) = result is True 
# OPT 1 (True) and OPT 2 (False ) = result is False
# OPT 1 (False) and OPT 2 (True) = result is False
# OPT 1 (False) and OPT 2 (False) = result is False

a = 10 
b = 6 
c = 20
d = 11
value = (a > b) and (d<c)
print(value)
##########################

a = 100 
b = 200
c = 20
d = 90
value = (b>a) and (c>d)
print(value)
######################################
a = 23
b = 100
c = 10
d = 34
value = (b < a) and (d > c)
print(value)
#######################################
a = 12
b = 100
c = 2
d = 10
value = (a > b) and (d > c)
print(value)
