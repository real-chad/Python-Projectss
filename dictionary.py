# Question1  for dictionaries
# Merge two dictionaries into one.
# d1={a:1}, d2={b:2}


d1={"a":1,"b":2}
d2={"c":3,"d":4}
# Functional Approach
d1.update(d2)
print(d1)
# Vanilla Python
for i in d2:
    d1[i] = d2[i]
print(d1)

# Question no 2
# Sum all values in a dictionary.
d3 = {"a":10,"b":20,"c":30}

sum = 0
for i in d3.values():
    sum = sum + i
print(sum)

# Question no 3
# Count the frequency of each element in a list using a dictionary.
l1 = ["a","b","a","c","b","a"]
d ={}
# {"a":3,"b":2,"c":1}


for i in l1:
    if i in d.keys():
        d[i] = d[i] +1
    else:
        d[i] = 1
print(d)

# Question no 4
# Combine two dicts, adding values for common keys.
d5={"a":5,"b":3} 
d6={"b":4,"c":2}

for i in d6:
    if i in d5:
        d5[i] = d5[i] + d6[i]
    else:
        d5 [i] = d6[i]
print(d5)

    



    