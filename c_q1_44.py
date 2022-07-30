#Измение уровня доступа
def com44_chk(txt_m,k):
    k_old=0
    k_all=['1','2','3','4']
    z=[]
    while True:
        while True:
            print(txt_m[22])
            print(txt_m[17])
            k_login=str(input())
            if k_login=='выход':
                return
            a=open('login.txt','r',encoding='utf-8')
            b=a.readline()
            while b!='':
                c=b.split('/*/')
                if k_login==c[0]:
                    k_old=c[2]
                    k_password=c[1]
                b=a.readline()
            a.close()
            if k_old==0:
                print(txt_m[12])
                continue
            if int(k)<=int(k_old):
                print(txt_m[24])
                continue
            break
        while True:
            print(txt_m[25])
            print(txt_m[17])
            k_new=str(input())
            if k_new=='выход':
                return
            if k_new not in k_all:
                print(txt_m[26])
                continue
            if int(k_new)>=int(k):
                print(txt_m[23])
                continue
            if int(k_new)==int(k_old):
                print(txt_m[28])
                continue
            break
        print('''Логин: %s
Старый уровень доступа: %s
Новый уровень доступа: %s'''%(k_login,k_old,k_new))
        while True:
            print(txt_m[21])
            y=str(input())
            if y=='да':
                h=1
                break
            elif y=='нет':
                h=0
                break
            else:
                print(txt_m[3])
        if h==1:
            break
        else:
            print(txt_m[20])
    new_user_k=k_login+'/*/'+k_password+'/*/'+k_new
    a=open('login.txt','r',encoding='utf-8')
    b=a.readline()
    while b!='':
        z.append(b)
        b=a.readline()
    a.close()
    for i in z:
        m=i.split('/*/')
        if k_login==m[0]:
            if i==z[-1]:
                z.remove(i)
                z.append(new_user_k)
            else:
                z.remove(i)
                z.append('\n'+new_user_k)
            break
        
    a=open('login.txt','w',encoding='utf-8')
    for i in z:
        a.write(i)
    a.close()
#Удаление пользователя
def com44_du(txt_m,k):
    l=[]
    m=[]
    h=0
    while True:
        z=0
        print(txt_m[29])
        print(txt_m[17])
        del_user=str(input())
        if del_user=='выход':
            return
        a=open('login.txt','r',encoding='utf-8')
        b=a.readline()
        while b!='':
            c=b.split('/*/')
            if del_user==c[0]:
                z=1
                dup=c[1]
                duk=c[2]
                break
            b=a.readline()
        a.close()
        if z==0:
            print(txt_m[12])
            continue
        if duk=='4\n':
            print(txt_m[31])
            continue
        del_user_login=del_user+'/*/'+dup+'/*/'+duk
        print(txt_m[30])
        a=open('login.txt','r',encoding='utf-8')
        b=a.readline()
        g=open('info.txt','r',encoding='utf-8')
        u=g.readline()
        while b!='':
            c=b.split('/*/')
            if c[0]==del_user:
                print('''Логин: %s
Пароль: %s
Уровень доступа: %s'''%(c[0],c[1],c[2]))
                break
            b=a.readline()
        while u!='':
            f=u.split('*;*')
            if f[0]==del_user:
                print('''%s
%s
%s'''%(f[1],f[2],f[3]))
                break
            u=g.readline()
        while True:
            print(txt_m[32])
            y=str(input())
            if y=='да':
                h=1
                break
            elif y=='нет':
                h=2
                break
            else:
                print(txt_m[3])
        if h==2:
            break
        a.close()
        g.close()
        a=open('login.txt','r',encoding='utf-8')
        b=a.readline()
        while b!='':
            l.append(b)
            b=a.readline()
        a.close()
        a=open('info.txt','r',encoding='utf-8')
        b=a.readline()
        while b!='':
            m.append(b)
            b=a.readline()
        a.close()
        for i in l:
            n=i.split('/*/')
            if n[0]==del_user:
                l.remove(i)
                break
        for i in m:
            v=i.split('*;*')
            if v[0]==del_user:
                m.remove(i)
                break
        a=open('login.txt','w',encoding='utf-8')
        for i in l:
            a.write(i)
        a.close()
        a=open('info.txt','w',encoding='utf-8')
        for i in m:
            a.write(i)
        a.close()
        break
