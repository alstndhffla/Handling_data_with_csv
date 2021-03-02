import csv, os
os.chdir(r'C:\Users\alstn\PycharmProjects\handling-data-with-csv-files')
# 읽어올 파일 위치를 지정해줘야한다.

"""
csv 파일을 불러와 리스트에 변환저장시켜주는 함수
파일을 열 때 filename 에 opencsv('test.csv') 식으로 기입한다.
"""


def opencsv(filename):
    f = open(filename, 'r')
    # csv.reader 로 파일을 읽어 reader 에 저장
    reader = csv.reader(f)
    output = []
    for i in reader:
        output.append(i)
    return output
    # 파일 닫기
    f.close()


# 만든 함수 활용
opencsv('a.csv')
# 안에 내용물 확인
print(opencsv('a.csv'))