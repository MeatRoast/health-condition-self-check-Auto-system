# 교육부 건강상태 자가진단 시스템 / 학생자가진단 시스템
# 해당 소스를 사용하실려면 아래 모듈을 설치해주세요
# pip install selenium
# 해당 시스템은 학교검색에 첫번쩨 학교만 할 수 있습니다. ( 귀차나서 작업안함.. )0
# 2022-02-10-Thur 시스템 변경으로 업데이트 되었습니다.
# 자유롭게 사용이 가능하며 블로그, 카페, 페이스북, SNS 등등 소스코드 업로드, 리뷰 목적 사용 시에는 꼭 GitHub링크 남겨주세요!
# https://github.com/MeatRoast
from selenium import webdriver
import time
# -----------------------------------------------------------------------------------------
# 시/도 번호를 선택해주세요!
# 서울특별시: 02
# 부산광역시: 03
# 대구광역시: 04
# 인천광역시: 05
# 광주광역시: 06
# 대전광역시: 07
# 울산광역시: 08
# 세종특별자치시: 09
# 경기도: 10
# 강원도: 11
# 충청북도: 12
# 충청남도:13
# 전라북도: 14
# 전라남도: 15
# 경상북도: 16
# 경상남도: 17
# 제주특별자치도: 18

city = ''

# -----------------------------------------------------------------------------------------
# 유초중고특 선택!
# 유치원: 2
# 초등학교: 3
# 중학교: 4
# 고등학교: 5
# 특수학교 등: 6

level = ''

# -----------------------------------------------------------------------------------------
# 크롬 드라이브 경로 작성
_system = ""
# -----------------------------------------------------------------------------------------
# 정보

school = ''
named = ''
bh = '' # YYMMDD
# PW
pw = ''

# 크롬드라이브
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument("disable-gpu")
web = webdriver.Chrome(executable_path=f"{_system}")

#웹사이트 접속
web.get("https://hcs.eduro.go.kr/#/loginHome")
web.find_element_by_id("btnConfirm2").click() # 자가진단하기 클릭
web.find_element_by_xpath('//*[@id="schul_name_input"]').click() #학교찾기 클릭
web.find_element_by_xpath(f'//*[@id="sidolabel"]/option[{city}]').click() # 시/도 선택
web.find_element_by_xpath(f'//*[@id="crseScCode"]/option[{level}]').click() #유초중고특 선택
web.find_element_by_id('orgname').send_keys(school) # 학교명 입력
web.implicitly_wait(0.5)
web.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[3]/td[2]/button').click() #해당 학교 검색
web.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/ul').click() # 첫번쩨에 있는 학교 불러오기
web.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/ul/li/a').click() # 학교 선택하기
web.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[2]/input').click() # 이름 입력하기 클릭
web.find_element_by_xpath('//*[@id="user_name_input"]').send_keys(named) # 이름 입력
web.find_element_by_xpath('//*[@id="birthday_input"]').send_keys(bh) # 생년월일 입력
web.find_element_by_xpath('//*[@id="btnConfirm"]').click() # 확인 클릭
print('학교 통과 완료')
time.sleep(1)
# PASSWORD 입력부분
web.find_elements_by_xpath('//*[@id="WriteInfoForm"]/table/tbody/tr/td/div')
web.find_element_by_class_name('keyboard-icon').click()
time.sleep(0.3)
for i in list(pw):
    time.sleep(1)
    web.find_element_by_css_selector(f'[aria-label="{i}"]').click()
time.sleep(0.5)
web.find_element_by_xpath('//*[@id="btnConfirm"]').click() # 확인 클릭
print('Password 입력완료')
time.sleep(1)
web.find_element_by_xpath('//*[@id="container"]/div/section[2]/div[2]/ul/li/a/em').click() # 확인 클릭
time.sleep(0.3)
web.find_element_by_xpath('//*[@id="survey_q1a1"]').click() # 자가진단 아니요 클릭
web.find_element_by_xpath('//*[@id="survey_q2a1"]').click() # 자가진단 음성 클릭
web.find_element_by_xpath('//*[@id="survey_q3a1"]').click() # 자가진단 아니요 클릭
web.find_element_by_xpath('//*[@id="btnConfirm"]').click() # 확인 클릭
name = web.find_element_by_xpath('//*[@id="container"]/div/div[2]/div[1]/p[1]').text # 이름/학교명 텍스트 변화
day = web.find_element_by_xpath('//*[@id="container"]/div/div[2]/div[1]/p[2]').text # 자가진단 일시 날짜 참여 상태 텍스트 변화
te = web.find_element_by_xpath('//*[@id="container"]/div/div[2]/div[2]/p').text # 등교 가능 여부 텍스트 변화
print(f'{name}') # name값 출력
print(f'{day}') # day값 출력
print(f'{te}') # te값 출력
print('자가진단 완료')
