#importing the tiktok python SDK
from TikTokApi import TikTokApi as tiktok
#import JSON for export of data
import json
#import helper function
from helpers import preprocess
#importing pandas
import pandas as pd

#using sys dependency to extract command line arguments
import sys

def get_data(hashtag):
    #obtaining cookie data (helps to connect to tiktok fr real time scrapping)
    verifyFp = "verify_kxeu8olo_cVc3YZXE_Ur04_416O_B8AV_hIyZWLNT9X8z"
    #setup instance
    api = tiktok.get_instance(custom_verifyFp = verifyFp, use_test_endpoints=True)
    #get data by hashtag
    trending = api.by_hashtag(hashtag)
    #print(trending) 

    #preprocessing data
    flattened_data = preprocess(trending)

    #exporting results to json file
    #with open('export.json', 'w') as f:
    #    json.dump(flattened_data, f)

    #convert preprocessed data to dataframe
    df_test = pd.DataFrame.from_dict(flattened_data, orient='index')
    #converting dataframe to csv
    df_test.to_csv('tiktok_data.csv', index= False)

if __name__ == '__main__': 
    print(sys.argv)
    get_data(sys.argv[1])