from random import randint

secret_num =  randint(1,100)
try_count = 0 #시도 횟수
guess_num = 0 #예상 숫자

while guess_num != secret_num and try_count <= 4:
    guess_num = eval(input("choosing num"))
    if(guess_num > secret_num):
        print("숫자가 더 작습니다.")
    
    elif(guess_num < secret_num):
        print("숫자가 큽니다.")
        
    else:
        print("정답입니다.")

if(guess_num == 5 and secret_num != guess_num):
    print("ㅅㄱㅇ")