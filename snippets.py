#input_type = [1, '12% Polyamide, 24% Viscose, 99% Polyester, 89% poly', "gg"]
#input_type = ['BAGS', '-', 'W', 'Handbag', 'Soft Leather', 45402387, '45402387PL']
'''g = input_type[1].split(",")
#remove the goods 
output = {}
#maybe i can split by isalpha andis digit
for i in range(len(g)):
    number = []
    material = []
    number = int("".join([letter for letter in g[i] if letter.isdigit()]))
    material = "".join([letter for letter in g[i] if letter.isalpha()])
    output.update({ number : material })
main_material = (output[max(output)])
'''

#what happens if we have no number?
'''
def calculate_max(composition):#here we get the list of the different items
    output = {}
    splitted_comp = input_type[4].split(",")
    print(len(splitted_comp), splitted_comp)
    if len(splitted_comp) == 1:
        main_material = splitted_comp
        print(main_material)
    else:
#maybe i can split by isalpha andis digit
        for i in range(len(composition)):
            number = []
            material = []
            number = int("".join([letter for letter in composition[i] if letter.isdigit()]))
            material = "".join([letter for letter in composition[i] if letter.isalpha()])
            output.update({ number : material })
    
    if output :
        main_material = (output[max(output)])
    else:
        pass
    return main_material

calculate_max(input_type)
'''
"""main = '100% Polyester'
main = "".join([i for i in main if i.isalpha()])
print(main)"""
'''
import re



value = ['FOOTWEAR ', 'Rubber nubbed sole', 'M', 'Loafer', 'Soft leather', 44498140, '44498140XW']
eval_sole = ((value[1]).lower()).replace(" ", "")
eval_upper =  ((value[4]).lower()).replace(" ", "")
eval_type = ((value[3]).lower()).replace(" ", "")

#n is where to look an dthe base is the word 
base = ["rubber", "pebbled"]

n = eval_sole
x = [re.search(fr"{i}", n) for i in base ]
#x = re.search(fr"{base}", n)
print(x)
print(eval_sole, eval_upper, eval_type)'''
'''import re
value = ['FOOTWEAR', 'Rubber nubbed sole', 'M', 'Loafer', 'Soft leather', 44498140, '44498140XW']

type_dictionary = {"ankleboots": "ab", "kneeboots":"k", "loaferm": "lplm", "pumpsm": "lplm", 
    "lace-upshoesm":"lplm", "loaferw": "lplw", "pumpsw": "lplw", "lace-upshoesw":"lplw" }

eval_type = ((value[3] + value[2]).lower()).replace(" ", "")
print("eval_type", eval_type)




for i in type_dictionary:
    x = re.search(fr"{i}", eval_type) 
    if x:
        print(x)
        sole_result = type_dictionary[x.group()]
        print(sole_result)
    else:
        pass'''

'''
import pandas as pd
read_document = pd.read_excel("Copy of C8 PRIO2 Da Calcolare.xlsx")
full_lenght = read_document.shape
'''









import openpyxl
from openpyxl import Workbook

def create_the_output_file():
    wb = Workbook()
    wb.save('balances.xlsx')
create_the_output_file()






# CODICE8 (7)	CODICE10 (8)	MACRO (2)	MICRO(5)	MATERIALS(6)	GENDER(4)	K/W/S(4)
list_ = [['42029291', '153', 'BAGS', 'Woven', 'W', 'Rucksack', 'Textile fibres', '45385118', '45385118SB'], ['42029291', '153', 'BAGS', 'Woven', 'W', 'Rucksack', 'Textile fibres', '45385118', '45385118SB']]
writing_to_file_f('balances.xlsx', list_)










