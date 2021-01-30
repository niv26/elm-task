import vt
import csv 
import os 
import glob
import json 
dir_path = os.getcwd()
#import psycopg2


# url , status , ts ,  harmless , malicious , suspicious , timeout , undetected 



# read csv file 
# write urls into table 
# test urls 
#


class Vt_operations:
    def __init__(self,api_key):
        self.api_key = api_key 
        self.client = vt.Client(api_key)

    def get_url_status(self, url):
        url_id = vt.url_id(url)
        analysis =  self.client.get_object("/urls/{}", url_id)
        res = json.loads(json.dumps(analysis.last_analysis_stats))
        res['url'] = url 
        return res 

    def get_bulk_url_status(self,url_list):
        bulk_analysis = [] 
        for i in url_list:
            #bulk_analysis[i] = self.get_url_status(i)
            status = self.get_url_status(i) 
            if status:
                print( status )

    def close_conn(self):
        self.client.close()
        

class Db_operations:
    def __init__(self,user,password,dbname, host):
        self.username = username
        self.password = password
        self.database_name = database_name
        self.url = url 
#        try:
#            conn = psycopg2.connect(f"dbname={dbname} user={user} host={host} password={password}")
#            cursor = conn.cursor()
#        except (Exception, psycopg2.Error) as error :
#            if(connection):
#                print("Failed to connect", error)

    #def insert_new_analysis(analysis_res):
        # url , status , ts ,  harmless , malicious , suspicious , timeout , undetected 
       # """ INSERT INTO analysis (url, status, ts , harmless , malicious , suspicious , timeout , undetected ) """


class Csv_operations:
    def __init__(self,path):
         self.path = path 
    
    def csv_files_to_list(self ):
         return ['www.elementor.com','www.textspeier.de']

    
def main():
    vto = Vt_operations('ad285f76ca564203bc98d81fb45bbbd882bdd6928e5b89db97db9a12b76c84f5')
    csvo = Csv_operations('PYTHON-TASK/files/')

    list_of_urls = csvo.csv_files_to_list()
    analysis = vto.get_bulk_url_status(list_of_urls)
    print(analysis)
    vto.close_conn()


main()