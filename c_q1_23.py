#Поиск по логину
def com23_login(txt_m,k):
    print(txt_m[5])
    login_info=str(input())
    x=0
    a=open('info.txt','r',encoding='utf-8')
    l=open('login.txt','r',encoding='utf-8')
    b=a.readline()
    v=l.readline()
    while b!='':
        p=v.split('/*/')
        c=b.split('*;*')
        if c[0]==login_info and int(p[2])<k:
            x=1
            for i in range (1,len(c)):
                print(c[i])
            break
        b=a.readline()
        v=l.readline()
    if x==0:
        print(txt_m[12])
    a.close()
    l.close()
#Поиск по ФИО
def com23_fio(txt_m,k):
    print(txt_m[6])
    fio_info=str(input())
    fio_info.strip()
    f_i=['****','||||']
    if fio_info.count(' ')==1:
        f_i=fio_info.split()
    s=0
    a=open('info.txt','r',encoding='utf-8')
    l=open('login.txt','r',encoding='utf-8')
    b=a.readline()
    v=l.readline()
    while b!='':
        c=b.split('*;*')
        p=v.split('/*/')
        fio=c[1]
        d=fio.split()
        if ((f_i[1] in fio) and (f_i[0] in fio)) or (fio_info in fio) and int(p[2])<k:
            s+=1
            for i in range(1,len(c)):
                print(c[i])
        b=a.readline()
        v=l.readline()
    if s==0:
        print(txt_m[13])
    a.close()
    l.close()
#Поиск по дню рождения
def com23_dr(txt_m,k):
    m=['январь','февраль','март','апрель','май','июнь','июль','август','сентябрь','октябрь','ноябрь','декабрь']
    print(txt_m[16])
    s=0
    dr_info=str(input())
    if '.' in dr_info:
        dr_i1=dr_info.split('.')
    a=open('info.txt','r',encoding='utf-8')
    j=open('login.txt','r',encoding='utf-8')
    b=a.readline()
    v=j.readline()
    while b!='':
        l=0
        c=b.split('*;*')
        p=v.split('/*/')
        dr_i2=c[2].split()
        dr_i3=dr_i2[2].split('.')
        if dr_info in m:
            n=str(m.index(dr_info)+1)
            if int(n)<10:
                n='0'+str(n)
            if dr_i3[1]==n:
                l=1
        if (dr_info==dr_i2[2] or dr_info==dr_i3[2] or l==1) and int(p[2])<k:
            for i in range(1,len(c)):
                print(c[i])
                s+=1
        b=a.readline()
        v=j.readline()
    if s==0:
        print(txt_m[13])
#Поиск по уровню доступа
def com23_k(txt_m,k):
    print(txt_m[14])
    k_info=str(input())
    logins=[]
    a=open('login.txt','r',encoding='utf-8')
    b=a.readline()
    while b!='':
        c=b.split('/*/')
        if k_info in c[2]:
            logins.append(c[0])
            k_user=c[2]
        b=a.readline()
    a.close()
    if (len(logins)==0) :
        print(txt_m[13])
        pass
    a=open('info.txt','r',encoding='utf-8')
    b=a.readline()
    while b!='':
        c=b.split('*;*')
        if (c[0] in logins) and int(k_user)<k:
            for i in range(1,len(c)):
                print(c[i])
        b=a.readline()
