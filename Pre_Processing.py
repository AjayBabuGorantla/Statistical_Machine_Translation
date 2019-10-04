# import pandas as pd

# df = pd.read_fwf('/home/ajay/Documents/NLP/NLP_Project/Corpus/Agriculture/HE_Agriculture/eng_agriculture_set1.txt')
# df.to_csv('eng_agriculture_set1.csv')

import csv
import os
import pandas as pd

def txt_to_csv(filename):
    os.chdir(r'/home/ajay/Documents/NLP/NLP_Project/Corpus/Agriculture/ET_Agriculture')
    with open(filename, 'r') as in_file:
        stripped = (line.strip() for line in in_file)
        lines = (line.split(",") for line in stripped if line)
        with open(filename[:-4]+".csv", 'w') as out_file:
            writer = csv.writer(out_file)
            #writer.writerow(('ID', 'Text'))
            writer.writerows(lines)

def files_manipulation():
    os.chdir(r'/home/ajay/Documents/NLP')
    df1=pd.read_csv('eng_agriculture_set1.csv', sep="\t")
    #print(df1.head(10))
    print(df1.shape)
    #df1.'ID\tValue'.apply(lambda x: pd.Series(str(x).split("\t")))
    
    df2=pd.read_csv('tel_agriculture_set1.csv', sep="\t")
    #print(df2.head(10))
    print(df2.shape)

    df3=pd.read_csv('eng_agriculture_set2.csv', sep="\t")
    print(df3.head(10))
    print(df3.shape)
    
    # df2.sort_values('ID')
    # df2.head

    result=pd.merge(df1,df2,on='ID')
    print(result.head(10))
    print(result.shape)

    result.to_csv('agriculture_set_1.csv')

    for i in range(1,16):
        df1=pd.read_csv('eng_agriculture_set'+str(i)+'.csv')
        df2=pd.read_csv()

def main():
    for i in range(1,16):
        txt_to_csv('tel_agriculture_set'+str(i)+'.txt')
        txt_to_csv('eng_agriculture_set'+str(i)+'.txt')

    files_manipulation()


if __name__ == "__main__":
    main()