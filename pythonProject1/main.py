# print("*%10s*" % ("123456789101112") )
import random
import string
#
# s = "element listy {lista[0]} i slownik {slownik[0]} "
#
# print(s.format(lista= [1,2,3],slownik = {0:"asf",1:'assaaaaf'}))
#
# print("|{0:#^6s}|".format("12345"))

import funkcje as f

binary_number = input("podaj regule 0-255: ")
length_of_automat_content = input("podaj dlogosc ciagu: ")
number_of_steps = int(input("podaj ilosc krokow: "))
content = ''.join(random.choice(f.symbols) for i in range(int(length_of_automat_content)))

rule = f.decimal_to_binary_arr(binary_number)


print(rule)
#

while number_of_steps:
    f.check_next_state(content,rule)
    content = f.return_new_automat_content()
    print(content)
    number_of_steps -= 1
