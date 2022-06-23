start = 0
end = 1000000
for num in range(start,end):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else: 
            print('prime number:',num)