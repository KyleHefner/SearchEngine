# SearchEngine
Search Engine made in Python

Contains 4 items:
SearchEngine.py, code for executing the Search Engine Program.

WEB_PAGES_RAW directory, raw html data organized in 75 directories, each with 500 unique files containing html pages.

bookkeeping.json, a file with 1 (key, value) pair per line, where key is the location of the html file, ex. "5\300" and value is the url containg that html information. "5/300" www.facebook.com/user/name translates to in directory 5 and file 300 is the html code from this url.

Inverted_index.dmp, a memory dump file that is created from serializing a python dictionary that is used as the Inverted Index. 

Summary:
Broken into two sections: Inverted Index construction and Search Engine technique. 

Inverted Index construction:
The SearchEngine program uses the WEB_PAGES_RAW directory to parse and tokenize the html pages into words and put them into the Inverted_index. For the key,value pairs in the index, key is a unique word, and value is a dictionary of docid, tfidf values for that word in that document. Consider {"Github", {"8/244, 0.15", "3/16", 0.24}}. This is an inverted index containing one word "Github". Github was found in file 244 in directory number 8 and the "relevance" of it is 0.15. "Github" was also found in file 16 directory number with relevance 0.24. after completion of the Inverted Index, it is serialized into Inverted_index.dmp memory file for storage For more information on tfidf values and "relevance", http://www.tfidf.com 

Search Engine technique:
The Search Engine program unserializes the memory file for the index and asks the user for queries to search against it. For multiple word queries, only webpages that contain all words will be returned. The search function ranks each page by tfidf value for each word. It returns the top 20 urls for a given query

                  
NOTE: Inverted_index.dmp and WEB_PAGES_RAW directory are not included due to size restraints. Search Engine program will not run, but can still be viewed
