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



'''




import openpyxl
from openpyxl import Workbook

def create_the_output_file():
    wb = Workbook()
    wb.save('balances.xlsx')
create_the_output_file()






# CODICE8 (7)	CODICE10 (8)	MACRO (2)	MICRO(5)	MATERIALS(6)	GENDER(4)	K/W/S(4)
list_ = [['42029291', '153', 'BAGS', 'Woven', 'W', 'Rucksack', 'Textile fibres', '45385118', '45385118SB'], ['42029291', '153', 'BAGS', 'Woven', 'W', 'Rucksack', 'Textile fibres', '45385118', '45385118SB']]
writing_to_file_f('balances.xlsx', list_)'''

'''
def calculate_max(composition):#here we get the list of the different items
    output = {}
    row_index = composition[0]
    output_list = []
    splitted_comp = composition.split(",")
    #splitted_comp = composition[4].split(",")
    print(splitted_comp)
    if len(splitted_comp) == 1:
        main_material = str(splitted_comp)
        main_material = "".join([i.lower() for i in main_material if i.isalpha()])
    else:
        for comp in splitted_comp:
            #["47% Merino Wool",  "19% Silk", "16% Cashmere","11% Alpaca wool", "7% Polyester"]
            number = "".join([letter for letter in comp if letter.isdigit()])
            material = "".join([letter.lower() for letter in comp if letter.isalpha()])
            
            
            if number !="":
                output[int(number)] = material
                #here we pass some info if theere are numbers to evaluate, we can append to the dicctionary 
            else:
                output_list.append(material)
                #append to list and evaluate them based on the type.

            if output!={}:
                main_material = (output[max(output)])
            else:
                main_material =  output_list[0]




        
    print(output) 
    print("---- main material ", main_material)
    #we get the main material for the composition
    
    result_list = [] 
    result_list.append(main_material)
    result_list.append(row_index)
    return result_list



V = "47% Merino Wool,  19% Silk, 16% Cashmere, 11% Alpaca wool, 7% Polyester"
calculate_max(V)



'''




'''




    evaluating_dresses_material_woman_knitted_suit_jacket = {
        "organiccotton": "3200",
        "cotton" :"3200",
        "polyester": "3300",
        "viscose": "3900",
        "silk": "3900" ,
        "polyamide": "3300",
        "cashmere": "3100",
        "virginwool": "3100",
        "linen" : "3900",
        "merinowool" : "3100",
        "acrylic" : "3300", 
        "elastane": "3300",
        "wool": "3100",
        "triacetate" : "3900",
        "acetate": "3900",
        "ramie": "3900",
        "lambskin" : "1000" 
        }

    evaluating_dresses_material_woman_woven_suit = {
        "organiccotton": "1200",
        "cotton" :"1200",
        "polyester": "1300",
        "viscose": "1910",
        "silk": "1990" ,
        "polyamide": "1300",
        "cashmere": "1100",
        "virginwool": "1100",
        "linen" : "1990",
        "merinowool" : "1100",
        "acrylic" : "1300", 
        "elastane": "1300",
        "wool": "1100",
        "triacetate" : "1910",
        "acetate": "1910",
        "ramie": "1990",
        "polyurethane": "1300",
        "alpacawool":"1100",
        "rayon":"1910"
       }

    evaluating_dresses_material_man_knitted_suit = {
        "polyester": "3390",
        "viscose": "3390",
        "silk": "3990" ,
        "polyamide": "3390",
        "cotton": "3200",
        "cashmere": "3100",
        "virginwool": "3100",
        "linen" : "3390",
        "merinowool" : "3100",
        "acrylic" : "3390", 
        "elastane": "3390",
        "wool": "3100",
        "organiccotton": "3200",
        "triacetate" : "3390",
        "acetate": "3390",
        "ramie": "3990",
        "polyacrylic" : "3390",
        "alpacawool":"3100",
        "rayon":"3390",
        "polyurethane":"3390"
        
    }



    evaluating_dresses_material_Woman_woven_co_ord = {
        "polyester": "2380",
        "viscose": "2918",
        "silk": "2990" ,
        "polyamide": "2380",
        "cotton": "2280",
        "cashmere": "2100",
        "virginwool": "2100",
        "linen" : "2990",
        "merinowool" : "2100",
        "acrylic" : "2380", 
        "elastane": "2380",
        "wool": "2100",
        "organiccotton": "2280",
        "triacetate" : "2918",
        "acetate": "2918",
        "ramie": "2990"
    }
    evaluating_dresses_material_man_woven_suit = {

        "polyester": "3390",
        "viscose": "3919",
        "silk": "3990" ,
        "polyamide": "3390",
        "cotton": "3290",
        "cashmere": "3100",
        "virginwool": "3100",
        "linen" : "3990",
        "merinowool" : "3100",
        "acrylic" : "3390", 
        "elastane": "3390",
        "wool": "3100",
        "organiccotton": "3290",
        "triacetate" : "3919",
        "acetate": "3919",
        "ramie": "3990"
    }

    evaluating_dresses_materia_woven_man_Waistcoat = {
        "polyester": "3390",
        "viscose": "3390",
        "silk": "3900" ,
        "polyamide": "3390",
        "cotton": "3290",
        "cashmere": "3900",
        "virginwool": "3900",
        "linen" : "3900",
        "merinowool" : "3900",
        "acrylic" : "3390", 
        "elastane": "3390",
        "wool": "3900",
        "organiccotton": "3290",
        "triacetate" : "3390",
        "acetate": "3390",
        "ramie": "3900",
        "textilefibres": "3900"
    }
    '''


'''
d = {
        "first dict" : {"a":2,
        "b":3 },

        "second dict" : { "a":2,
            "b":4
        }
    }

for p_id, p_info in d.items():
    print("p_id", p_id[p_info])'''

'''
import re
from calculate_max_module import calculate_max

#need to check the different tipes of upper , the evaluation of faux before so that i get what that is 
upper_eval = { "faux": "ru", "rubber" : "ru", "skin":"le","leather":"le", "textile":"te", "te":"fibres" }#in .lower()
#should default if no tgotten 
type_eval = {'lace-upshoesw': "luw", 'pumpsw':"pw", 'loaferm':"lm", 'balletflatsw': "bfw", 'anklebootsw':"abw", 'kneebootsw':"kbw", 'toepostsandalsw':"tpsw", 
                'sandalsw' :"sw", 'trainersm':"tm", 'espadrillesm' :"em", 'loaferw':"lw", 'trainersw':"tw", 'anklebootsm':"abm", 'lace-upshoesm':"lum"}
# foe now i wouldn t add any extra checkings (hard code in the evaluation of rubber/leather --> defaults to rubber)
sole_eval = {"rubber":"r", "pebbled":"r", "leather":"l", "woven":"w", "-": "Nan"}#.lower()
#creating the evaluation string here 

evaluation = ['FOOTWEAR', 'Rubber nubbed sole', 'M', 'Loafer', 'Soft leather, textile', '44498140', '44498140XW', 2]
    #columns_sum = ((str(value[4]+value[3] + value[1])).lower()).replace(" ", "")


#main material is here the upper 
main_material = calculate_max(evaluation)


eval_upper =  ((evaluation[4]).lower()).replace(" ", "")#le
eval_sole = ((evaluation[1]).lower()).replace(" ", "")#r
    #also here we consider the gender
eval_type = (((evaluation[3] + evaluation[2]).lower()).replace(" ", "")).strip()#lm
    #print("eval_type", eval_type)


#lerlm

#evaluates the shoes 
#i i get the l first that is the evaluatio of the first filter if the result is not none
#l = ([i for i in [re.search(fr"{i}", eval_upper) for i in upper_eval] if i!=None])
upper_code = "".join([i.group() for i in [i for i in [re.search(fr"{i}", main_material[0]) for i in upper_eval] if i!=None]])
#we need a function here that evaluates the different main material 








sole_code = "".join([i.group() for i in [i for i in [re.search(fr"{i}", eval_sole) for i in sole_eval] if i!=None]])
type_code = "".join([i.group() for i in [i for i in [re.search(fr"{i}", eval_type) for i in eval_type] if i!=None]])



#now i need to go into the dict
result_of_upper_eval = (upper_eval[upper_code])
result_of_sole_eval = (sole_eval[sole_code])
result_of_type_eval = (type_eval[type_code])


print("final result",  result_of_upper_eval + result_of_sole_eval + result_of_type_eval)

eval_result = result_of_upper_eval + result_of_sole_eval + result_of_type_eval

#-------------------------------working up until no

#UPPER SOLE AND TYPE
#sole = r,l,w,-



'''


'''
# MODIFYING THE DICTIONARY NOW, REMOVING THE FIRST TWO LETTERS (UPPER COMPOSITION so the first element under which thei are)
evaluating_shoes_starting_from_upper = {#first letter is for the sole

    "le" : {
#----------------------------------------------------------leather sole -- should be ok
        "lab":"035119",#leather woman ankle boots
        "llm":"035995",
        "llum":"035995",
        "llw":"035999",
        "lpw":"035999",
        "lluw":"035999",
        "lsw":"039938",
#---------------------------------------------------woven sole
        "wtw":"039998",#woman 
        "wtpsw":"039938",#woman
        "wsw":"039998",#woman
        "wpw":"035999",#woman
        "wabw":"039198",#woman
        "wabm":"03911690",#man 
        "wlm":"039996",
        "":"",
        "":"",
#--------------------------------------------------------- ( - sole) 
        "Nanlm":"039996",
        "Nanlw":"035999",
        "Nanlum":"039996",
        "Nanabw":"039198",
#------------------------------------------------------------- leather/rubber sole
        "rsw ": "039938", #woman
        "rtpsw": "039998",#woman
        "rpw": "039998",#woman
        "rlm": "035995",#man
        "rluw": "039998",#woman
        "rlum": "039996",#man
        "rkbw":"039198",#woman
        "rabw":"03911890", #woman
        "rabm":"03911690", #man
#------------------------------------------------------------------  rubber clated sole
        "rtm":"039996",#man
        "rabw": "035118",#woman
        "rlw":"039998",#woman
        "rkw":"039198", #woman
        "rabm": "039116",#man
        "rlum":"039996", #man
# --------------------------------------------------------------pebbled sole
        "rlm":"039996", #man
#-------------------------------------------------------------- rubber nubbed sole
        "rlm":"039996", #man
#-------------------------------------------------------------------rubber sole
        "rabm":"03919619",#man
        "rabw":"039198",#woman
        "rtw":"039998",#woman
        "rsw":"039938", #woman
        "rpw":"039998",#woman
        "rlw":"039998",#woman
        "rluw":"039998",#woman
        "rtm":"039996"#man

'''

'''#women 029998
    },
    "ru": {#takes into acccount only rubber soles (rubber upper and leather below improbable)
        "rluw" :"029998",##adding the rubber part      
        "rpw" :"029998", #adding the rubber part calculated with the column, shouldn t be the same for the upper
        "rlm":"029996",
        "rbfw":"029998",
        "rkbw":"029190",
        "rtpsw":"029939",
        "rsw":"029998",
        "rtm":"029996",
        "rem":"029996",
        "rlw":"029998",
        "rtw":"029998",
        "rlum":"029996",
        "rabw":"029190", #woman
        "rabm":"029190"

    },

    "te": {#sole??, type??
        "wtw":"041990",#woman
        "wsw":"039998",#woman 
        "wpw":"039911",#woman
        "wtm":"041990",# man
        "wlw":"041990",#woman
        "wabw":"041990"#woman 

    }

}




#THIS IS A FUNCTION NOW SO WE CAN RETURN STUFF


#needs to check the dict now, by getting the first letters in the result
#main material = evaluation result (without the first two) 
# evaluation dictionary 
if eval_result[0:2] in evaluating_shoes_starting_from_upper:
    final_result = "64" + evaluating_shoes_starting_from_upper[eval_result[0:2]][eval_result[2:]]
    print("evaluation-----------------> ", "64"+evaluating_shoes_starting_from_upper[eval_result[0:2]][eval_result[2:]])
    #return  + value[:-1] #main_material, , first_two
    index_plus_result = []
    index_plus_result.append(final_result)
    index_plus_result.append(main_material[1])
    return index_plus_result
else:
    print("problem evaluating the last part in the footwear function")
    return "error"



'''



#PRE VERSIONE


'''#maybe identification with three variables 

    """
     					    SOLE
				leather (l)      rubber (r)

					    TYPE
		ankleboots (ab)     kneeboots (k)     loafer_pumps_lace_up_man (lplm)     loafer_pumps_lace_up_woman (lplw)   
        loafer_textile (lt) sandals_textile (st)


					    UPPER
			textile (t)			leather (le)   rubber/"""



    evaluating_footwear_with_uppers_leather_ankle_boots_woman_leather_sole = { #
        "calfskin": "035119",
        "softleather": "035119",
        "fauxleather":"029190"
    }
    evaluating_footwear_with_uppers_leather_kneeboot_rubber_sole = {#
        "calfskin": "039198",
        "softleather": "039198",
        "textilefibres":" 039998"
    }
    evaluating_footwear_with_uppers_leather_loafer_man_lace_up_shoes_man_leather_sole = {#
        "softleather": "035995"
        
    }
    evaluating_footwear_with_uppers_leather_loafer_pumps__lace_up_shoes_woman_leather_sole = {#
        "softleather": "035999"
    }
    evaluating_footwear_with_uppers_leather_lace_up_shoes_loafer_pumps_woman_rubber_sole = {#rlelplw
        "softleather": "039998",
        "cowhide": "039998",
        "textilefibres":"039998",
        "calfskin": "039998"
    }
    evaluating_footwear_with_uppers_leather_lace_up_shoes_trainers_loafer_man_rubber_sole = {#rlelplm
        "softleather": "039996",
        "calfskin" : "039996",
        "cowhide": "039996",
        "textilefibres":"039996"
        
    }
    evaluating_footwear_with_uppers_textile_loafer_woman_rubber_sole = {#rtlt
        "textilefibres": "041990"
    }

    evaluating_footwear_with_uppers_leather_sandals_woman_rubber_sole = {#rtst
        "softleather": "039938",
        "calfskin": "039938",
        "textilefibres":" 039998"
    }


    #
    evaluating_footwear_with_uppers_textile_trainers_man_woven_sole = {#rtst
        "textilefibres": "039996"
    }

    evaluating_footwear_with_uppers_leather_anklebootsm_man_rubber_sole = {#rtst
        "softleather": "039116"
    }

    #evaluating the different to get a flag 
    #['FOOTWEAR', 'Rubber nubbed sole', 'M', 'Loafer', 'Soft leather', 44498140, '44498140XW']
    #columns_sum = ((str(value[4]+value[3] + value[1])).lower()).replace(" ", "")

    eval_sole = ((value[1]).lower()).replace(" ", "")
    eval_upper =  ((value[1]).lower()).replace(" ", "")
    #also here we consider the gender
    eval_type = (((value[3] + value[2]).lower()).replace(" ", "")).strip()
    #print("eval_type", eval_type)

    sole = ["rubber", "pebbled"]
    sole_woven = ["woven"]
    upper = ["leather", "cowhide", "calfskin"]
    #takes into account also the gender but not for all 
    #trainers for man needs to be added 
    type_dictionary = {"anklebootsw": "ab", "kneebootsw":"k", "loaferm": "lplm", "pumpsm": "lplm", 
    "lace-upshoesm":"lplm", "loaferw": "lplw", "pumpsw": "lplw", "lace-upshoesw":"lplw", "sandalsw": "st", "trainersm": "lplm",
    "trainersw":"lplw", "anklebootsm":"abm" }


    if [re.search(fr"{i}", eval_sole) for i in sole]:
        sole_result = "r"
    elif [re.search(fr"{i}", eval_sole) for i in sole_woven]:
        sole_result = "w"
    else:
        sole_result = "l"



    if [re.search(fr"{i}", eval_upper) for i in upper]:
        upper_result = "le"
        
    else:
        upper_result = "t"


#needs here also to check the gender
    
    





    for i in type_dictionary:
        x = re.search(fr"{i}", eval_type) 
        if x:
            
            dict_result = type_dictionary[x.group()]
            
            result_of_filters = (sole_result + upper_result + dict_result).strip()
            
            break
        else:
            #print("code not found in ---> ", x)
            #print("what we have after first evaluation--> ",sole_result + upper_result )
            result_of_filters = sole_result + upper_result + "NOT FOUNDDDD"
        
            
    
    #print("results of filters , what we will search in the dict -->", result_of_filters )
    #print("what we will look for    ",   )
    #dictionary with the possible result and function calls

    results_funct_calls = {
            "lleab" : evaluating_footwear_with_uppers_leather_ankle_boots_woman_leather_sole,
            "llek": evaluating_footwear_with_uppers_leather_kneeboot_rubber_sole,
            "llelplm" : evaluating_footwear_with_uppers_leather_loafer_man_lace_up_shoes_man_leather_sole ,
            "llelplw" : evaluating_footwear_with_uppers_leather_loafer_pumps__lace_up_shoes_woman_leather_sole ,
            "rlelplw" : evaluating_footwear_with_uppers_leather_lace_up_shoes_loafer_pumps_woman_rubber_sole,
            "rlelplm": evaluating_footwear_with_uppers_leather_lace_up_shoes_trainers_loafer_man_rubber_sole  ,
            "rtlplw": evaluating_footwear_with_uppers_textile_loafer_woman_rubber_sole,
            "rlest" : evaluating_footwear_with_uppers_leather_sandals_woman_rubber_sole,
            "rlek" : evaluating_footwear_with_uppers_leather_kneeboot_rubber_sole,
            "rleab" : evaluating_footwear_with_uppers_leather_ankle_boots_woman_leather_sole,
            "wtab":"",
            "rleabm": evaluating_footwear_with_uppers_leather_anklebootsm_man_rubber_sole,
            "wtlplm": evaluating_footwear_with_uppers_textile_trainers_man_woven_sole,
            "wtst":evaluating_footwear_with_uppers_leather_lace_up_shoes_loafer_pumps_woman_rubber_sole
    }

    
    print(result_of_filters)

    if result_of_filters in results_funct_calls:
        return last_two_calc(main_material, results_funct_calls[result_of_filters], first_two) + value[:-1]
    else:
        print("problem evaluating the last part in the footwear function")
'''
'''
import re
def evaluating_the_sole(result_of_sole_evaluation):
    if "/" in result_of_sole_evaluation:
        split_result = result_of_sole_evaluation.split("/")
        print("split_results", split_result)
        #group returns the match, striung the pòart passed as evaluation 
        sole_valid = "".join([i.string for i in [i for i in [re.search(fr"sole", i) for i in split_result] if i!=None]])
        print(sole_valid)
        return sole_valid
    else:
        print(result_of_sole_evaluation)
        return result_of_sole_evaluation


eval_sole = "leather/rubbersole"
evaluating_the_sole(eval_sole)
'''


value = [0, 1, 2]

def try_return_tuple(value):
    return (value[1], "error")



print(try_return_tuple(value))








