# データを受け取る
N = int(input())

# 1 から N まで  
for i in range(1,N+1): 
    if i%3==0 and i%5==0:
        print("FizzBuzz")  
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)