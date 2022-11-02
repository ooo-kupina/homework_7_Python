from generate import man_gen, fman_gen, phone_gen, birthday
from random import shuffle
import os


def start():
    gen_id = man_gen.fullnames + fman_gen.fullnames

    shuffle(gen_id)
    phones = phone_gen.phones
    birthdays = birthday.birthdays

    with open("generate_id.csv", "w", encoding="utf-8") as file:
        file.write(f'"id","name","phone","birthday"\n')
        for i in range(len(gen_id)):
            file.write(f'"{i}","{gen_id[i]}","{phones[i]}","{birthdays[i]}"\n')

    if __name__ == "__main__":
        print(man_gen.fullnames)
        print(fman_gen.fullnames)
        print(gen_id)
        print(phones)
        print(len(gen_id))

    os.system("generate_id.csv")


open("generate_id.csv", "r")  # Не получается открыть файл в консоли почему-то.
