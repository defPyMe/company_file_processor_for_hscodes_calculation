from calculate_max_module import calculate_max
from last_two_calc_module import last_two_calc
import re


## THERE ARE CASES WHEN WE HAVE NO SOLE !!! BUT WOVEN 


def footwear_f(value):
    #print("-----------------entering new evaluation --------------------")
    #print(value)
    first_two = "64"
    main_material = calculate_max(value)
    #maybe identification with three variables 

    """
     					    SOLE
				leather (l)      rubber (r)

					    TYPE
		ankleboots (ab)     kneeboots (k)     loafer_pumps_lace_up_man (lplm)     loafer_pumps_lace_up_woman (lplw)   
        loafer_textile (lt) sandals_textile (st)


					    UPPER
			textile (t)			leather (le)"""



    evaluating_footwear_with_uppers_leather_ankle_boots_woman_leather_sole = { #
        "calfskin": "035119",
        "softleather": "035119",
        "fauxleather":"029998"
    }
    evaluating_footwear_with_uppers_leather_kneeboot_rubber_sole = {#
        "calfskin": "039198",
        "softleather": "039198"
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
        "cowhide": "039996"
        
    }
    evaluating_footwear_with_uppers_textile_loafer_woman_rubber_sole = {#rtlt
        "textilefibres": "041990"
    }

    evaluating_footwear_with_uppers_leather_sandals_woman_rubber_sole = {#rtst
        "softleather": "039938",
        "calfskin": "039938"
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
    upper = ["leather", "cowhide", "calfskin"]
    #takes into account also the gender but not for all 
    #trainers for man needs to be added 
    type_dictionary = {"anklebootsw": "ab", "kneebootsw":"k", "loaferm": "lplm", "pumpsm": "lplm", 
    "lace-upshoesm":"lplm", "loaferw": "lplw", "pumpsw": "lplw", "lace-upshoesw":"lplw", "sandalsw": "st", "trainersm": "lplm",
    "trainersw":"lplw" }


    if [re.search(fr"{i}", eval_sole) for i in sole]:
        sole_result = "r"
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
            "rleab" : evaluating_footwear_with_uppers_leather_ankle_boots_woman_leather_sole
    }

    


    if result_of_filters in results_funct_calls:
        return last_two_calc(main_material, results_funct_calls[result_of_filters], first_two) + value[:-1]
    else:
        print("problem evaluating the last part in the footwear function")
    
    