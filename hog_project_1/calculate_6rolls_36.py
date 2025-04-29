
# create a array of 36 to restore
result = [0] * 37
dice = [2, 3, 4, 5, 6]

# calculate the 1 case
case1 = 1 - pow(5/6, 6)


sum_posibility = pow(5, 6)

# calculate the other cases with 5sided dice
for i1 in dice:
    for i2 in dice:
        for i3 in dice:
            for i4 in dice:
                for i5 in dice:
                    for i6 in dice:
                        outcome = i1 + i2 + i3 + i4 + i5 + i6
                        result[outcome] += 1

for i in range(0, 37):
    result[i] = (result[i]/sum_posibility) * (1 - case1)
    result[i] = f"{result[i]:.6f}"
result[1] = case1
result[1] = f"{result[1]:.6f}"

for j in range(0, 37):
    print(j, ": ", result[j])
# multiplty the (1 - 1case) with the others

