def even_number(num):
    even=[]
    for i in num:
        if i % 2==0:
            even.append(i)
    return even
n = [2,4,5]
print(even_number(n))