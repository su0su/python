import random

n=1
score=[0,0,0,0,0]
best=10
total=0

while True:

    print("UP & DOWN 게임에 오신걸 환영합니다~")
    print("1.게임 시작 2. 기록 확인 3. 게임종료")

    num = int(input(">>"))

    if num == 1:
        answer = random.randint(1,100)
        print(answer)

        first=1
        last=100


        for i in range(0,10):
            my=int(input("%d번째 숫자 입력(%d~%d) : " %(i+1,first, last)))

            if i==9 and my !=answer:
                print("입력횟수를 초과하셨습니다.")
                break

            if my > answer and my < last:   # last>my>answer 일 경우
                print("DOWN")
                last = my                   #범위는 my<?<first가 됨
                n = n+1                     #실행횟수 증가
            elif my < answer and my > first:    #anser>my>first 일 경우
                print("UP")
                first = my
                n = n+1
            elif my < first or my > last:
                print("범위에 없는 숫자입니다. 다시 입력해주세요.")
                n = n+1
            elif my == last and my != answer:
                print("DOWN")
                n = n+1
            elif my == first and my != answer:
                print("UP")
                n = n+1
            else:
                print("정답입니다!!")
                print("%d번째만에 맞추셨습니다." %(n))
                if best > n :
                    print("최고기록 갱신 ~!")
                    score.insert(total,n)
                    total=total+1
                    break               
                else : 
                    print("최고기록은 %d입니다." %(n))
                    score.insert(total,n)
                    total=total+1
                    break            

    elif num == 2 :
        print(total)
        for i in range(0,total):
         print(i+1, end='  ')
         print(score[i])

         
    else :
        print("게임을 종료합니다. 감사합니다.")
        break


    
