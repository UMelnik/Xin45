p=int(input('Введите p(2<p<=10):'))
print(f'{p}-ичная таблица умножения')
for x in range (1,p-1):
    for y in range (1,p-1):
        z = (x*y//p)*10+(x*y)%p
        print (z,end=' ')
    print()
        
