from pprint import pprint
import csv
from models import pattern,pattern_2,make_uniform_phones, to_list
with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

last_contact_list = []
final_contacts_list = []

make_uniform_phones(contacts_list, last_contact_list)


some_dict = {}
for i in last_contact_list:
    lastname = i[0]
    firstname = i[1]
    surname = i[2]
    organization = i[3]
    position = i[4]
    phone = i[5]
    email = i[6]
    count = 0
    if some_dict.get(lastname) != None:
        some_list = [lastname,firstname,surname,organization,position,phone,email]
        for some_value in some_dict.get(i[0]):
            count += 1
            if some_value != '' and count < 7:
                del some_list[count]
                some_list.insert(count, some_value)
        some_dict[some_list[0]] = some_list[1],some_list[2],some_list[3],some_list[4],some_list[5],some_list[6]
    else:
        some_dict[lastname] = firstname,surname,organization,position,phone,email

to_list(some_dict,final_contacts_list)
        
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(final_contacts_list)

if __name__ == '__main__':
   pass