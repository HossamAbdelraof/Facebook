# Facebook
> facebook projects for Almentor.net internship
#


the perpose of project to collect Facebookk Data (Comments, Reactions, Shares, etc..) to figure the customers interactions on our product 
the nsuggest improvement based on interactions on the posts and ads 

the full project designed in 4 steps

 1- Graph API exploler <br>
 2- Facebook Access token<br>
 3- Gathering data (permission problem) <br>
 4- code <br>

### Graph API exploler 

1- first step to use facebook API is to sign up as devloper at [Facebook for Devlopers](https://developers.facebook.com/)<br>
2- then [create your first app](https://developers.facebook.com/docs/development/create-an-app) to get your access token<br>
3- after that go to [Graph API exploler](https://developers.facebook.com/tools/explorer/) to get access token and collect the data<br>

> the access token is limited for 1h but you can expand access token or get lifelong access token
######
### Get Facebook Access Token
 #### 1- limited access token (1h)
 open [Grahp API exploler](https://developers.facebook.com/tools/explorer/) 
 
 
 ![image](https://user-images.githubusercontent.com/81495150/138315875-4bf1874f-ed74-4843-a535-1afdba81b994.png)
 
  __press on generate access token and continue with your FB account__<br>
  __the access token tool will generate user access token__
  
![image](https://user-images.githubusercontent.com/81495150/138346812-74b93791-df20-4234-8662-a362f1a353da.png)

**you can create page access token for your FB pages from {user or bage} droplist**

![image](https://user-images.githubusercontent.com/81495150/138346889-9d1c07d7-ceee-40f1-9eb5-21ce835b6fb4.png)

this access token is limited for 1h 

 #### 2- lifelong acccess token
 
 **to get lifelong access token open *My Apps* page from main bar in FB devlopers page or visit the page from [Here](https://developers.facebook.com/apps/)**<br>
 choose your app
 
 then frmo teh menu on left select ***Settings*** droplist then choose ***Basic***
 
 ![image](https://user-images.githubusercontent.com/81495150/138348600-061667e2-380e-490c-8426-07034e742962.png)
 
 in the new page copy ***App ID*** and ***App Secret*** 
 
 ![image](https://user-images.githubusercontent.com/81495150/138348857-192569e8-be9f-436e-a36d-8a402d8ac802.png)


the lifelong access token is "***App ID***" + "|" + "***App Secret*** "
 
 

