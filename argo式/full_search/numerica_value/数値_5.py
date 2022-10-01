"""
正の整数 N が与えられます。 1 以上 N 以下の整数 i について、次の問題に答えてください。

i が 3 でも 5 でも割り切れるならば FizzBuzz を出力し、
それ以外で i が 3 で割り切れるならば Fizz を出力し、
それ以外で i が 5 で割り切れるならば Buzz を出力し、
i がどちらでも割り切れないならば i 自身を出力してください。

Nは 1 以上 100 以下の整数
"""
# 入力を受け取る
N = int(input())

# i に 1 から N までの数を順番に代入する
for i in range(1,N+1):
    # i が 3でも5でも割り切れる場合、FizzBuzzを出力
    if  i%3==0 and i%5==0:
        print('FizzBuzz')
    # i が 3で割り切れる場合、Fizzを出力
    elif i%3==0:
        print('Fizz')
    # i が 5で割り切れる場合、Buzzを出力
    elif i%5==0:
        print('Buzz')
    else:
        print(i)
