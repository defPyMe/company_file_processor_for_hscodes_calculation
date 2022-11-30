#what happens when we have a double value? 
#what happemns when i have two values and no numbers 
# needs to fill in empty spaces as well
from dress import dress_f
from bag import bag_f
from suits_and_co import suits_and_co_f
from last_two_calc_module import last_two_calc
from calculate_max_module import calculate_max
from topwear_module import topwear
from process_the_doc_module import process_the_doc
#from footwear_module import footwear_f
from jewellery_module import jewellery_f
from suits_and_co import suits_and_co_f
from footwear_module import footwear_f
from write_to_output_file import writing_to_file_f
from create_the_output_file import create_the_output_file_f


# HS code internal selection tender - to be shared
#needs the obj created in order to process the doc correctly 
full_dataset = process_the_doc("Copy of C8 PRIO2 Da Calcolare.xlsx")
#print(full_dataset)

#creating the file 
create_the_output_file_f()





#can pass here different arguments 
dress = [dress_f(i) for i in full_dataset if i[0]=="DRESSES"]  
footwear = [footwear_f(i) for i in full_dataset if i[0]=="FOOTWEAR"]  
jewellery = [jewellery_f(i) for i in full_dataset if i[0]=="JEWELLERY and WATCHES"] 
topwear = [topwear(i) for i in full_dataset if i[0]=="TOPWEAR"] 
suits = [suits_and_co_f(i) for i in full_dataset if i[0]=="SUITS and CO-ORDS"]  
bag = [bag_f(i) for i in full_dataset if i[0]=="BAGS"]

'''
all_results = [dress, footwear, jewellery, topwear, suits, bag]
for i in all_results:
    writing_to_file_f("balances.xlsx", i)'''