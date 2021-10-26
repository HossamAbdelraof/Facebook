# Facebook-graph-api

scrap facebook data [posts, comments, etc] 

using any limited access token and update it every automatically using facebook SDK

requirements
> Facebook developer account 

> pyfacebook SDK

**pip install python-facebook-sdk**

> pandas


**pip install pandas**


the code designed as python class, just create app and you can get posts, posts_ID, comments, comments for specific posts, get lifelong access token(easteregg)

withen creating class app you should have acces_token, page_ID ,user_ID to config the API

```python
def __init__(self,  token, page_ID, user_ID):
        from pyfacebook import GraphAPI
        import pandas as pd
        import requests

        self.page_ID = page_ID
        self.user_ID = user_ID

        self.api = GraphAPI(access_token=token)
```
to get posts method sends request to get teh posts from page_ID, tehe method takes 2 parameters { limit: int 1 ~ 100,
full: boolean }
the limit is the data return limit ; the full is bool if you need to return all the data with add_next function

#### add_next():
```python
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
```
this function takes the data parameter (our returning data) ant the key (the name of data from (posts, comments, etc)

first if checks if there is more data and sends HTTP request to collect them
then it pass the collected data to itself (cycle until no more data) 
after collecting all data we merge it with the parent one until returning to the orignal data 

#### get_posts_id():

```python
def get_posts_id(self, posts):

        id_list = [i["id"] for i in posts["data"]]
        return id_list
```    
thsi function takes posts data and loop for every post int the data and extract teh ID
the post_ID consist of 2 parts 
> **"page_id"_"post_id"**


#### get_comments():
```python
    def get_comments(self):

        self.comments = []

        for ids in self.posts["data"]:

            self.comment = self.api.get_connection(
                object_id=ids["id"], connection="comments")
            self.comment = add_next(self.comment, "comment")["data"]
            self.comments.extend(self.comment)

        return self.comments
```   
this function collect the comments from the posts "collected ealier" and return it 
to collect all comments the method use add_next(): function to collect all the comments 


        
        
