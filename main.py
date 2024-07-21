import csv
import re
import pprint




pattern = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
substr = r'+7(\2)\3\4\5\6\7'

with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

def phone_list(contacts_list):
    new_contacts_list = list()
    for item in contacts_list:
        new_contact = list()
        full_name_str = ",".join(item[:3])
        result = re.findall(r'(\w+)', full_name_str)
        while len(result) < 3:
            result.append('')
        new_contact += result
        new_contact.append(item[3])
        new_contact.append(item[4])
        phone_pattern = re.compile(pattern)
        changed_phone = phone_pattern.sub(substr, item[5])
        new_contact.append(changed_phone)
        new_contact.append(item[6])
        new_contacts_list.append(new_contact)
    return del_contact(new_contacts_list)

def del_contact(new_contacts_list):
    phone_book = dict()
    for item in new_contacts_list:
        if item[0] in phone_book:
            contact_value = phone_book[item[0]]
            for i in range(len(contact_value)):
                if item[i]:
                    contact_value[i] = item[i]
        else:
            phone_book[item[0]] = item
    return list(phone_book.values())

with open("phonebook.csv", "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerows (phone_list(contacts_list))

    
  









  
  


 
  
