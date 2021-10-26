""" 

collect facebook pages comments with graph API
this code collect 2 pages data 

"""

from pyfacebook import GraphAPI as gpi
import pandas as pd
import requests
import time
from datetime import datetime




## this functions check if there is more data 
## in teh request and collect it with HTTP request
## it sends request and if there is "next" key in the data it send request with teh valuee 
## else it return the value of the data  
def add_next(data, key):

    try:
        url = data["paging"]["next"]

    except KeyError:
        return data

    new_data = requests.get(url)
    new_data = new_data.json()
    print(key)
    nex = add_next(new_data, key)
    data["data"].extend(nex["data"])

    return data


def main(info):
    comments = []
 

    print("start for {} at time {}".format(info["name"], datetime.now()))
    
    
    start_time = time.time()
    
    ## start apiaccess token
    api = gpi(access_token=info['access_token'])
    print("apiinitialized for {}\n\n".format(info["name"]))

    start = time.time()
    print("start collecting posts for {}\n\n".format(info["name"]))
    posts = api.get_connection(info["id"], connection="posts", limit = 100)
    posts = add_next(posts, "posts")["data"]
    end = time.time()
    print("collecting posts takes: %.3f second" %(end-start))
    
    print("start collecting messing comments for {}\n\n".format(info["name"]))
    start_comment = time.time()
    
    ## collecting cmments for the posts collected
    n = 0
    for i in posts:
        print(n)
        n+=1

        comment = api.get_connection(i["id"], connection="comments", limit = 100)
        comment = add_next(comment, "comment")
        
        ## extends the comments to the list
        comments.extend(comment["data"])
        
    end_comment = time.time()
    print("collecting comments takes: %.3f second" %(end_comment-start_comment))
    
    print("ading {} data to .csv file \n\n".format(info["name"]))
    
    df = pd.DataFrame (comments)
    df.to_csv("{}_coments.csv".format(info["name"]),index = False)
    
    print("data saved with name {}_comments.csv".format(info["name"]))
    
    end_time = time.time()    
    print("full task for {} for collecting {} with their comments takes {} s\n\n\n".format(info["name"], len(comments), end_time -start_time))
    

if __name__ == '__main__':
   
   ## access  token info
   access = {'access_token': 'token',
              'category': 'Education website',
              'category_list': [{'id': 'int', 'name': 'category name'},
               {'id': 'int', 'name': 'category name'}],
              'name': 'page name',
              'id': 'page ID',
              'tasks': ['page Tasks']}
              
        
       main(access)
    
