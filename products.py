#while 迴圈適合用在不知會用幾次情況下
products = []
while True :
	name = input ('請輸入商品名稱：')
	if name == 'q':
		break
	price = input ('請輸入價格')
	products.append([name,price]) #二維清單 （同個位置有多個input)
print (products)

for p in products:
	print (p[0], '的價格是', p[1])