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