pruducts = []
while True:
    name = input('請輸入商品名稱： ')
    if name == 'q':
        break
    price = input('請輸入商品價格： ')
    pruducts.append([name, price])
print(pruducts)

for p in pruducts:
    print(p[0], '的價格是', p[1])
