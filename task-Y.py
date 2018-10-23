import math

c = 50
h = 30

def calculate(d):
    return int(round(math.sqrt((2*c*d/h))))

csv = raw_input("Please enter the values: ").split(",")

result = []
for i in csv:
    result.append(str(calculate(int(i))))

print ",".join(result)
