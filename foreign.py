import os, re		# os 모듈과 re 모듈은 항상 필요하기 때문에 먼저 임포트
import usecsv		# usecsv 모듈을 임포트
os.chdir(r'C:\Users\alstn\PycharmProjects\handling-data-with-csv-files')
# popSeoul.csv 파일을 저장한 경로로 이동합니다

# 외국인비율 구하기
# 이 명령을 실행하기 전에, 같은 폴더에 'usecsv.py' 가 복사되어 있거나, usecsv.py 가 전체 경로에서 이동될 수 있도록 설정.

# 파일 열기 
total = usecsv.opencsv('popSeoul.csv')	

# 콤마 등을 제거하는 함수 usecsv.switch 를 사용
newPop = usecsv.switch(total)	
# 4번째 구까지만 시범출력
print(newPop[:4])

for i in newPop:
    foreign = 0
    # 한 번 루프가 돌고 나면 foreign 을 다시 지정해줘야 하므로 foreign 을 0으로 먼저 지정
    try:
	    foreign = round(i[2] / (i[1] + i[2]) * 100, 1)
        # i[0]에는 지역구 이름이 저장되어 있고, foreign 은 외국인 비율
	    print(i[0], foreign)
    except:
	    pass

new = [['구', '한국인', '외국인', '외국인 비율(%)']]
# 등록외국인의 비율이 3이 넘을 때만 넘을 때만 출력
for i in newPop:
    foreign = 0
    try:
        foreign = round(i[2] / (i[1] + i[2]) * 100, 1)
        if foreign > 3:
            new.append([i[0], i[1], i[2], foreign])
    except:
        pass

# 3% 넘는 구만 파일로 저장하기
usecsv.writecsv('newPop.csv', new)
