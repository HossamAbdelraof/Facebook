# Facebook-Comments-Colelctor
collect facebook comments to .csv file

requerments:
> facebook accesstoken 
> page ID
> page name 


install required libraries 
```
pip install python-facebook-sdk
```

to get posts method sends request to get teh posts from page_ID, tehe method takes 2 parameters { limit: int 1 ~ 100,
full: boolean }

```python
posts = api.get_connection(info["id"], connection="posts", limit = n)
```

the limit is the data return limit ; the full is bool if you need to return all the data with add_next function

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

after collecting posts id in array 
loop for every id in the list to collect comments
and set a timer 


```python
 n = 0
    for i in posts:
        print(n)
        n+=1

        comment = api.get_connection(i["id"], connection="comments", limit = 100)
        comment = add_next(comment, "comment")

        comments.extend(comment["data"])
```
this function collect the comments from the posts "collected ealier" and return it 
to collect all comments the method use add_next(): function to collect all the comments 


###

to add comments to DataFrame and save it as csv

```python
 df = pd.DataFrame (comments)
    df.to_csv("{}_coments.csv".format(info["name"]),index = False)
```






     
