from selenium import webdriver  
driver = webdriver.Chrome('/Users/조수경/Downloads/chromedriver_win32/chromedriver.exe') #크롬 드라이버 경로
driver.get('http://zzzscore.com/1to50/?ts=1591461175994') # 접속할 사이트 URL

btns = driver.find_elements_by_xpath('//*[@id="grid"]/div[*]') #div 태그 속에 있는 숫자 버튼
num = 1
while num<=50: # 번호가 총 50개이기 때문에 50번 반복
    for s in btns:
        if s.text == str(num):
            s.click()
            print("number " + str(num)+ " cliked!")
            num += 1
            break