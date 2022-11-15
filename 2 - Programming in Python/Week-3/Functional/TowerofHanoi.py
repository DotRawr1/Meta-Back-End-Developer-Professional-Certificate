# only one disk can be moved at a time
# only the upper disk of any of the towers can be moved
# larger disks cannot be placed over smaller disks
# optimal will be 2^n-1, where n is the number of disks to be moved

# Recursive function for Tower of Hanoi
def hanoi(disks, source, helper, destination):
    # Base Condition - complete execution and avoid infinite loops
    if (disks == 1):
        print('Disk {} moves from tower {} to tower {}.'.format(disks, source, destination))
        return
    # Recursive calls in which function calls itself
    hanoi(disks - 1, source, destination, helper)
    print('Disk {} moves from tower {} to tower {}.'.format(disks, source, destination))
    hanoi(disks - 1, helper, source, destination)
# Driver code - generic term used to denote the section that calls the function or class
disks = int(input('Number of disks to be displaced: '))
'''
Tower names passed as arguments:
Source: A
Helper: B
Destination: C
'''
# Actual function call
hanoi(disks, 'A', 'B', 'C')

# output: Number of disks to be displaced: 3
"""
Disk 1 moves from tower A to tower C.
Disk 2 moves from tower A to tower B.
Disk 1 moves from tower C to tower B.
Disk 3 moves from tower A to tower C.
Disk 1 moves from tower B to tower A.
Disk 2 moves from tower B to tower C.
Disk 1 moves from tower A to tower C.
"""