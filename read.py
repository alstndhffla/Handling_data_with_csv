import csv, os
os.chdir(r'C:\Users\alstn\PycharmProjects\handling-data-with-csv-files')
# 인코딩을 사용해 읽게 될 경우
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb1 in position 0: invalid start byte 와 같은 에러가 발생
# 이는 csv 파일의 내용이 8비트의 문자로 시작하지 않기 때문이다
# f = open('a.csv', 'r', encoding='utf-8')

# 16비트 바꿀 경우 아래와 같은 에러 발생
# UnicodeError: UTF-16 stream does not start with BOM
# f = open('a.csv', 'r', encoding='utf-16')

# 그래서 이렇게 사용
f = open('a.csv', 'r')
new = csv.reader(f)
for i in new:
    print(i)

# 다시 파일을 처음부터 읽기 위해서는 seek() 함수를 사용해 처음으로 이동시켜야 한다.
f.seek(0)
# csv 형을 리스트로 바꾸기 위해 임의의 객체(a_list)를 만들고
a_list = []
for i in new:
    # 반복문을 통해 차례대로 저장한다.
    a_list.append(i)

# 아래와 같이 그냥 print 만으로 출력할 경우 리스트 안은 텅 빈 것으로 출력된다.
# 그 이유는 new = csv.reader(f) 작업으로 커서가 맨 마지막으로 이동했기 때문...
# 다시 파일을 처음부터 읽기 위해서는 seek() 함수를 사용해 처음으로 이동시켜야 한다.
print(a_list)
