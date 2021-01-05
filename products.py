# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 20:56:58 2020

@author: wayne
"""
import os
products = []
if os.path.isfile('product.csv'):
    print('找到檔案')
    with open ('product.csv', 'r') as f:
        for line in f:
            if '商品,價格' in line :
                continue
            name, price = line.strip().split(',')
            products.append([name, price])
    print(products)

else:
    print('檔案遺失')
        
#使用者輸入
while True:
    name = input('請輸入商品名稱：')
    if name == 'q':
        break
    price = int(input('請輸入商品價格：'))
    
    products.append([name , price])
print (products)

for p in products:
    print(p[0], '的價格是' ,p[1])
    
with open ('product.csv' , 'w' ) as f :
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n')
    