# import pandas as pd

# df = pd.read_fwf('/home/ajay/Documents/NLP/NLP_Project/Corpus/Agriculture/HE_Agriculture/eng_agriculture_set1.txt')
# df.to_csv('eng_agriculture_set1.csv')

import csv
import os
import pandas as pd
import re

def txt_to_csv(filename):
    # os.chdir(r'/home/ajay/Documents/NLP/NLP_Project/Corpus/Agriculture/ET_Agriculture')
    os.chdir(r'/home/ajay/Documents/NLP/NLP_Project/Corpus/Entertainment/ET_Entertainment')
    with open(filename, 'r') as in_file:
        stripped = (line.strip() for line in in_file)
        lines = (line.split(",") for line in stripped if line)
        with open(filename[:-4]+".csv", 'w') as out_file:
            writer = csv.writer(out_file)
            #writer.writerow(('ID', 'Text'))
            writer.writerows(lines)


def remove_tokens(filename,new_filename):

    # if not isinstance(csv_path, str):
    #     raise TypeError("csv_path should be of {}".format(str))
    
    token_sanitizer_pattern = r'\\[A-Z.\-_,$()`]{1,}'

    with open(filename, 'r') as csv_file:
        sanitized_buffer = []
        for line in csv_file:
            line = re.sub(token_sanitizer_pattern, '', line)
            sanitized_buffer.append(line)

    #os.chdir(r'/home/ajay/Documents/NLP/NLP_Project/Corpus/Agriculture/ET_Agriculture/Sanitized')
    with open(new_filename, 'w') as fp:
        fp.writelines(sanitized_buffer)


def files_manipulation():
    # os.chdir(r'/home/ajay/Documents/NLP/NLP_Project/Corpus/Agriculture/ET_Agriculture')

    for i in range(1,30 ):


        ##### For Agriculture Set
        
        # os.chdir(r'/home/ajay/Documents/NLP/NLP_Project/Corpus/Agriculture/ET_Agriculture')
        

        # df1=pd.read_csv('eng_agriculture_sanitized_set'+str(i)+'.csv', sep="\t")
        # df2=pd.read_csv('tel_agriculture_sanitized_set'+str(i)+'.csv', sep="\t")
        # result=pd.merge(df1,df2,on='ID')

        # os.chdir(r'/home/ajay/Documents/NLP/NLP_Project/Corpus/Agriculture/ET_Agriculture/Sanitized')
       
        
        # result.to_csv('agriculture_set_'+str(i)+'.csv')
        # # df=pd.read_csv('agriculture_set_'+str(i)+'.csv')
        # # print(df.shape)

        ##### For Entertainment Set
        #print(i)
        os.chdir(r'/home/ajay/Documents/NLP/NLP_Project/Corpus/Entertainment/ET_Entertainment')

        df1=pd.read_csv('eng_entertainment_sanitized_set'+str(i)+'.csv', sep="\t")
        #print(i)
        df2=pd.read_csv('tel_entertainment_sanitized_set'+str(i)+'.csv', sep="\t")
        #print(i)
        
        result=pd.merge(df1,df2,on='ID')

        os.chdir(r'/home/ajay/Documents/NLP/NLP_Project/Corpus/Entertainment/ET_Entertainment/Sanitized')

        result.to_csv('entertainment_set_'+str(i)+'.csv')


def csv_to_txt(filename,output_textfileName1, output_textfileName2):
    df=pd.read_csv(filename)
    English=list(df['Value_x'])
    Telugu=list(df['Value_y'])

    with open(output_textfileName1, 'w') as fp:
        for item in English:
            fp.write("%s\n"%item)
    with open(output_textfileName2, 'w') as fp:
        for item in Telugu:
            fp.write("%s\n"%item)

        

def main():
    
    ##### For Agriculture Set
    
    # for i in range(1,16):
    #     txt_to_csv('tel_agriculture_set'+str(i)+'.txt')
    #     txt_to_csv('eng_agriculture_set'+str(i)+'.txt')
    
    # for i in range(1,16):
    #     remove_tokens('eng_agriculture_set'+str(i)+'.csv', 'eng_agriculture_sanitized_set'+str(i)+'.csv')
    #     remove_tokens('tel_agriculture_set'+str(i)+'.csv', 'tel_agriculture_sanitized_set'+str(i)+'.csv')
    
    # files_manipulation()

    # for i in range(1,16):
    #     csv_to_txt('agriculture_set_'+str(i)+'.csv','eng_agriculture_sanitized_set_'+str(i)+'.txt','tel_agriculture_sanitized_set_'+str(i)+'.txt')


    ##### For Entertainment Set

    for i in range(1,30):
        txt_to_csv('tel_entertainment_set'+str(i)+'.txt')
        txt_to_csv('eng_entertainment_set'+str(i)+'.txt')
        # print(i)
    
    for i in range(1,30):
        remove_tokens('eng_entertainment_set'+str(i)+'.csv', 'eng_entertainment_sanitized_set'+str(i)+'.csv')
        remove_tokens('tel_entertainment_set'+str(i)+'.csv', 'tel_entertainment_sanitized_set'+str(i)+'.csv')
    
    files_manipulation()

    for i in range(1,30):
        csv_to_txt('entertainment_set_'+str(i)+'.csv','eng_entertainment_sanitized_set_'+str(i)+'.txt','tel_entertainment_sanitized_set_'+str(i)+'.txt')


if __name__ == "__main__":
    main()