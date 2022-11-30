from calculate_max_module import calculate_max
from last_two_calc_module import last_two_calc

def jewellery_f(value):
   first_two = "71"
   main_material = calculate_max(value)
    #i should have the row index from the other function 
   #print("(main_material inside the jewel function      ", main_material)
   evaluating_jewels_material = {
        "silver": "131100",
        "metal": "171900",
        "brass": "171900" ,
        "plastic":"1790",
        "leather":"1790",
        "textilefibres":"1790",
        "softleather":"1790",
        "glass":"1790",
        "stainlesssteel": "171900"
    }

   return last_two_calc(main_material, evaluating_jewels_material, first_two) + value[:-1]



