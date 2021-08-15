from bs4 import BeautifulSoup
import requests
import csv

# ---------------------------------------------------------------------------


siteName = "https://www.bbc.com"
sitePrefix = "https://www.bbc"

bbcHtmlFile = requests.get(siteName).text
soupBbcHtmlFile = BeautifulSoup(bbcHtmlFile, "lxml")


articlesContainer = soupBbcHtmlFile.find("div", class_ = "module__content")
articlesList = articlesContainer.find("ul", class_ = "media-list")
articlesListItems = articlesList.findAll("li", class_ = "media-list__item")


for list in articlesListItems:
    mediaContent = list.find("div", class_ = "media__content")
    mediaLink = mediaContent.find("a" ,class_ = "media__link")
    articleLinkSuffix = mediaLink["href"]


    articleLink = ""
    articleTitle = mediaLink.text


    if (sitePrefix not in articleLinkSuffix):
        articleLink = siteName + articleLinkSuffix

    else:
        articleLink = articleLinkSuffix
    


    print(articleTitle)
    print(articleLink)
    





    
    










