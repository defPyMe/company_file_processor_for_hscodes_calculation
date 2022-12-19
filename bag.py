from calculate_max_module import calculate_max
from last_two_calc_module import last_two_calc

def bag_f(value):
    first_two = "4202"
    main_material = calculate_max(value)
    evaluating_shoulderbag_handbag_crossbodybog_material_man = {
        "leather": "2100",
        "calfskin": "2100",
        "sheepskin": "2100",
        "softleather": "2100",
        "goatskin": "2100",
        "cowhide": "2100",
        "textilefibres": "2290",
        "polyamide": "2290",
        "polyester": "2290",
        "Polyurethane": "2210",
        "pvcpolyvinylchloride": "2210",
        "cotton": "2290",
        "polyurethane": "2210",
        "shearling": "2100"

    }
    evaluating_rucksack = {
        "leather": "9100",
        "calfskin": "9110",
        "sheepskin": "9110",
        "softleather": "9110",
        "goatskin": "9110",
        "cowhide": "9110",
        "textilefibres": "9291",
        "polyamide": "9291",
        "polyester": "9291",
        "nylon": "9291",
        "": "",
        "": "",
        "": "",
        "": ""

    }
    result_to_be_passed = []

    if value[3] in ["Shoulder bag", "Cross-body bag", "Handbag"]:
        first_two = "4202"
        return last_two_calc(main_material, evaluating_shoulderbag_handbag_crossbodybog_material_man, first_two) + value[:-1]
    elif value[3]=="Rucksack":
        first_two = "4202"
        return last_two_calc(main_material, evaluating_rucksack, first_two) + value[:-1]
    else:
        result_to_be_passed.append("error")
        return ( result_to_be_passed + list(reversed(value)))
    