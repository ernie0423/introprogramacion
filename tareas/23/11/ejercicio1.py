num_fact = 1
FACT = []

for num in range(1,20+1):
    num_fact = num * num_fact
    FACT.append(num_fact)

print(FACT)