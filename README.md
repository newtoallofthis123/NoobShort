# NoobShort

NoobShort is a simple url shortener written in python. It is written using the flask module. You can easily use NoobShort as an template to make your own url shortener by deploying it to heroku. NoobShort is open source hecne you are free to use it as you like. If you like, you can clone the github repository and you can directly deploy it. All you have to do is, in the details.txt file, change the application name to your domain. NoobShort utilizes no other external modules except flask. NoobShort generates a random 8 digit string of characters and stores the relation and if it ever has to shorten the same url, it returns the same string.

I wrote NoobShort to practise web development with flask. This is a beginner project. You can go through the code on github. If you want your own instance, clone the repository and initialize using heroku.

# API

The API is quite simple and easy to use. You just have to make a request to https://noob-short.herokuapp.com/api/v1/'url'. You will get a json with 3 parameters: original_url, short_url, time_created. Use them as you like.

Example Response

`{'original_url': 'https://google.com', 'short_url': 'N7OV8mvS', 'time_created': '09:54:01 2021-09-08'}`

### The below example is for python

```python
import requests

page = requests.get("https://noob-short.herokuapp.com/api/v1/https://google.com")

content = page.content

print(f'Shortened Url: {content["short_url"]}')
```

# Deploying

It is quite easy to deploy NoobShort with heroku cli. You have to have a heroku account for this though.

1. Clone the Github Repository

`git clone https://github.com/newtoallofthis123/NoobShort.git`

2. login to heroku cli

`heroku login`

3. Create a new heroku app

`heroku create "app-name"`

4. Initialize Git and Add

`git init
git add .`

5. Commit and Push

`git commit -m "Commit Message"
git push`

6. Wait for Heroku to build and Done.

## Hope You Enjoy NoobShort

# Future

I am still learning flask and in the future, I hope to make NoobShort better

- Add Url Alias [-]
- Add a REST API [-]
- Make Backend Faster
- Improve the UI

Thanks for Using NoobShort
A Project By NoobScience

> NoobScience 
