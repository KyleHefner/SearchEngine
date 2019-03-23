#Team 36

import os
from bs4 import BeautifulSoup
import lxml
import re
import sqlite3
import numpy
import time
import pickle
import json


    
def create_index():
    Main_folder = "WEBPAGES_RAW"
    Storage_file = "Inverted_index.dmp"
    num_docs = 37500
    webpages = os.listdir(Main_folder)
    time1 = time.time()
    print(webpages)
    inverted_index = {}
    print("Building Inverted_index")
    f = 0
    for folder in webpages:
        if folder != "bookkeeping.json" and folder != "bookkeeping.tsv":
            print(folder)
        
            for filename in os.listdir(Main_folder + "/" + folder):
                
                docid = str(folder) + "/" + str(filename)
                path = Main_folder + "/" + docid
                html = open(path, "r")

                print(path)
                soup = BeautifulSoup(html, "html.parser")

                word_list = re.sub('[^A-Za-z0-9 ]+', ' ', soup.text).lower().split()

                for word in word_list:
                    #if len(word) > 3:
                    if word not in inverted_index:
                        inverted_index[word] = {}  
                        inverted_index[word][docid] = round(float(1/float(len(word_list))),4)
                
                    else:
                        if docid not in inverted_index[word]:
                            inverted_index[word][docid] = round(float(1/float(len(word_list))),4)
                        else:
                            inverted_index[word][docid] += round(float(1/float(len(word_list))),4)
                
            

    time2 = time.time()
    print("DONE in ", time2-time1)
    print ("Now calculating tf-idf")
    time3 = time.time()
    ## now calculating tf-idf
    for word,posting_list in inverted_index.items():
        
        for doc_id,tf in posting_list.items():
            idf = round(numpy.log(num_docs/len(posting_list.keys())),4)
            tf_idf = round(idf*tf,4)
            inverted_index[word][doc_id]= tf_idf


    time4 = time.time()
    print("DONE in ", time4-time3)
    time5 = time.time()
    print("Putting Inverted Index into File")
    dbfile = open(Storage_file, "w")
    pickle.dump(inverted_index,dbfile)
    dbfile.close()
    time6 = time.time()
    print("Done in ", time6-time5)

def load_dictionary():
    print("Putting Inverted Index back into dictionary")
    time7 = time.time()
    dbfile = open("Inverted_index.dmp","r")
    inverted_index = pickle.load(dbfile)
    dbfile.close()
    time8= time.time()
    print("Done in ", time8-time7)
    return inverted_index

def query_index(inverted_index, search_query):
    url_list = []
    search_list = search_query.split()
    list_of_doc={}
    result = {}
    for word in search_list:
        if word in inverted_index:
            list_of_doc[word] = inverted_index[word]

    for w, l in list_of_doc.items():
        for doc,tf in l.items():
            if doc not in result:
                result[doc] = tf
            else:
                result[doc] = result[doc]+tf
                
    result = sorted(result.items(), key = lambda kv:kv[1], reverse = True)
    

    
    with open('bookkeeping.json', 'r') as json_data:
        json_dict = json.load(json_data)
    for docid,tf in result:
        url_list.append(json_dict[docid])
    return url_list


##def user_input():
##    try:
##        query = input("Enter a query: ")
##        return query
##    except:
##        print("Error")
##        return ""

            
def main():
    inverted_index = load_dictionary()
    
    while True:
        word = raw_input("Enter a query: or(quit) to stop ")
        word = word.lower()
        if word !="quit":
            results = query_index(inverted_index, word)

            if len(results) > 20:
                for i in range(20):
                    print (results[i])
            else:
                for i in range(len(results)):
                    print (results[i])
        else:
            break
    
    
if __name__ == '__main__':
    main()

        
    
    
