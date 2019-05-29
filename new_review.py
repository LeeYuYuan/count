data = []
count = 0
sum_len = 0
with open('reviews.txt', 'r') as f:
	for result in f:
		data.append(result)
for d in data:
    count = count + 1	
    print('第', count, '則留言共有', len(d), '個字元')
    sum_len = sum_len + len(d)   
print('平均留言長度', sum_len / len(data))
print('此檔案中共有', len(data), '筆留言')
print('總共有', sum_len, '個字元')

new = []
number = 0
for d in data:
	if len(d) > 100:
		new.append(d)
print('一共有', len(new), '比留言長度大於100')


positive = []
for p in data:
	if 'good' in p:
		positive.append(p)
print('一共有', len(positive), '則正面留言')


count = 1
wc = {}
for d in data:#字數出現次數計算
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] = count + 1
		else:
			wc[word] = count
			if wc[word] > 2000:
				print(word, wc[word])


