from generate import man_gen, fman_gen
import random
import time
from random import randrange
from datetime import timedelta
from datetime import datetime


def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


d1 = datetime.strptime('1/1/1945', '%m/%d/%Y')
d2 = datetime.strptime('1/1/2005', '%m/%d/%Y')

birthdays_num = len(man_gen.fullnames + fman_gen.fullnames)
birthdays = []

for i in range(birthdays_num):
    birthdays.append(random_date(d1, d2).strftime("%Y-%m-%d"))

if __name__ == "__main__":
    print(birthdays_num)
    print(birthdays)
