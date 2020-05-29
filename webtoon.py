from bs4 import BeautifulSoup 
import urllib.request
import os,re # 태그, 공백 제거를 위해 필요

# HTTP Error 403: Access Denied 에러 제거. 봇 우회
opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

# 웹툰 이름 가져오기
html = urllib.request.urlopen("https://comic.naver.com/webtoon/list.nhn?titleId=654774&weekday=mon")
result = BeautifulSoup(html.read(),"html.parser")
name = result.findAll("h2") # 만화 제목 가져오기
tag = result.find_all(['span']) # h2 속 span태그 가져와 제거위함

for s in tag: # span 태그 제거 (만화작가이름)
    s.extract()

text = re.sub('<.+?>', '', str(name), 0, re.I|re.S) # 모든 태그 제거 <>
nospace = re.sub('&nbsp;| |\t|\r|\n|]', '', text) # 공백과 []괄호 제거
folder=nospace[4:]
if not os.path.isdir(folder):
    os.mkdir(folder) # '웹툰,'부분 이후의 제목으로 폴더 생성
os.chdir(folder)
print(folder+" 폴더 생성")

page = result.findAll('td',{'class':'title'}) # class 명이 title인 td 안에 회차 주소 존재
num=1
for s in page:
    html1 = urllib.request.urlopen("https://comic.naver.com"+s.a['href']) # 회차 주소로 이동
    result1 = BeautifulSoup(html1.read(),"html.parser")  
    img = result1.findAll('img',{'alt':'comic content'}) # <img alt =comic content>에 이미지 파일 존재

    # 회차 별 폴더 만들기
    title = result1.find('h3') # 회차 제목 가져오기
    titletext = re.sub('<.+?>', '', str(title), 0, re.I|re.S) # 태그 제거
    if not os.path.isdir(titletext):
        os.mkdir(titletext)
    os.chdir(titletext)

    #이미지 저장 
    for i in img:
        save=str(num)+'.jpg' # 파일 이름과 확장자
        path=i.get("src") # 파일 경로
        urllib.request.urlretrieve(path,save) # 이미지 저장
        num=num+1
    print(titletext+" 저장 완료")
    os.chdir("..") # 저장 후 상위 폴더로 이동
print("끝")
     