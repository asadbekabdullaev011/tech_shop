import psycopg2

connection = psycopg2.connect(
    host = 'localhost',
    port = '5432',
    database = 'postgres',
    user = 'postgres',
    password = '1234'
)

cursor = connection.cursor()

def pro():
    print('Добро пожаловать в магазин Мир технологий')
    print('Список наших товаров:')
    cursor.execute('SELECT product_name FROM products')
    connection.commit()
    product = []
    for i in cursor:
        product.append(*i)
    for y in product:
        print(y)
    phone = input('Что вы хотите купить? ')
    if phone in product:
        tel = f"SELECT product_count FROM products WHERE product_name = '{phone}'"
        cursor.execute(tel)
        connection.commit()
        tele_phone1 = cursor.fetchone()
        tele_phone2 = f"SELECT price FROM products WHERE product_name = '{phone}'"
        cursor.execute(tele_phone2)
        connection.commit()
        tele_phone3 = cursor.fetchone()
        print(f"У нас есть {tele_phone1[0]} штук '{phone}'")
        phone2 = int(input("Количество: "))
        tel2 = int(tele_phone3[0]) * int(phone2)
        if phone2 <= tele_phone1[0]:
            count_total = int(tele_phone1[0]) - int(phone2)
            full_name = input("ФИО: ")
            adres = input('Аддрес: ')
            number = int(input('Тел номер: '))
            print(f"""                                  Мир технологий
            ___________________________________________________________
            ФИО: {full_name}
            Имя телефона: {phone}
            Количество: {phone2}
            Общая сумма: {tel2}""")
            query1 = f"UPDATE products SET product_count = {count_total} WHERE product_name = '{phone}'"
            cursor.execute(query1)
            connection.commit()
            query2 = f"INSERT INTO itc (full_name, number, adres, product_name, product_count, total_sum) VALUES('{full_name}', {number}, '{adres}', '{phone}', {phone2}, {tel2})"
            cursor.execute(query2)
            connection.commit()
            cursor.close()
            connection.close()
        else:
            print(f"У нас нету такой '{phone}'")
    else:
        print("В данный время нету такой телефон")

def admin():
    # print("Добавить товар: 1") \nИзменить товар: 2
    num = int(input("Ввод: "))
    if num == 1:
        pro_name = input("product_name: ")
        pro_company = input("company: ")
        pro_count = input("product_count: ")
        pro_price = input("price: ")
        cursor.execute(f"INSERT INTO products (product_name, company, product_count, price) VALUES('{pro_name}','{pro_company}', {pro_count}, {pro_price})")
        connection.commit()
        cursor.execute("SELECT * FROM products")
        connection.commit()
        dat = cursor.fetchall()
        for i in dat:
            print(*i)

while True:
    print("Выберите кто вы?")
    print("Админ: 1\nКлиент: 2")
    n = int(input('Ввод: '))
    if n == 1:
        print("Вы выбрали Админ")
        a = 'abdullaevbek011@gmail.com'
        b = '1234'
        login = input('Введите эл.адрес: ')
        pasword = input('Введите пароль: ')
        if login in a and pasword in b:
            admin()
            break
        connection.commit()
        
    elif n == 2:
        print("Вы выбрали Клиент")
        fullName = input('FullName: ')
        new_email = input('Email: ')
        password = input("Password: ")
        cursor.execute(f"SELECT EMAIL FROM archiv WHERE EMAIL = '{new_email}'")
        data = cursor.fetchall()
        a = []
        for i in data:
            a.append(*i)
        cursor.execute(f"SELECT PASSWORD FROM archiv WHERE EMAIL = '{new_email}'")
        data1 = cursor.fetchall()
        l = []
        for y in data1:
            l.append(*y)
        if new_email not in a:
            if "@" in new_email and \
                new_email.count(".", new_email.index("@")):
                cursor.execute(f"INSERT INTO archiv(first_name, email, password) VALUES \
                ('{fullName}', '{new_email}', '{password}');")
                connection.commit()
                pro()
                break
            else:
                    print("Ошибочная почта")
        else:
            print(f"Существует такой {new_email} аккаунт")
            if password in l:
                pro()
                break
        connection.commit() 
    else:
        print('выберите правильно кто вы!!!')


cursor.close()
connection.close()
