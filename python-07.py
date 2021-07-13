"""
1) Print the following patterns using loop :

a.

*
**
***
****

b.

*
***
*****
***
*
"""
c = 0

while c <= 5:
    print(f"{c*'*'}")
    c = c + 1
while c >= 0:
    print(f"{c * '*'}")
    c = c -1




