from csv import reader
import random


# # open file
# with open("HerdMentality.csv", "r", encoding='utf-8') as my_file:
#     # pass the file object to reader()
#     file_reader = reader(my_file)
#     rows = list(file_reader)

#     while(True):

#         num=random.uniform(1, 992)
#         num=int(num)

#         print(rows[num])
#         input("Enter for next card")

def getcard():
    # open file
    with open("HerdMentality.csv", "r", encoding='utf-8') as my_file:
        # pass the file object to reader()
        file_reader = reader(my_file)
        rows = list(file_reader)

        num=random.uniform(1, 992)
        num=int(num)
        print(rows[num][0])
        return rows[num][0]
