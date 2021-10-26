class scrap:

    def __init__(self,  token, page_ID, user_ID):
        from pyfacebook import GraphAPI
        import pandas as pd
        import requests
      
        self.page_ID = page_ID
        self.user_ID = user_ID

        self.api = GraphAPI(access_token=token)

       def get_posts(self, limit=100, full=True):

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

        self.posts = self.api.get_connection(
            object_id=self.page_ID, connection="posts", limit=limit)

        if full:
            self.posts = add_next(self.posts, "posts")
        return self.posts


    def get_posts_id(self, posts):

        id_list = [i["id"] for i in posts["data"]]
        return id_list
    
    def get_comments(self):
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
        
        self.comments = []
        
        for ids in self.posts["data"]:
            
            self.comment = self.api.get_connection(object_id=ids["id"], connection="comments")
            self.comment = add_next(self.comment, "comment")["data"]
            self.comments.extend(self.comment)
    

        return self.comments
        
    def get_post_comments(self, postse):

        for ids in posts["data"]:

            self.comment = "@@@".join(([mess["message"] for mess in self.api.get_connection(
                object_id=ids["id"], connection="comments")["data"]]))
            return self.comment

                
    def return_posts(self):
        return self.posts

    
    def return_comments(self):
        return self.comments


    def get_lifelong_tooken(self, old_token):
        self.access_tokens = self.api.exchange_long_lived_page_access_token(
            self.user_ID, access_token=old_token)["data"]
        print("teh lifelong access tokens is ")
        print(self.access_tokens)
        
        

app = scrap(token='any limited access token',
            page_ID="the page id", user_ID="user id")


