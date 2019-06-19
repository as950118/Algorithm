'''
설명은
https://blog.naver.com/na_qa/221454850891
'''
x,y,w,h = map(int, input().split())
print(min(w-x, h-y, x, y))
