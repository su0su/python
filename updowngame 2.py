import random # 랜덤값

n=1
score = []
name = []
rank=[]
best=10
total=0
congra=0

#기록 확인 하는 함수
def check():

    score.reverse()
    name.reverse()

    for i in range(0,total): # 게임한 횟수동안 반복
        print(i+1, end='  ')
        print(name[i], end='  ')
        print(score[i])

    score.reverse()
    name.reverse()

#파일 읽어오는 함수
def scorefile():
    f = open("score.txt",'r')
    line=f.readlines()

    for i in range(0,len(line)):
        f1=line[i].split(':') #':'를 기준으로 line리스트에 저장
        rank.append(f1[0]) #rank에 순위 저장
        name.append(f1[1]) #name에 이름 저장
        score.append(f1[2]) #score에 점수 저장

        print(rank[i], end=' ')
        print(name[i], end=' ')
        print(score[i])

    if not line: #파일에 내용이 없다면 check함수
        check()

    f.close()

        
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
            my=int(input("%d번째 숫자 입력(%d~%d) : " %(n,first, last)))

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
            elif my < first or my > last: # 2번 피드백. 범위에 없는 숫자면 맞춘 횟수를 카운트 하지 않음
                print("범위에 없는 숫자입니다. 다시 입력해주세요.")
                continue
            elif my == last and my != answer: # 입력한 값과 최댓값이 같고 정답이 아닐 경우
                print("DOWN")
                n = n+1
            elif my == first and my != answer: # 입력한 값고 최솟값이 같고 정답이 아닐 경우
                print("UP")
                n = n+1
            else: 
                print("정답입니다!!")
                print("%d번째만에 맞추셨습니다." %(n))
                congra=n # 1번 피드백 n을 congra변수에 저장시켜 다시 1로 바뀌기 전의 값을 넣어줌
                n=1
                if best > congra :       # 기존에 있던 (첫번째일 경우 10) 최대값보다 n이 작을 경우
                    print("최고기록 갱신 ~!")
                    score.append(congra) # 점수 리스트 score에 점수 n을 insert
                    total=total+1         # 기록을 갱신한 총 횟수
                    best=congra
                    print("\n")

                    na=input("닉네임을 입력하세요 >> ")
                    print(na)
                    name.append(na)
                    print(name)
                    break               
                else : # 3번 피드백. 최고 기록만 점수판에 넣어줌
                    print("\n")
                    break            

    elif num == 2 : # 기록 확인  
        print("rank/name/score")
        scorefile()
         
    else : # 게임 종료시 파일에 기록 저장
        f = open("score.txt",'w') 
        score.reverse()
        name.reverse()

        for i in range(0,total): # 게임한 횟수동안 반복
         f.write("%s:%s:%s" %(i+1,name[i],score[i]))
         f.write("\n")

        f.close()

        print("게임을 종료합니다. 감사합니다.")
        break


    
