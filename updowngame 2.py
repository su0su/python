import random # 랜덤값

n=1
score = []
name = []

# 파일에 기록 저장
def writefile(best):
    fw = open("score.txt",'a')      # 파일을 뒤에 이어쓸 수 있도록 a 권한 부여
    fw.write(na + ':' + str(best) + '\n')
    fw.close()

#3,5번 피드백. 파일에서 점수를 불러서 비교
#파일에서 기록 가져옴
def readfile():
    f = open("score.txt",'r')
    line=f.readlines()

    for i in range(0,len(line)):
        f1=line[i].split(':') #':'를 기준으로 line리스트에 저장   
        name.append(f1[0]) #name에 파일에서 가져온이름 저장
        score.append(int(f1[1])) #score에 파일에서 가져온 점수 저장

    score.reverse()
    if line:
        best=int(score[0])
        score.reverse()
    else: best = 11

    return best

# 4번 피드백, 파일에서 점수 불러와서 최고 기록 비교
b = readfile()
 
while True:
    print("UP & DOWN 게임에 오신걸 환영합니다~")
    print("1.게임 시작 2. 기록 확인 3. 게임종료")

    num = int(input(">>"))

    if num == 1: # 게임시작
        answer = random.randint(1,100) # 랜덤값 1부터 100까지 생성
        print(answer)

        first=1
        last=100

        while (n < 11): # 1,2번 피드백. 범위 잘못 입력시 횟수 카운트 x
            my=int(input("%d번째 숫자 입력(%d~%d) : " %(n,first, last)))

            if n==10 and my !=answer: # 10번을 초과했는데 답을 맞추지 못할 경우
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
            elif my < first or my > last: # 범위에 없는 숫자면 맞춘 횟수를 카운트 하지 않음
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
                #congra=n # n을 congra변수에 저장시켜 다시 1로 바뀌기 전의 값을 넣어줌
                if b > n or not score:       # 기존에 있던 (첫번째일 경우 10) 최대값보다 n이 작을 경우
                    print("최고기록 갱신 ~!")
                    
                    na=input("닉네임을 입력하세요 >> ")
                    writefile(n)
                    score.append(n) # 점수 리스트 score에 점수 n을 추가
                    name.append(na)
                    b=n
                    n=1
                    break               
                else : #최고 기록만 점수판에 넣어줌
                    print("\n")
                    break            

    elif num == 2 : # 기록 확인 
        if not name:
            print("기록이 없습니다.")
            print(name)
        else :         
            f3 = open("score.txt",'r')
            lines=f3.readlines() 

            print("rank/name/score")

            for i in range(len(lines),0,-1):
                print(len(lines)-i+1, end=' ')
                print(name[i-1], end=' ')
                print(score[i-1])       
    else : 
        print("게임을 종료합니다. 감사합니다.")
        break
