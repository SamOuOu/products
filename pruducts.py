#檢查檔案是否存在
import os

pruducts = []

if os.path.isfile('pruducts.csv'):
    print('UUU')
    #讀取
    with open('pruducts.csv', 'r') as f:
        for line in f:
            if '商品,價格' in line:
                continue
            name, price = line.strip().split(',') 
            pruducts.append([name, price])
    print(pruducts)

else:
    print('NNN')

#輸入新增
while True:
    name = input('請輸入商品名稱： ')
    if name == 'q':
        break
    price = input('請輸入商品價格： ')
    pruducts.append([name, price])
print(pruducts)

#印出每項
for p in pruducts:
    print(p[0], '的價格是', p[1])

#寫入檔案
with open('pruducts.csv', 'w') as f:
    f.write('商品,價格\n')
    for p in pruducts:
        f.write(p[0] + ',' + p[1] + '\n')
