# UrlShortenerAPIHandler
This project is related to the first task of YektaNet interview

# Application
In this site, you can convert your url to a shorter url and access it through any client using the api designed for site
 with your own unique token.
 
## First of ALL
To use the site's features, you must first register to receive your personal token.
Registration on the site is possible in two ways:
1. Register through the main page of the site
2. Register through the designed api.

Registration via api:
Send to url below specific form-data: 

- username, email password and password2
```djangourlpath
localhost:8000/api/users/register
```
You can also login using your username and password via the api.

- Note: When you log in to the site through the api, you will be given a new token.

```djangourlpath
localhost:8000/api/users/login
```

Using your url and the "init_url" input, you can get your shorter url through the api:
```djangourlpath
localhost:8000/api/shortener/creat
```

If you have already received the shortened url with your original url, you can get it through the api:
```djangourlpath
localhost:8000/api/shortener/<slug>/
```
Using the following command, you can view all registered urls and filter them as desired according to the following parameters:

- 'init_url', 'short_url', 'device', 'browser'
```djangourlpath
localhost:8000/api/shortener/list
```
## Redirections
In the redirect section of the site, you can see all your shortened URLs and click on each one to be redirected to the main URL.

You can also use the api to redirect to your original url with your truncated urls:
```djangourlpath
localhost:8000/api/shortener/redirections/<slug>/
```
## Filters
In the filter section of the site, you can filter all available addresses by device and browser and their time period.