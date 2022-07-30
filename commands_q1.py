def choose(login,password,txt_m,command):
    '''Посмотреть информацию о пользователях(23)
        Создание нового пользователя(37)
        Изменить уровень/удаления пользователя(44)'''
    import c_q1_23
    import c_q1_37
    import c_q1_44
    f=['23','37','44']
    g=['0','1','2','3','4','5','6','7','8','9']
    #isdigit
    '''n=0
    for i in txt_m:
        while True:
            for w in txt_m:
                if w==i:
                    break
                n+=1
        for j in i:
            if j in g:
                x=i[1:]
                txt_m.insert(n,x)
    print(txt_m)'''
    while True:
        a=open('login.txt','r')
        b=a.readline()
        while b!='':
            c=b.split('/*/')
            if c[0]==login:
                k=c[2]
                k=k[:1]
                k=int(k)
                break
            b=a.readline()
        a.close()
        if command=='23' and k>1:
            while True:
                print(txt_m[9])
                print(txt_m[17])
                command=str(input())
                if command=='логин':
                    c_q1_23.com23_login(txt_m,k)
                elif command=='доступ':
                    c_q1_23.com23_k(txt_m,k)
                elif command=='фио':
                    c_q1_23.com23_fio(txt_m,k)
                elif command=='дата рождения':
                    c_q1_23.com23_dr(txt_m,k)
                elif command=='выход':
                    return
                else:
                    print(txt_m[3])
                    continue
        elif command=='37' and k>2:
            c_q1_37.com37_nu(txt_m)
            return
        elif command=='44' and k>=3:
            while True:
                print(txt_m[27])
                print(txt_m[17])
                command=str(input())
                if command=='изменить уровень':
                    c_q1_44.com44_chk(txt_m,k)
                elif (command=='удалить пользователя' or command=='19') and k==4:
                    c_q1_44.com44_du(txt_m,k)
                elif command=='выход':
                    return
                else:
                    print(txt_m[3])
                    continue
        elif command not in f:
            print(txt_m[3])
            break
        else:
            print(txt_m[4])
            break

                
    
    
