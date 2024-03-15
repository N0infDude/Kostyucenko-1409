l = ''
with open('game.txt','r',encoding = 'utf-8') as f:
    for i in range(500):
        l += str(i)+' '+f.readline()+'\n'
str_l = ''.join(l)
str_l = str_l.replace('$','/')
print(str_l)
ans = open('game_new.txt','w',encoding = 'utf-8')
f.close()
ans.close()
