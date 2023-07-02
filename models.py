import csv
import re
pattern = r"(\w+)([,]|\s)(\w+)?([,]|\s)(\w+)?[,]?[,]?[,]?(\w+)?[,]([^,]*)?[,]((\+7|8)\s*\W*(\d{3})\W*(\d{3})\W*(\d{2})\W*(\d{2}))?(\s)?(\W*)?((\w+\W)\s(\w+))?\W?[,](.+)?"
pattern_2 = r'[,](\+7\(\)--)[,]'

def make_uniform_phones(contacts_list, last_contact_list):
    for i in contacts_list[1:]:
        a = ','.join(i)
        result = re.sub(pattern, r"\1,\3,\5,\6,\7,+7(\10)\11-\12-\13\14\17\18,\19", a)
        not_correct_number = re.findall(pattern_2, result)
        if not_correct_number != []:
            result = re.sub(pattern_2, r",,", result)
        last_contact_list.append(result.split(','))

def to_list(dict, list):
    for key,values in dict.items():
        some_list = []
        some_list.append(key)
        for value in values:
            some_list.append(value)
        list.append(some_list)