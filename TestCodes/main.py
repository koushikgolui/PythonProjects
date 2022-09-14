# # ts = ['2019-01-01', '2019-01-02', '2019-01-08', '2019-02-01', '2019-02-02', '2019-02-05']
# #
# # from datetime import datetime, timedelta
# # import numpy as np
# #
# # weekly_list = []
# # day_last_processed = ''
# # # weekend_date = datetime.strptime(ts[0], '%Y-%m-%d') + timedelta(days=7)
# # for i in range(len(ts)):
# #     weekend_date = datetime.strptime(ts[i], '%Y-%m-%d') + timedelta(days=7)
# #     days_in_week = []
# #     for j in range(len(ts)):
# #         if datetime.strptime(ts[j], '%Y-%m-%d') < weekend_date and ts[j] not in [item for items in weekly_list for
# #                                                                                  item in items]:
# #             days_in_week.append(ts[j])
# #
# #     if len(days_in_week):
# #         weekly_list.append(days_in_week)
# #
# #
# # print(weekly_list)
#
# # Anagram checking function
#
# def isanagram(str1, str2):
#     set1 = set(str1)
#     print(set1)
#     set2 = set(str2)
#     print(set2)
#     if set1 == set2:
#         return "anagram"
#     else:
#         return "not anagram"
#
# str1 = 'restfull'
# str2 = 'fluster'
# print(isanagram(str1, str2))
#
# # if __name__ == "__main__":
# #     str1 = 'restful'
# #     str2 = 'fluster'
# #     isanagram(str1, str2)
#
#
# def sort_integers(integers):
#     sorted_list = []
#     len_of_array = len(integers) -1
#     for i in range(len_of_array):
#         num = integers[i]
#         for j in range(len_of_array):
#             if num > integers[j]:
#                 num = integers[j]
#         sorted_list.append(i)
#     return sorted_list
#
#
# x = [5, 6, 4, 7, 9, 10, 2]
# print(sort_integers(x))


# import string
#
# alphabets = list(string.ascii_lowercase) + list(string.ascii_lowercase)
#
# alphabets_dict = {}
#
# for i in range(len(alphabets[:26])):
#     alphabets_dict[alphabets[i]] = alphabets[i+2]
#
# string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb\
#  rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
# new_string = []
#
# for letter in string:
#     if letter.isalpha():
#         new_string.append(alphabets_dict[letter])
#     else:
#         new_string.append(letter)
# print("".join(new_string))
#
#
# print(string.maketrans(alphabets_dict))

import math
import os
import random
import re
import sys


# def missingCharacters(s):
#     # Write your code here
#     # Write your code here
#     digits = []
#     alphabets = ['0','1','2','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w', 'x', 'y', 'z']
#
#     missing_chars = [char for char in alphabets if char not in s]
#     final_string = "".join(missing_chars)
#     return final_string5
#
#
# if __name__ == '__main__':
#     # fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     s = input()
#
#     result = missingCharacters(s)
#     print(result)


# for T in range(int(input())):
#     block_size = int(input())
#     lst = [int(i) for i in input().split()]
#     min_index = lst.index(min(lst))
#     left = lst[:min_index]
#     right = lst[min_index:]
#     if left == sorted(left, reverse=True) and right == sorted(right):
#         print("Yes")
#     else:
#         print("No")



# def countitems(lst):
#     dict_count = {}
#     for items in lst.sort():


# lst = [1,2,3,4,5,6,0]
#
# for j in range(1, len(lst)):
#     key_item = lst[j]
#     print(f"key item for iteration {j} is : {key_item}")
#     i = j - 1
#     while i >= 0:
#         if lst[i] > key_item:
#             lst[i], lst[i+1] = lst[i+1], lst[i]
#             print(lst)
#         i -= 1
#     print(f"after iteration {j} is : {lst}")

def return_char(string):
    for char in string:
        return char

# string = "koushik"
# # chars = map(return_char, string)
# # print(list(chars))
#
# print((lambda string: print(string)))

tables = [lambda x: x * 10 for x in range(1, 11)]

for table in tables:
    print(table())

