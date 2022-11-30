import pandas as pd 

def process_the_doc(doc):
    read_document = pd.read_excel(doc)
    print("rows and columns --------------> ",read_document.shape)
    '''if "Unnamed: 1" in columns:
        columns.index("Unnamed: 1")=""
    '''
    #read_document.set_axis(['CODICE8','K/W/S', 'CODICE10', 'MACRO', 'MICRO', 'MATERIALS', 'GENDER'], axis=1, inplace=True)
    
    full_dataset = [] 
    count = 0
    #getting all the rows as lists in the dataset
    for i in range(len(read_document)):
        count += 1
        full_dataset.append(list((( str(read_document.loc[i, 'MACRO']).strip(), str(read_document.loc[i, "K/W/S"]).strip(), str(read_document.loc[i, 'GENDER' ]).strip(),
        str(read_document.loc[i, 'MICRO']).strip(), str(read_document.loc[i, 'MATERIALS']).strip(), str(read_document.loc[i, 'CODICE8']).strip(), str(read_document.loc[i, 'CODICE10' ]).strip(), str(count) ))))
    print(full_dataset[-1])
    return full_dataset
    
    
