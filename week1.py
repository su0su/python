import random # 랜덤값

n=1
score=[0,0,0,0,0]
best=10
total=0

while True:

    print("UP & DOWN 게임에 오신걸 환영합니다~")
    print("1.게임 시작 2. 기록 확인 3. 게임종료")

    num = int(input(">>"))

    if num == 1: # 게임시작
        answer = random.randint(1,100) # 랜덤값 1부터 100까지 생성
        print(answer)

        first=1
        last=100


        for i in range(0,10): 
            my=int(input("%d번째 숫자 입력(%d~%d) : " %(i+1,first, last)))

            if i==9 and my !=answer: # 10번을 초과했는데 답을 맞추지 못할 경우
                print("입력횟수를 초과하셨습니다.")
                break

            if my > answer and my < last:   # last>my>answer 일 경우
                print("DOWN")
                last = my                   # 범위는 my<?<first가 됨
                n = n+1                     # 실행횟수 증가
            elif my < answer and my > first:    # anser>my>first 일 경우
                print("UP")
                first = my
                n = n+1
            elif my < first or my > last: # 입력한 값이 최댓값보다 크거나 최솟값보다 작을 경우
                print("범위에 없는 숫자입니다. 다시 입력해주세요.")
                n = n+1
            elif my == last and my != answer: # 입력한 값과 최댓값이 같고 정답이 아닐 경우
                print("DOWN")
                n = n+1
            elif my == first and my != answer: # 입력한 값고 최솟값이 같고 정답이 아닐 경우
                print("UP")
                n = n+1
            else: 
                print("정답입니다!!")
                print("%d번째만에 맞추셨습니다." %(n))
                if best > n :                   # 기존에 있던 (첫번째일 경우 10) 최대값보다 n이 작을 경우
                    print("최고기록 갱신 ~!")
                    score.insert(total,n) # 점수 리스트 score에 점수 n을 insert
                    total=total+1         # 게임한 총 횟수
                    break               
                else : 
                    print("최고기록은 %d입니다." %(n))
                    score.insert(total,n)
                    total=total+1
                    break            

    elif num == 2 : # 기록 확인
        print(total)
        for i in range(0,total): # 게임한 횟수동안 반복
         print(i+1, end='  ')
         print(score[i])

         
    else :
        print("게임을 종료합니다. 감사합니다.")
        break


    
