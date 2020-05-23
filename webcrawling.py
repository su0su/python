from bs4 import BeautifulSoup 
import urllib.request

print("***서울여자대학교 학과 및 홈페이지 정보")
print("학과             홈페이지")

html = urllib.request.urlopen("http://www.swu.ac.kr/www/swuniversity.html")
result = BeautifulSoup(html.read(),"html.parser")
major = result.findAll("a")

for s in major:
    # 단어 필터링
    if "대학원" in s.text or "바롬" in s.text or "교육원" in s.text or "자율전공학부" in s.text or "공동기기실" in s.text:
        continue
    else:
        html1 = urllib.request.urlopen("https://www.swu.ac.kr"+s['href']) # 해당 학부의 소개 사이트로 이동
        result1 = BeautifulSoup(html1.read(),"html.parser")
        page = result1.find("a",{"class":"btn btn_xl btn_blue_gray"}) #a의 btn btn_xl btn_blue_gray 클래스에 학부 사이트가 저장되어 있음
    
        if page == None: # 학부 사이트가 없을 때
            print(s.text+"\t\t홈페이지가 존재하지 않음")
        else : 
            if "홈페이지" in page.text: # "홈페이지" 단어가 들어가면 사이트 존재
                print(s.text+"\t\t"+page['href'])
            else: 
                print(s.text+"\t\t홈페이지가 존재하지 않음")
