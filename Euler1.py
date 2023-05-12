multiples_list = []

for i in range(0, 1000):
    if i % 3 == 0 or i % 5 == 0:
        multiples_list.append(i)

print(multiples_list)
print(sum(multiples_list))
