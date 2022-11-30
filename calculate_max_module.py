


def calculate_max(composition):#here we get the list of the different items
    output = {}
    row_index = composition[7]
    output_list = []
    splitted_comp = composition[4].split(",")
    if len(splitted_comp) == 1:
        #seems to have solved som eissues 
        main_material = str(splitted_comp)
        #need to remove the digits from here
        main_material = "".join([i.lower() for i in main_material if i.isalpha()])
        #print("---- main material singular", main_material, splitted_comp)
        #print("one material only main material -->", main_material)
    else:
#maybe i can split by isalpha andis digit
#need to check if there are numbers or not 
        #print("splitted comp", splitted_comp)
        #i should be the full lenght of the values in the elements in the split comp
        for comp in splitted_comp:
            #lenght_of_single_comp = len(comp)
            #number = []
            #material = []
            number = "".join([letter for letter in comp if letter.isdigit()])
            material = "".join([letter.lower() for letter in comp if letter.isalpha()])
            #print("what we get in the evaluation of the digits and letters", number, material)
            
    #if we have no numbers but just  two strings for the compositions we should see if it is possible to get
    # a response with either in the dictionary of results by puitting it in a list or something like that 
            
            #print("what we are actually appending top the dict", output)
            if number !="":
                output[number] = material
                #here we pass some info if theere are numbers to evaluate, we can append to the dicctionary 
            else:
                output_list.append(material)
                #append to list and evaluate them based on the type.
            if output!={}:
                main_material = (output[max(output)])
            else:
                main_material =  output_list[0]




        
        
        #print("---- main material plural", main_material)
    #we get the main material for the composition
    #print("main_material, row_index", main_material, row_index)
    result_list = [] 
    result_list.append(main_material)
    result_list.append(row_index)
    return result_list
