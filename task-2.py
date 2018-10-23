numbers = [456,456345,6456346,1356,1546,1457,145,7246724671,61,345,13451345,3456,4545134,5134,545,145]

#This returns the first duplicate found and asumes that there are no further duplicates
def findDuplicateNumber(numbers):
    seen = []
    for n in numbers:
        if n not in seen:
            seen.append(n)
        else:
            return n

print findDuplicateNumber(numbers)
