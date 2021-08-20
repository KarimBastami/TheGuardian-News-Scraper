from bs4 import BeautifulSoup
import requests
import csv

# ---------------------------------------------------------------------------


siteName = "https://www.bbc.com"
sitePrefix = "https://www.bbc"

htmlFile = requests.get(siteName).text
soupHtmlFile = BeautifulSoup(htmlFile, "lxml")



def getArticleLinkContainers(_soupHtmlFile):
    
    mediaContainers = []

    for articlesContainer in _soupHtmlFile.findAll("div", class_ = "module__content"):

        try:
            articlesList = articlesContainer.find("ul")
            articlesListItems = articlesList.select("li[class *= --]")


            for list in articlesListItems:

                mediaContent = list.find("div", class_ = "media__content")

                try:
                    mediaLink = mediaContent.find("a" ,class_ = "media__link")
                except:
                    continue
                
                
                mediaContainers.append(mediaLink)

        except:
            continue
    
    return mediaContainers




def getArticlesLinks(_siteName, _sitePrefix, _soupHtmlFile):

    articleLinkList = []
    linkContainers = getArticleLinkContainers(_soupHtmlFile)

    for link in linkContainers:
        
        try:
            articleLinkSuffix = link["href"].strip()
        except:
            continue


        articleLink = ""

        if (_sitePrefix not in articleLinkSuffix):
            articleLink = _siteName + articleLinkSuffix

        else:
            articleLink = articleLinkSuffix
        

        articleLinkList.append(articleLink)

    return articleLinkList




def getArticlesTitles(_soupHtmlFile):

    articleTitleList = []
    linkContainers = getArticleLinkContainers(_soupHtmlFile)

    for link in linkContainers:

        try:
            articleTitle = link.text.strip()
        except:
            continue

        articleTitleList.append(articleTitle)

    return articleTitleList




# ----------------------------------- #
# ------------- Testing ------------- #
# ----------------------------------- #

for titles in getArticlesTitles(soupHtmlFile):
    print(titles)
    print("-------------")

print("")

for links in getArticlesLinks(siteName, sitePrefix, soupHtmlFile):
    print(links)
    print("-------------")



    
    










