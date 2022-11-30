from calculate_max_module import calculate_max
from last_two_calc_module import last_two_calc

def suits_and_co_f(value):


    main_material = calculate_max(value)
    
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

    evaluating_dresses_material_woman_woven_suit = {
        "polyester": "3390",
        "viscose": "3990",
        "silk": "3390" ,
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
        "rayon":"3390"
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
    evaluating_dresses_material_Woman_woven_co_ord = {

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
        #as dresses we have the difference in knitted and woven
    if value[1] =="Woven" and value[2] == "W" and value[3]=="Suit jacket":
       first_two = "6204"
       return last_two_calc(main_material, evaluating_dresses_material_woman_woven_suit, first_two) + value[:-1]
    elif value[1] =="Woven" and value[2] == "W" and value[3]=="Suit":
        first_two = "6204"
        return last_two_calc(main_material, evaluating_dresses_material_woman_woven_suit, first_two) + value[:-1]
    elif value[1] =="Woven" and value[2] == "W" and value[3]=="Co-ord":
        first_two = "6204"
        return last_two_calc(main_material,evaluating_dresses_material_Woman_woven_co_ord, first_two) + value[:-1]
    elif value[1] =="Knitted" and value[2] == "W" and value[3]=="Suit jacket":
        first_two = "6104"
        return last_two_calc(main_material, evaluating_dresses_material_woman_knitted_suit_jacket, first_two) + value[:-1]
    elif value[1] =="Knitted" and value[2] == "M" and value[3]=="Suit jacket":
        first_two = "6103"
        return last_two_calc(main_material,evaluating_dresses_material_woman_woven_suit, first_two) + value[:-1]
    elif value[1] =="Woven" and value[2] == "M" and value[3]=="Suit jacket":
        first_two = "6203"
        return last_two_calc(main_material,evaluating_dresses_material_Woman_woven_co_ord, first_two) + value[:-1]
    elif value[1] =="Woven" and value[2] == "M" and value[3]=="Waistcoat":
        first_two = "6211"
        return last_two_calc(main_material,evaluating_dresses_materia_woven_man_Waistcoat, first_two) + value[:-1]


