import re
def evaluating_the_sole_f(result_of_sole_evaluation):
    if "/" in result_of_sole_evaluation:
        split_result = result_of_sole_evaluation.split("/")
        #group returns the match, striung the pòart passed as evaluation 
        sole_valid = "".join([i.string for i in [i for i in [re.search(fr"sole", i) for i in split_result] if i!=None]])
        return sole_valid
    else:
        return result_of_sole_evaluation