from random import randint

with open("generate/FirstNamesF.txt", encoding="utf-8") as file:
    firstnames = file.read().split()
    file.close()

with open("generate/LastNamesF.txt", encoding="utf-8") as file:
    lastnames = file.read().split()
    file.close()

with open("generate/MiddleNamesF.txt", encoding="utf-8") as file:
    midnames = file.read().split()
    file.close()

fullnames = []

for i in range(0, 100):
    fullname_str = f"{lastnames[randint(0, len(lastnames) - 1)]} " \
                   f"{firstnames[randint(0, len(firstnames) - 1)]} " \
                   f"{midnames[randint(0, len(midnames) - 1)]}"
    fullnames.append(fullname_str)

with open("generate/fman_fullname.txt", "w", encoding="utf-8") as file:
    for i in range(len(fullnames)):
        file.write(fullnames[i])
        file.write("\n")
    file.close()

if __name__ == "__main__":
    print(firstnames)
    print(lastnames)
    print(midnames)
    print(fullnames)
