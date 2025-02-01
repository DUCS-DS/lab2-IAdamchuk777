# Lists for testing
mylist = [2, 2, 4, 200]  # Increasing 
mylist1 = [20, 15, 5, -5]  # Decreasing 
mylist2 = [3, 5, 4, 6]  # Not Monotonic

def isincreasing(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

def isdecreasing(lst):
    for i in range(len(lst) - 1):
        if lst[i] < lst[i + 1]:
            return False
    return True

def monotonic(lst):
    return isincreasing(lst) or isdecreasing(lst)

print(monotonic(mylist))   # True
print(monotonic(mylist1))  # True
print(monotonic(mylist2))  # False
#Ivan Adamchuk