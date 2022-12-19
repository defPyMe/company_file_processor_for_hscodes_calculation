from calculate_max_module import calculate_max
from last_two_calc_module import last_two_calc


def dress_f(value):
    if value[1] =="Woven":
       first_two = "6204"
    else:
        first_two = "6104"
    #here the 04 is always woman
    
    #creating a dictionary with materials
    # the below takes the list as the value
    # NEED TO STRIP THE VALUES WE IMPORT
    main_material = calculate_max(value)
   
    evaluating_dresses_material = {
        "polyester": "4300",
        "viscose": "4400",
        "silk": "4910" ,
        "polyamide": "4300",
        "cotton": "4200",
        "cashmere": "4100",
        "virginwool": "4100",
        "linen" : "4990",
        "merinowool" : "4100",
        "acrylic" : "4300", 
        "elastane": "4300",
        "wool": "4100",
        "acetate": "4400",
        "polyurethane": "4300",
        "lyocell": "4400"


    
    }
    result_to_be_passed = []
    if main_material != "":
        return last_two_calc(main_material, evaluating_dresses_material, first_two) + value
    else:
        result_to_be_passed.append("error")
        return ( result_to_be_passed + value[-1:] + value[:-1])