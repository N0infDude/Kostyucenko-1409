l = ''
line=''
with open('game.txt','r',encoding = 'utf-8') as f:
    for i in range(501):
        l += str(i)+' '+f.readline()+'\n'
# str_l = ''.join(l)
# str_l = str_l.replace('$','/')
print(f)
f.close()

    