import os

#讀取檔案
def read_file(filename):
    products = []
    with open(filename, 'r') as f:
        for line in f:
            if '商品,價格' in line:
                continue
            name, price = line.strip().split(',') 
            products.append([name, price])
    return(products)

#輸入新增
def user_input(products):
    while True:
        name = input('請輸入商品名稱： ')
        if name == 'q':
            break
        price = input('請輸入商品價格： ')
        products.append([name, price])
    print(products)
    return(products)

#印出每項
def print_products(products):
    for p in products:
        print(p[0], '的價格是', p[1])

#寫入檔案
def write_file(filename, products):
    with open(filename, 'w') as f:
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + p[1] + '\n')

#檢查檔案是否存在
def main():
    filename = 'products.csv'
    if os.path.isfile(filename):
        print('UUU')
        products = read_file(filename)

    else:
        print('NNN')

    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)

main()