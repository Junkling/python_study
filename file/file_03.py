# csv
# csv meme type = text/csv

import csv

with open('../resource/test_csv_01.csv' , 'r' , encoding='utf-8') as f7:
    reader = csv.reader(f7)
    print(reader)
    print(type(reader))

    print(dir(reader))
    # 첫 행의 구분을 뺴기 위한 작업
    col = next(reader)
    print(col)

    for k , v in enumerate(reader):
        print(f'[{k}], {v}')

    # 여기를 초기화 해줘야 맨 위로 커서가 올라감

    f7.seek(0)

    col = next(reader)
    print(col)
    for i in reader:
        print(f'{i[0]} is {i[1]} years old')

with open('../resource/test_csv_01.csv' , 'r' , encoding='utf-8') as f8:
    # 구분좌를 지정할 수 있음
    reader = csv.reader(f8 ,delimiter='|' )

    for row in reader:
        print(row)

with open('../resource/test_csv_01.csv' , 'r' , encoding='utf-8') as f9:
    # 구분좌를 지정할 수 있음
    reader = csv.DictReader(f9)
    print(reader)
    print(type(reader))
    print(dir(reader))

    for key , row in enumerate(reader):
        print(row)

w_list = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]

with open('../resource/test_csv_02.csv' , 'w' , encoding='utf-8') as w1:
    print(dir(csv))
    csv_writer = csv.writer(w1)
    print(dir(csv_writer))
    print(type(csv_writer))
    # csv_writer.writerows(w_list)
    for row in w_list:
        csv_writer.writerow(row)



with open('../resource/test_csv_03.csv' , 'w' , encoding='utf-8') as w2:
    fields = ['One', 'Two', 'Three']
    wt = csv.DictWriter(w2, fieldnames=fields)
    wt.writeheader()

    for v in w_list:
        wt.writerow({'One' : v[0], 'Two' : v[1], 'Three' : v[2]})


with open('../resource/test_csv_03.csv' , 'r' , encoding='utf-8') as f10:
    # 구분좌를 지정할 수 있음
    reader = csv.DictReader(f10)
    print(reader)
    print(type(reader))
    print(dir(reader))

    for key , row in enumerate(reader):
        print(row)