import pprint
import csv
import re




#text ="phonebook_raw.csv"
pattern = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
substr = r'+7(\2)\3\4\5\6\7'
# pattern = r"^(\+7|8)(\s?)(\(?)([0-9]{3})(\)?)(\s?)(\-?)([0-9]{3})(\s?)(\-?)(\d{2})(\s?)(\-?)(\d{2})(\s?)(\(?)|[а-о]+(\.?)(\s?)([0-9]{4})"
# substr = r"+7(\4)\8\11\14"
#pattern = re.sub(pattern, substr, text)

with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

def phone(contact_list: list):
  list_new = list()
  for item in contact_list:
        full_name = ' '.join(set(item[:2])).split(' ') 
        result = [full_name[0], full_name[1], full_name[2], item[3], item[4],
                re.sub(pattern, substr, item[5]), 
                item[6]]                 
        list_new.append(result)
  return new_list_name(list_new)

def new_list_name(contacts: list):
    for contact in contacts:
        firstname = contact[0]
        lastname = contact[1]
        for new_contact in contacts:
            new_last_name = new_contact[0]
            new_first_name = new_contact[1]
            if firstname == new_first_name and lastname == new_last_name:
                if contact[2] == "": contact[2] = new_contact[2]
                if contact[3] == "": contact[3] = new_contact[3]
                if contact[4] == "": contact[4] = new_contact[4]
                if contact[5] == "": contact[5] = new_contact[5]
                if contact[6] == "": contact[6] = new_contact[6]
    result_list = list()
    for new_contact_list in contacts:
        if new_contact_list not in result_list:
            result_list.append(new_contact_list)
    return result_list

with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(phone(contacts_list))
  



 
  
