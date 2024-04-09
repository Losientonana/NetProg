total_sum = 0
for num in range(1, 1001): 
    for s in str(num):  
        total_sum += int(s)

print(total_sum)
