#### Project Init
```
python3 -m venv dj
. dj/bin/activate
pip install djangorestframework
django-admin startproject DjangoRestApiMongoDB
pip install djongo
```
Note: 
- `pip install pymongo==3.12.1` for avoiding `Database objects do not implement truth value testing or bool()` error!
- `pip install djongo==1.3.3` for solving SQLdecoder error.
  
Follow the [tutorial](https://www.bezkoder.com/django-mongodb-crud-rest-framework/) to do the following steps.

#### MongoDB set up
Follow this [intructions](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-os-x/#std-label-install-with-homebrew) according to your system.
Note: Django 4.0+ has changed some features, be aware!
- Changefrom `django.conf.urls import url` to `from django.urls import re_path` in `urls.py`

```
// MacOS example
brew tap mongodb/brew
brew update
brew install mongodb-community@6.0
brew services start mongodb-community@6.0

// Connect and Use MongoDB
mongotop
```
#### Implement Results.

<table border="0">
 <tr>
    <td>GET a song by id<img src="./imgs/1.png"/></td>
    <td>GET all songs<img src="./imgs/2.png"/></td>
 </tr>
 <tr>
    <td>POST new song<img src="./imgs/3.png"/></td>
    <td>DELETE<img src="./imgs/4.png" /></td>
 </tr>
 <tr>
    <td>GET by Favorite filter<img src="./imgs/5.png"/></td>
    <td>GET name by an input string filter<img src="./imgs/6.png"/></td>
 </tr>
 <tr>
    <td>Before UPDATE<img src="./imgs/7.png"/></td>
    <td>After UPDATE<img src="./imgs/8.png"/></td>
 </tr>

</table>

