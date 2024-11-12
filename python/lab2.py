from tabulate import tabulate

def display_menu():
    print("\nМеню:")
    print("1. Добавить автомобиль")
    print("2. Посмотреть все автомобили")
    print("3. Изменить информацию об автомобиле")
    print("4. Удалить автомобиль")
    print("5. Поиск автомобиля")
    print("6. Выход из приложения")
    print("ooo BSL CORPoration12356")
def main():
    file_name = 'cars.txt'
    
    while True:
        display_menu()
        choice = input("Выберите опцию: ")

        if choice == '1':
            add_car(file_name)
        elif choice == '2':
            view_cars(file_name)
        elif choice == '3':
            modify_car(file_name)
        elif choice == '4':
            delete_car(file_name)
        elif choice == '5':
            search_car(file_name)
        elif choice == '6':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

def add_car(file_name):
    print("После того как вы написали марку и т.д автомобиля - нажмите ENTER без пробела.")

    brand = input("Введите марку автомобиля: ")
    if len(brand) == 0:
        print("Поле не должно быть пустым!")
        return

    factory = input("Введите завод автомобиля: ")
    if len(factory) == 0:
        print("Поле не должно быть пустым")
        return

    color = input("Введите цвет: ")
    if len(color) == 0:
        print("Поле не должно быть пустым")
        return

    kpp = input("Введите тип КПП: ")
    if len(kpp) == 0:
        print("Поле не должно быть пустым")
        return

    engine = input("Введите тип двигателя: ")
    if len(engine) == 0:
        print("Поле не должно быть пустым")
        return

    with open(file_name, 'a') as file:
        file.write(f"{brand},{factory},{color},{kpp},{engine}\n")

    print("Автомобиль добавлен.")

def view_cars(file_name):
    try:
        with open(file_name, 'r') as file:
            cars = file.readlines()

        if not cars:
            print("Нет автомобилей для отображения.")
        else:
            print("\nСписок автомобилей:")
            table_data = [[index + 1] + car.strip().split(',') for index, car in enumerate(cars)]
            print(tabulate(table_data, headers=["№", "Марка", "Завод", "Цвет", "Тип КПП", "Двигатель"], tablefmt="grid"))

    except FileNotFoundError:
        print("Файл не найден.")

def modify_car(file_name):
    view_cars(file_name)
    try:
        car_index = int(input("Введите номер автомобиля для изменения: ")) - 1
        with open(file_name, 'r') as file:
            cars = file.readlines()

        if car_index < 0 or car_index >= len(cars):
            print("Неверный номер автомобиля.")
            return

        brand = input("Введите марку автомобиля: ")
        if len(brand) == 0:
            print("Поле не должно быть пустым!")
            return

        factory = input("Введите завод автомобиля: ")
        if len(factory) == 0:
            print("Поле не должно быть пустым")
            return

        color = input("Введите цвет: ")
        if len(color) == 0:
            print("Поле не должно быть пустым")
            return

        kpp = input("Введите тип КПП: ")
        if len(kpp) == 0:
            print("Поле не должно быть пустым")
            return

        engine = input("Введите тип двигателя: ")
        if len(engine) == 0:
            print("Поле не должно быть пустым")
            return

        cars[car_index] = f"{brand},{factory},{color},{kpp},{engine}\n"

        with open(file_name, 'w') as file:
            file.writelines(cars)
                
        print("Информация об автомобиле обновлена.")

    except ValueError:
        print("Введите корректный номер автомобиля.")
    except FileNotFoundError:
        print("Файл не найден.")

def delete_car(file_name):
    view_cars(file_name)
    try:
        car_index = int(input("Введите номер автомобиля для удаления: ")) - 1
        with open(file_name, 'r') as file:
            cars = file.readlines()
            
        if car_index < 0 or car_index >= len(cars):
            print("Неверный номер автомобиля.")
            return

        del cars[car_index]

        with open(file_name, 'w') as file:
            file.writelines(cars)

        print("Автомобиль удален.")
    except ValueError:
        print("Введите корректный номер автомобиля.")
    except FileNotFoundError:
        print("Файл не найден.")

def search_car(file_name):
    search_term = input("Введите марку или завод автомобиля для поиска: ").lower()
    try:
        with open(file_name, 'r') as file:
            cars = file.readlines()

        found = False
        table_data = []
        for index, car in enumerate(cars):
            if search_term in car.lower():
                table_data.append([index + 1] + car.strip().split(','))
                found = True
        
        if found:
            print("\nНайденные автомобили:")
            print(tabulate(table_data, headers=["№", "Марка", "Завод", "Цвет", "Тип КПП", "Двигатель"], tablefmt="grid"))
        else:
            print("Автомобили не найдены.")

    except FileNotFoundError:
        print("Файл не найден.")

if __name__ == "__main__":
    main()