numbers = [10, 20, 30, 40, 50, 60, 70, 80]
print(f"0. Початковий список: {numbers}")
print(f"1. Додатний індекс [2]: {numbers[2]} | Від'ємний [-1]: {numbers[-1]}")
slice1 = numbers[1:4]     
slice2 = numbers[:5:2]    
slice3 = numbers[::-1]  
print(f"2. Зрізи: \n   Стандарт [1:4]: {slice1}\n   Крок 2 [:5:2]: {slice2}\n   Реверс [::-1]: {slice3}")
numbers.append(90)
print(f"3. Додано 90 в кінець: {numbers} (Довжина: {len(numbers)})")
numbers.insert(0, 5)
print(f"4. Вставлено 5 на початок: {numbers} (Довжина: {len(numbers)})")
numbers[1:3] = [11, 12]
print(f"5. Заміна діапазону [1:3]: {numbers} (Довжина: {len(numbers)})")