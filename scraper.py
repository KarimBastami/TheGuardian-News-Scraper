from bs4 import BeautifulSoup
import requests
import csv

# ---------------------------------------------------------------------------


siteName = "https://www.bbc.com"
sitePrefix = "https://www.bbc"

bbcHtmlFile = requests.get(siteName).text
soupBbcHtmlFile = BeautifulSoup(bbcHtmlFile, "lxml")


for articlesContainer in soupBbcHtmlFile.findAll("div", class_ = "module__content"):

    try:
        articlesList = articlesContainer.find("ul")
        articlesListItems = articlesList.select("li[class *= --]")


        for list in articlesListItems:

            mediaContent = list.find("div", class_ = "media__content")

            try:
                mediaLink = mediaContent.find("a" ,class_ = "media__link")
                articleLinkSuffix = mediaLink["href"].strip()
            except:
                continue
            

            articleLink = ""
            articleTitle = mediaLink.text.strip()


            if (sitePrefix not in articleLinkSuffix):
                articleLink = siteName + articleLinkSuffix

            else:
                articleLink = articleLinkSuffix
            


            print(articleTitle)
            print(articleLink)
            print("----------------------------------------------\n")
    
    except:
        continue




    
    










