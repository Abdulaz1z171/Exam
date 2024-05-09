# n42 Aliyev Abdulaziz 

#  1.	Postgresql bazaga python yordamida ulaning . Product nomli jadval yarating  (id,name,price, color,image) . 
import psycopg2
from typing import List



conn = psycopg2.connect(
    database = 'n42',
    host = 'localhost',
    user = 'postgres',
    password = 'temur_1336',
    port = 5432
)


cur = conn.cursor()

create_products_table = '''
    CREATE TABLE IF NOT EXISTS products(
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        price NUMERIC(6,2) NOT NULL,
        color VARCHAR(100) NOT NULL,
        image VARCHAR(255) NOT NULL

    );
'''

cur.execute(create_products_table)
conn.commit()

"""

"""
# 2 Insert_product , select_all_products , update_product,delete_product nomli funksiyalar yarating.
def insert_table(name,price,color,image):
    insert_product_query = '''
        INSERT INTO  products(name,price,color,image)
        VALUES   (%s,%s,%s,%s)
    

                '''
    inser_product_parametres = (name,price,color,image)
    cur.execute(insert_product_query,inser_product_parametres)
    conn.commit()


"""

# 3.Alphabet nomli class yozing .class obyektlarini  iteratsiya qilish imkoni   bo’lsin (iterator).  obyektni for sikli orqali iteratsiya qilinsa 26 ta alifbo xarflari chiqsin


class Alphabet:
    def __init__(self,words:List[str,]):
        self.words = words
        self.count = 0


    def __iter__(self):
        return self
    

    def __next__(self):
        if self.count < len(self.words):
            result = self.words[self.count]
            self.count += 1
            return result
        else:
            raise StopIteration
        

my_alphabet = ['A','B','D','E','F','G','H','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z','SH','CH','NG']
alphabet = Alphabet(my_alphabet)


for i in alphabet:
    print(i)
"""

# 4.	print_numbers va print_leters nomli funksiyalar yarating. 
# prit_numbers funksiyasi (1,5) gacha bo’lgan sonlarni , print_letters esa
#   ‘’ABCDE” belgilarni loop da bitta dan time sleep(1) qo’yib ,parallel 2ta
#  thread yarating.Ekranga parallel ravishda itemlar chiqsin.
#

import time


def print_numbers():
    for i in range(1, 6):
        print(i)
        time.sleep(1)


def print_letters():
    arr = ['ABCD']
    for i in len(arr):
        print(arr[i])
        time.sleep(1)


# thread1 = threading.Thread(target=print_numbers)
# thread2 = threading.Thread(target=print_letters)
#
# start = time.time()

# thread1.start()
# thread2.start()
#
# thread1.join()
# thread2.join()





# 5.	Product nomli class yarating (1 – misoldagi Product ).Product classiga save() nomli object method yarating.Uni vazifasi object attributelari orqali bazaga saqlasin.

class Person:
    def __init__(self,name,price,color,image):
        self.name = name 
        self.price = price
        self.color = color
        self.image = image


    def save(self):
        insert_into_to_product = '''
        INSERT INTO products(name,price,color,image)
        VALUES              (%s,%s,%s,%s);

        '''
        insert_into_params = (self.name,self.price,self.color,self.image)
        cur.execute(insert_into_to_product,insert_into_params)
        conn.commit()




# 6.	DbConnect nomli ContextManager yarating. Va uning vazifasi python orqali PostGresqlga ulanish (conn,cur)

import psycopg2
db_parameters = {
    'host' : 'localhost',
    'database' : 'n42',
    'user' : 'postgres',
    'password' : 'temur_1336',
    'port' : 5432
}

# DbConnect contex manager yaratamiz
class DbConnect:
    def __init__(self,db_parameters):
     
        self.db_parameters = db_parameters
        self.conn = psycopg2.connect(**db_parameters)
    
    def __enter__(self):
        
        self.cur = self.conn.cursor()
        return self.cur

    def __exit__(self,exc_tb,exc_type,exc_val):
        if self.conn and not self.conn.closed:
            self.conn.commit()
            self.conn.close()

    
#7

