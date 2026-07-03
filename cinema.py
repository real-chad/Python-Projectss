ages = [15,18,98,45,32,62,76,82,58]
regulars = []
seniors = []
for i in ages:
    if i >= 60:
        seniors.append(i)
    else:
        regulars.append(i)
elderest_regular = regulars[0]
seat_elder_reg = 0

for i in range(len(regulars)):
    if regulars[i] > elderest_regular:
        elderest_regular = regulars[i]
        seat_elder_reg = i
print(f"The Number of seniors are {len(seniors)} and list of their ages is {seniors}")
print(f"The number of regular viewers are {len(regulars)} and list of their ages is {regulars}")
print(f"The Senior most in the regulars is {elderest_regular} at seat no {seat_elder_reg}")
    

