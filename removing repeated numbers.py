numbers=[2,3,4,5,2,3,4,6,7]
repeated=[]
for num in numbers:
    if num not in repeated:
        repeated.append(num)
print(repeated)