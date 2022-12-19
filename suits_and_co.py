from calculate_max_module import calculate_max
from last_two_calc_module import last_two_calc

def suits_and_co_f(value):
    print("what we are working with", value)

    main_material = calculate_max(value)

    #['SUITS and CO-ORDS', 'Woven', 'M', 'Suit jacket', '56% Cotton, 40% Polyester, 4% Elastane', '49345802', '49345802TU', '803']



    #evaluating here the gender and the type
    type_gender_eval = {"suitjacketmwoven":"sjmw","suitjacketwwoven":"sjww",
                        "suitjacketmknitted":"sjmk","suitjacketwknitted":"sjwk",
                        "suitjacketm-":"sjm-","suitjacketw-":"sjw-",
                        "suitmwoven":"smw","suitwwoven":"sww",
                        "suitmknitted":"smk","suitwknitted":"swk",
                        "suitm-":"sm-","suitw-":"sw-",
                        "waistcoatwwoven":"www","waistcoatmwoven":"wmw",
                        "waistcoatwknitted":"wwk","waistcoatmknitted":"wmk",
                        "waistcoatw-":"wwNan","waistcoatm-":"wmNan",
                        "co-ordwwoven":"cww", "co-ordwknitted":"cwk"
                        }

    #also here we consider the gender
    eval_type_gender_fabric = (((value[3] + value[2]+ value[1]).lower()).replace(" ", "")).strip()#lm

    if_tygender = "".join([type_gender_eval[i] for i  in  type_gender_eval if i == eval_type_gender_fabric])

    materials_evaluation = {
        "sjmw" : {


        "polyester": "62033390",
        "viscose": "62033919",
        "silk": "62033990" ,
        "polyamide": "62033390",
        "cotton": "62033290",
        "cashmere": "62033100",
        "virginwool": "62033100",
        "linen" : "62033990",
        "merinowool" : "62033100",
        "acrylic" : "62033390", 
        "elastane": "62033390",
        "wool": "62033100",
        "organiccotton": "62033290",
        "triacetate" : "62033919",
        "acetate": "62033919",
        "ramie": "62033990"


        },
        "sjww" : {
        "polyester": "62043390",
        "viscose": "62043919",
        "silk": "62043990" ,
        "polyamide": "62043390",
        "cotton": "62043290",
        "cashmere": "62043100",
        "virginwool": "62043100",
        "linen" : "62043990",
        "merinowool" : "62043100",
        "acrylic" : "62043390", 
        "elastane": "62043390",
        "wool": "62043100",
        "organiccotton": "62043290",
        "triacetate" : "62043919",
        "acetate": "62043919",
        "ramie": "62043990",
        "polyacrylic":"62043390",
        "rayon":"62043919",
        "polyurethane":"62043390"


        },

        "sjmk" : {
        "polyester": "61033300",
        "viscose": "61033900",
        "silk": "61033900" ,
        "polyamide": "61033300",
        "cotton": "61033200",
        "cashmere": "61033100",
        "virginwool": "61033100",
        "alpacawool":"61033100",
        "linen" : "61033900",
        "merinowool" : "61033100",
        "acrylic" : "61033300", 
        "elastane": "6103330",
        "wool": "61033100",
        "organiccotton": "61033200",
        "triacetate" : "61033900",
        "acetate": "61033900",
        "ramie": "61033900",
        "lambskin" : "61031000",


        },

        "sjwk" : {
        "polyester": "61043300",
        "viscose": "61433900",
        "silk": "61043900" ,
        "polyamide": "61043300",
        "cotton": "61043200",
        "cashmere": "61043100",
        "virginwool": "61043100",
        "linen" : "61043900",
        "merinowool" : "61043100",
        "acrylic" : "61043300", 
        "elastane": "61043300",
        "wool": "61043100",
        "organiccotton": "61043200",
        "triacetate" : "61043900",
        "acetate": "61043900",
        "ramie": "61043900"


        },

        "sjm-" : {
        "lambskin":"42031000",
        "softskin":"42031000",
        "softleather":"42031000"

        },

        "sjw-" : {
         "lambskin":"42031000",
        "softskin":"42031000",
        "softleather":"42031000"


        },

        "smw" : {
                
        "polyester": "62033390",
        "viscose": "62033919",
        "silk": "62033990" ,
        "polyamide": "62033390",
        "cotton": "62033290",
        "cashmere": "62033100",
        "virginwool": "62033100",
        "linen" : "62033990",
        "merinowool" : "62033100",
        "mohairwool":"62033100",
        "superswool":"62033100",
        "acrylic" : "62033390", 
        "elastane": "62033390",
        "wool": "62033100",
        "organiccotton": "62033290",
        "triacetate" : "62033919",
        "acetate": "62033919",
        "ramie": "62033990"


        },

        "sww" : {
        "organiccotton": "62041200",
        "cotton" :"62041200",
        "polyester": "62041300",
        "viscose": "62041910",
        "silk": "62041990" ,
        "polyamide": "62041300",
        "cashmere": "62041100",
        "virginwool": "62041100",
        "linen" : "62041990",
        "merinowool" : "62041100",
        "acrylic" : "62041300", 
        "elastane": "62041300",
        "wool": "62041100",
        "triacetate" : "62041910",
        "acetate": "62041910",
        "ramie": "62041990",
        "polyurethane": "62041300",
        "alpacawool":"62041100",
        "rayon":"62041910"

        },



        "smk" : {
        "cotton" :"61033200",
        "polyester": "61033300",
        "viscose": "61033900",
        "silk": "61033900" ,
        "polyamide": "61033300",
        "cashmere": "61033100",
        "virginwool": "61033100",
        "linen" : "61033900",
        "merinowool" : "61033100",
        "acrylic" : "61033300", 
        "elastane": "61033300",
        "wool": "6103100",
        "triacetate" : "61033900",
        "acetate": "6103900",
        "ramie": "61033900",
        "lambskin" : "61031000",
        "alpacawool":"61033100"


        },

        "swk" : {
        "polyester": "61043300",
        "viscose": "61433900",
        "silk": "61043900" ,
        "polyamide": "61043300",
        "cotton": "61043200",
        "cashmere": "61043100",
        "virginwool": "61043100",
        "linen" : "61043900",
        "merinowool" : "61043100",
        "acrylic" : "61043300", 
        "elastane": "61043300",
        "wool": "61043100",
        "organiccotton": "61043200",
        "triacetate" : "61043900",
        "acetate": "61043900",
        "ramie": "61043900"


        },

        "sm-" : {
        "lambskin":"42031000",
        "softskin":"42031000",
        "softleather":"42031000"



        },

        "sw-" : {
        "lambskin":"42031000",
        "softskin":"42031000",
        "softleather":"42031000"



        },

        "www" : {

        "polyester": "",
        "viscose": "",
        "silk": "" ,
        "polyamide": "",
        "cotton": "",
        "cashmere": "",
        "virginwool": "",
        "linen" : "",
        "merinowool" : "",
        "acrylic" : "", 
        "elastane": "",
        "wool": "",
        "organiccotton": "",
        "triacetate" : "",
        "acetate": "",
        "ramie": ""


        },

        "wmw" : {

        "polyester": "62113390",
        "viscose": "62113390",
        "silk": "62113900" ,
        "polyamide": "62113390",
        "cotton": "62113290",
        "cashmere": "62113900",
        "virginwool": "6211390010",
        "linen" : "62113900",
        "merinowool" : "6211390010",
        "acrylic" : "62113390", 
        "elastane": "62113390",
        "wool": "6211390010",
        "organiccotton": "62113290",
        "triacetate" : "6211339090",
        "acetate": "62113390",
        "ramie": "6211390090",
        "textilefibres":"62113900"

        },

        "wwk" : {
       "polyester": "",
        "viscose": "",
        "silk": "" ,
        "polyamide": "",
        "cotton": "",
        "cashmere": "",
        "virginwool": "",
        "linen" : "",
        "merinowool" : "",
        "acrylic" : "", 
        "elastane": "",
        "wool": "",
        "organiccotton": "",
        "triacetate" : "",
        "acetate": "",
        "ramie": ""


        },


        "wmk" : {

        "polyester": "61013010",
        "viscose": "61013010",
        "silk": "6101902090" ,
        "polyamide": "61013010",
        "cotton": "61012010",
        "cashmere": "6101902019",
        "virginwool": "6101902019",
        "linen" : "6101902090",
        "merinowool" : "6101902019",
        "acrylic" : "61013010", 
        "elastane": "61013010",
        "wool": "6101902019",
        "organiccotton": "61012010",
        "triacetate" : "61013010",
        "acetate": "61013010",
        "ramie": "61013010",
        "textilefibres":""




        },


        "wwNan" : {

       "polyester": "",
        "viscose": "",
        "silk": "" ,
        "polyamide": "",
        "cotton": "",
        "cashmere": "",
        "virginwool": "",
        "linen" : "",
        "merinowool" : "",
        "acrylic" : "", 
        "elastane": "",
        "wool": "",
        "organiccotton": "",
        "triacetate" : "",
        "acetate": "",
        "ramie": ""

        },


        "wmNan" : {

       "polyester": "",
        "viscose": "",
        "silk": "" ,
        "polyamide": "",
        "cotton": "",
        "cashmere": "",
        "virginwool": "",
        "linen" : "",
        "merinowool" : "",
        "acrylic" : "", 
        "elastane": "",
        "wool": "",
        "organiccotton": "",
        "triacetate" : "",
        "acetate": "",
        "ramie": ""

        },


        "cww" : {

        "polyester": "62042380",
        "viscose": "62042918",
        "silk": "62042990" ,
        "polyamide": "62042380",
        "cotton": "62042280",
        "cashmere": "62042100",
        "virginwool": "62042100",
        "linen" : "62042990",
        "merinowool" : "62042100",
        "acrylic" : "62042380", 
        "elastane": "62042380",
        "wool": "62042100",
        "organiccotton": "62042280",
        "triacetate" : "62042918",
        "acetate": "62042918",
        "ramie": "62042990"

        },


        "cwk" : {
        "polyester": "61043300",
        "viscose": "61433900",
        "silk": "61043900" ,
        "polyamide": "61043300",
        "cotton": "61043200",
        "cashmere": "61043100",
        "virginwool": "61043100",
        "linen" : "61043900",
        "merinowool" : "61043100",
        "acrylic" : "61043300", 
        "elastane": "61043300",
        "wool": "61043100",
        "organiccotton": "61043200",
        "triacetate" : "61043900",
        "acetate": "61043900",
        "ramie": "61043900"
        }
    }
    result_to_be_passed = []
    index = value[7]
    main_material_firsst_value = main_material[0]
    if if_tygender!=None:
        result_to_be_passed.append(materials_evaluation[if_tygender][main_material_firsst_value])
        result_to_be_passed.append(index)
#needs evaluation of teh suits and co type, like we did with the shoes .. how it is differentiated
#needs to return the index and the result, guess it can be done here 
        return  result_to_be_passed + value[:-1]
    else:
        result_to_be_passed.append("error")
        return ( result_to_be_passed + value[-1:] + value[:-1])


