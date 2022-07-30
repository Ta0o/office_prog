#Создание нового пользователя
def com37_nu(txt_m):
    q=['!','"','$','%','&',"'",'(',')','*','+','`','-','/',':',';','<','>','=','?','@','[',']','^','_','|','{','}','~',',','#','№',' ']
    w=['1','2','3','4','5','6','7','8','9','0','.']
    e=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
    y=[31,29,31,30,31,30,31,31,30,31,30,31]
    t=[]
    info_file=[]
    login_file=[]
    logins=[]
    a=open('login.txt','r',encoding='utf-8')
    b=a.readline()
    while b!='':
        if '\n' in b:
            login_file.append(b[:-1])
        else:
            login_file.append(b)
        l_p_k=b.split('/*/')
        logins.append(l_p_k[0])
        b=a.readline()
    a.close()
    a=open('info.txt','r',encoding='utf-8')
    b=a.readline()
    while b!='':
        if '\n' in b:
            info_file.append(b[:-1])
        else:
            info_file.append(b)
        b=a.readline()
    a.close()
    while True:
        while True:
            p=0
            print(txt_m[18],'фамилию:')
            f=str(input())
            f=f.lower()
            f.strip()
            for i in q:
                if i in f:
                    p+=1
            for i in w:
                if i in f:
                    p+=1
            for i in e:
                if i in f:
                    p+=1
            if p!=0 or len(f)<2:
                print(txt_m[8])
                continue
            else:
                f1=f[0].upper()
                f=f1+f[1:]
                t.append(f)
                break
        while True:
            p=0
            print(txt_m[18],'имя:')
            f=str(input())
            f=f.lower()
            f.strip()
            for i in q:
                if i in f:
                    p+=1
            for i in w:
                if i in f:
                    p+=1
            for i in e:
                if i in f:
                    p+=1
            if p!=0 or len(f)<2:
                print(txt_m[8])
                continue
            else:
                f1=f[0].upper()
                f=f1+f[1:]
                t.append(f)
                break
        while True:
            p=0
            print(txt_m[18],'отчество:')
            f=str(input())
            f=f.lower()
            f.strip()
            for i in q:
                if i in f:
                    p+=1
            for i in w:
                if i in f:
                    p+=1
            for i in e:
                if i in f:
                    p+=1
            if p!=0 or len(f)<2:
                print(txt_m[8])
                continue
            else:
                f1=f[0].upper()
                f=f1+f[1:]
                t.append(f)
                break
        while True:
            p=0
            print(txt_m[18],'дату рождения(в формате << **.**.**** >>):')
            dr=str(input())
            for j in dr:
                if j not in w:
                    p+=1
            if p!=0:
                print(txt_m[8])
                continue
            dr1=dr.split('.')
            if (len(dr1)!=3):
                print(txt_m[19])
                continue
            else:
                if (len(dr1[0])!=2) or (len(dr1[1])!=2) or (len(dr1[2])!=4):
                    print(txt_m[19])
                    continue
                else:
                    if (int(dr1[1])>12) or (int(dr1[2])>2022) or (int(dr1[2])<1900) or (int(dr1[0])>31) or ('00' in dr1[0]) or ('00' in dr1[1]) or ('0000' in dr1[2]):
                        print(txt_m[19])
                        continue
                    else:
                        if y[int(dr1[1])-1]<int(dr1[0]):
                            print(txt_m[19])
                            continue
                        elif(int(dr1[2])%4!=0) and (int(dr1[1])==2) and (int(dr1[0])>=29):
                            print(txt_m[19])
                            continue
                        else:
                            t.append(dr)
                            break
        while True:
            print(txt_m[18],' логин:')
            l=str(input())
            if l in logins:
                print(txt_m[7])
                continue
            t.append(l)
            break
        while True:
            print(txt_m[18],' пароль:')
            p=str(input())
            t.append(p)
            break
        while True:
            print(txt_m[18],' должность:')
            d=str(input())
            t.append(d)
            break
        print('''ФИО: %s
Дата рождения: %s
Логин: %s
Пароль: %s
Должность: %s'''%(t[0]+' '+t[1]+' '+t[2],t[3],t[4],t[5],t[6]))
        g=0
        while True:
            print(txt_m[21])
            o=str(input())
            if o=='да':
                g=1
                break
            elif o=='нет':
                g=0
                break
            else:
                print(txt_m[3])
        if g==1:
            break
        else:
            print(txt_m[20])
            continue
    new_user_info=t[4]+'*;*'+'ФИО: '+t[0]+' '+t[1]+' '+t[2]+'*;*'+'Дата рождения: '+t[3]+'*;*'+'Должность: '+t[6]
    new_user_login=t[4]+'/*/'+t[5]+'/*/1'
    
    a=open('login.txt','r',encoding='utf-8')
    b=a.read()
    b+='\n'+new_user_login
    a.close()
    a=open('login.txt','w',encoding='utf-8')
    a.write(b)
    a.close()
    a=open('info.txt','r',encoding='utf-8')
    b=a.read()
    b+='\n'+new_user_info
    a.close()
    a=open('info.txt','w',encoding='utf-8')
    a.write(b)
    a.close()
