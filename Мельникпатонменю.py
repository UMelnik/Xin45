question = "Задачу какого типа вам необходимо решить?"
print(question)
V1="1)Задача на кодирование информации"
print(V1)
V2="2)Задача на кодирование звука"
print(V2)
V3="3)Задача на кодирование изображения"
print(V3)
n=input("введите номер:")
if (n=="1"):
    print(V1)
    question1 = "Какие данные вам необхдимо найти?"
    print(question1)
    V21="1)I(общее кол-во информиции)"
    print(V21)
    V22="2)N(мощность алфавита)"
    print(V22)
    V23="3)i(информационный вес символа)"
    print(V23)
    V24="4)K(кол-во символов)"
    print(V24)
    n1=input("введите номер или букву:")
    if (n1=="1") or (n1=="I"):
        print(V21)
        question3 = "Какими данными вы располагаете?"
        print(question3)
        V31=("1)N")
        print(V31)
        V32=("2)K")
        print(V32)
        V33=("3)i")
        print(V33)
        N=int(input("N="))
        K=int(input("K="))
        i=int(input("i="))
        print(N)
    if (n1=="2") or (n1=="N"):
        print(V22)
    if (n1=="3") or (n1=="i"):
        print(V23)
    if (n1=="4") or (n1=="K"):
        print(V24)
if (n=="2"):
    print(V2)
if (n=="3"):
    print(V3)

