a = {'Найменування': None, 'Кількість': None, 'Ціна': None, 'Виробник': None, 'Дата надходження на склад': None}
A = []
n = int(input('Введіть кількість різних товарів: '))

for i in range(n):
    A.append(a.copy())

for i in range(len(A)):
    A[i]['Найменування'] = input(f'Введіть найменування {i+1}-го товару: ')
    A[i]['Кількість'] = input(f'Введіть кількість {i+1}-го товару: ')
    A[i]['Ціна'] = float(input(f'Введіть ціну {i+1}-го товару: '))
    A[i]['Виробник'] = input(f'Введіть виробника {i+1}-го товару: ')
    A[i]['Дата надходження на склад'] = input(f'Введіть дату надходження на склад {i+1}-го товару: ')
    
all_price = 0

for i in range(len(A)):
    all_price += A[i].get('Ціна')

average_price = all_price/len(A)

print()
print('Товари з ціною, що вище середньої:')
print()
for i in range(len(A)):
    if(A[i].get('Ціна') > average_price):
        for k in A[i]:
            print(f'{k}: {A[i][k]}', end = '; ')
        print()

