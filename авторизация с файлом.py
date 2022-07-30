import commands_q1
c=open('text_m.txt','r',encoding='utf-8')
txt_m=c.read() 
txt_m=txt_m.split('\n')
c.close()
while txt_m.count('')!=0:
    txt_m.remove('')
while True:
    print(txt_m[0])
    login=(str(input()))
    password=(str(input()))
    a=open('login.txt','r',encoding='utf-8')
    d=a.readline()
    while d!='':
        b=d.split('/*/')
        if login==b[0] and password==b[1]:
            print(txt_m[1])
            a.close()
            k=b[2]
            while True:
                print(txt_m[10])
                print(txt_m[15])
                command=str(input())
                if command=='выход':
                    break
                else:
                    commands_q1.choose(login,password,txt_m,command)
            break
        else:
            d=a.readline()
            continue
    try:
        k=k
    except:
        print(txt_m[2])
        a.close()
    else:
        print(txt_m[11])
    finally:
        continue
