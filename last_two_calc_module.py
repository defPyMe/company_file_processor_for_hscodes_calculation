



def last_two_calc(main_material, evaluation, first_two):
    if main_material[0] in evaluation :
        #print(main_material, evaluation, first_two)
        third_two = evaluation[main_material[0]]
        #print("SUCCESSSS    ", first_two + third_two)
    else:
        third_two = "something wrong with the dictionary"
        print("what was passed i the function", main_material, evaluation, first_two)
        print("the evaluation returned", first_two + third_two)
        print("returned value for comparison", main_material)
    result_of_calculation = first_two + third_two
    index_plus_result = []
    index_plus_result.append(result_of_calculation)
    index_plus_result.append(main_material[1])
    
    
    
    return index_plus_result