from calculate_max_module import calculate_max
from last_two_calc_module import last_two_calc



def topwear(value):
    #evaluation of man and woman 
    #what about the man here?         
    # !!!!!!!!!!!!!
    #still neeeds some changes when getting the correct number 
    #!!!!!!!!!!!!!
    #moving the evaluation on top
    main_material = calculate_max(value)


    #creating a dictionary with materials
    # the below takes the list as the value
    # NEED TO STRIP THE VALUES WE IMPORT
    #needs a different dictionary if the clothes a r emade for women or men

#BLOUSE SOLO DONNA 

    
    evaluating_dresses_material_woman_knitted = {
        "organiccotton": "1000",
        "cotton" :"1000",
        "polyester": "2000",
        "viscose": "2000",
        "silk": "9030" ,
        "polyamide": "2000",
        "cashmere": "9010",
        "virginwool": "9010",
        "linen" : "9090",
        "merinowool" : "9010",
        "acrylic" : "2000", 
        "elastane": "2000",
        "wool": "9010",
        "triacetate" : "2000",
        "acetate": "2000",
        "ramie": "9050",
        "lyocell":"2000",
        "rayon":"2000"
        }

    evaluating_dresses_material_man_knitted = {
        "organiccotton": "1000",
        "cotton" :"1000",
        "polyester": "2010",
        "viscose": "2090",
        "silk": "9090" ,
        "polyamide": "2010",
        "cashmere": "9010",
        "virginwool": "9010",
        "linen" : "9090",
        "merinowool" : "9010",
        "acrylic" : "2010", 
        "elastane": "2010",
        "wool": "9010",
        "triacetate" : "2090",
        "acetate": "2090",
        "ramie": "9090"
       }

    evaluating_dresses_material_woman_woven_shirt = {
        "polyester": "4000",
        "viscose": "4000",
        "silk": "1000" ,
        "polyamide": "4000",
        "cotton": "3000",
        "cashmere": "2000",
        "virginwool": "2000",
        "linen" : "9090",
        "merinowool" : "2000",
        "acrylic" : "4000", 
        "elastane": "4000",
        "wool": "2000",
        "organiccotton": "3000",
        "triacetate" : "4000",
        "acetate": "4000",
        "ramie": "9010",
        "cupro":"4000",
        "modal":"4000",
        "paper": "9090",
        "ovineleather":"9090",
        "polyurethane":"4000",
        "mulberrysilk":"1000",
        

    }
    evaluating_dresses_material_man_woven = {
        "polyester": "9080",
        "viscose": "3000",
        "silk": "9080" ,
        "polyamide": "9080",
        "cotton": "2000",
        "cashmere": "9080",
        "virginwool": "9080",
        "linen" : "9010",
        "merinowool" : "9080",
        "acrylic" : "9080", 
        "elastane": "9080",
        "wool": "9080",
        "organiccotton": "2000",
        "triacetate" : "3000",
        "acetate": "3000",
        "ramie": "9010",
        "hemp":"9080",
        "modal":"3000",
        "tencel":"3000",
        "nylon":"9080"
    }

    
    if value[1] =="Woven" and value[2] == "W" and (value[3].lower()) in ["shirt", "blouse", "denim shirt", "polo shirt"]:#ok
       first_two = "6206"
       return last_two_calc(main_material, evaluating_dresses_material_woman_woven_shirt, first_two) + value[:-1]
    elif value[1] =="Knitted" and value[2] == "W":#ok
        first_two = "6106"
        return last_two_calc(main_material, evaluating_dresses_material_woman_knitted, first_two) + value[:-1] 
    elif value[1] =="Knitted" and value[2] == "M":#ok for now
        first_two = "6105"
        return last_two_calc(main_material, evaluating_dresses_material_man_knitted, first_two) + value[:-1]
    elif value[1]=="Woven" and value[2]=="M":
        first_two = "6205" #ok for now
        return last_two_calc(main_material, evaluating_dresses_material_man_woven, first_two) + value[:-1]
    elif value[2]=="W" and (value[3].lower()) in ["shirt", "blouse", "denim shirt", "polo shirt"]:
        first_two = "6206"
        return last_two_calc(main_material, evaluating_dresses_material_woman_woven_shirt, first_two) + value[:-1]










        
