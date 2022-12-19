from calculate_max_module import calculate_max
from choosing_the_sole import evaluating_the_sole_f
import re


## THERE ARE CASES WHEN WE HAVE NO SOLE !!! BUT WOVEN 


def footwear_f(value):

    main_material = calculate_max(value)
    


#need to check the different tipes of upper , the evaluation of faux before so that i get what that is 
    upper_eval = { "faux": "ru", "rubber" : "ru", "skin":"le","leather":"le", "textile":"te", "te":"fibres" , "cowhide":"le"}#in .lower()
#should default if no tgotten 
    type_eval = {'lace-upshoesw': "luw", 'pumpsw':"pw", 'loaferm':"lm", 'balletflatsw': "bfw", 'anklebootsw':"abw", 'kneebootsw':"kbw", 'toepostsandalsw':"tpsw", 
                'sandalsw' :"sw", 'trainersm':"tm", 'espadrillesm' :"em", 'loaferw':"lw", 'trainersw':"tw", 'anklebootsm':"abm", 'lace-upshoesm':"lum"}
# foe now i wouldn t add any extra checkings (hard code in the evaluation of rubber/leather --> defaults to rubber)
    sole_eval = {"rubber":"r", "pebbled":"r", "leather":"l", "woven":"w", "-": "Nan"}#.lower()
#creating the evaluation string here 


#main material is here the upper 
    main_material = calculate_max(value)
    #eval_upper =  ((value[4]).lower()).replace(" ", "")#le
    eval_sole = ((value[1]).lower()).replace(" ", "")#r
    #also here we consider the gender
    eval_type = (((value[3] + value[2]).lower()).replace(" ", "")).strip()#lm
    #print("eval_type", eval_type)
    eval_sole_cleaned = evaluating_the_sole_f(eval_sole)



    upper_code = "".join([i.group() for i in [i for i in [re.search(fr"{i}", main_material[0]) for i in upper_eval] if i!=None]][0])
#we need a function here that evaluates the different main material 

    sole_code = "".join([i.group() for i in [i for i in [re.search(fr"{i}",  eval_sole_cleaned) for i in sole_eval] if i!=None]])
    type_code = "".join([i.group() for i in [i for i in [re.search(fr"{i}", eval_type) for i in eval_type] if i!=None]])



#now i need to go into the dict
    result_of_upper_eval = (upper_eval[upper_code])
    result_of_sole_eval = (sole_eval[sole_code])
    result_of_type_eval = (type_eval[type_code])


    print("final result",  result_of_upper_eval + result_of_sole_eval + result_of_type_eval)

    eval_result = result_of_upper_eval + result_of_sole_eval + result_of_type_eval


# MODIFYING THE DICTIONARY NOW, REMOVING THE FIRST TWO LETTERS (UPPER COMPOSITION so the first element under which thei are)
    evaluating_shoes_starting_from_upper = {#first letter is for the sole

    "le" : {
#----------------------------------------------------------leather sole -- should be ok
        "labw":"035119",#leather woman ankle boots
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
        #"rlum": "039996",#man
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
        "rem":"035995",

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

#women 029998
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
        "wabw":"041990",
        "rlw":"041990",#woman 
        "wbfw":"039998",
        "wkbw":"041990"
    }

}




#THIS IS A FUNCTION NOW SO WE CAN RETURN STUFF
    result_to_be_passed = []

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
        return index_plus_result + value[:-1]
    else:
        result_to_be_passed.append("error")
        return ( result_to_be_passed + value[-1:] + value[:-1])