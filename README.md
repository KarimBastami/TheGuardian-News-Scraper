# News_Scraper
A simple console based webscraper that scrapes articles from TheGuardian.com and uploads them to a MongoDB database

Articles include:
  - Title
  - URL
  - Category
  - Author
  - Text Content

### How To Use:

- Project consists of three files 
  - scraper.py
  - mongo.py
  - main.py
  
- Run main.py in the same directory as the other files and a console based user interface should appear 

- Make sure pymongo, beautiful soup and the request libraries are installed

- There are only two options available at the moment
  - Scrape for new articles: which will check for any articles not already in the database and upload them
  - Query features: which allows you to search for articles based on a certian category "Hurricanes", "Egypt" etc...
  
 
 ### Tools Used:
 - Beautiful Soup & Requests Library
 - MongoDB / pymongo library 
  
  
 ### Future Work:
 - At the moment the scraper only works on the home page of TheGuardian.com and does not support crawling
 - Improve scraping speed as it can take around a minute to fully scrape
 
  
