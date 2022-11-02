from generate import man_gen, fman_gen
from random import randint

opers = ["+7 (915)", "+7 (962)"]

phones_num = len(man_gen.fullnames + fman_gen.fullnames)
phones = []

for i in range(phones_num):
    phones.append(f"{opers[randint(0, len(opers) - 1)]} {randint(202, 999)}-"
                  f"{randint(0, 9)}{randint(0, 9)}-"
                  f"{randint(0, 9)}{randint(0, 9)}")

with open("generate/phones.txt", "w", encoding="utf-8") as file:
    for i in range(len(phones)):
        file.write(f"{phones[i]}\n")

if __name__ == "__main__":
    print(phones)
