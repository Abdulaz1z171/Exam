import psycopg2
from typing import List
"""
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


# for i in alphabet:
#     print(i)


# 4.	print_numbers va print_leters nomli funksiyalar yarating. 
# prit_numbers funksiyasi (1,5) gacha bo’lgan sonlarni , print_letters esa
#   ‘’ABCDE” belgilarni loop da bitta dan time sleep(1) qo’yib ,parallel 2ta
#  thread yarating.Ekranga parallel ravishda itemlar chiqsin.
#
from decimal import Decimal

def print_numbers(n:int):
    for i in range(n):
        return i

    
def print_letters(letter:str):
    for i in len(letter):
        print(letter[i])
    
print_letters('absd')


