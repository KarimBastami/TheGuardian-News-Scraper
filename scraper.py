from bs4 import BeautifulSoup
import requests
import csv

# ---------------------------------------------------------------------------



def getHtmlFileFromUrl(url):
    htmlFile = requests.get(url).text
    return BeautifulSoup(htmlFile, "lxml")



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




def getArticlesLinks(_siteUrl, _sitePrefix, _soupHtmlFile):

    articleLinkList = []
    linkContainers = getArticleLinkContainers(_soupHtmlFile)

    for link in linkContainers:
        
        try:
            articleLinkSuffix = link["href"].strip()
        except:
            continue


        articleLink = ""

        if (_sitePrefix not in articleLinkSuffix):
            articleLink = _siteUrl + articleLinkSuffix

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




def getArticlesAuthors(_siteUrl, _sitePrefix, _soupHtmlFile):

    articlesAuthorList = []
    articlesUrls = getArticlesLinks(_siteUrl, _sitePrefix, _soupHtmlFile)
    authorSearchParameters = ["lx-commentary__meta-reporter",
                              "ssrcss-1gg9z89-Contributor",
                              "qa-contributor-name"]

    count = 0

    for url in articlesUrls:
        articlePage = getHtmlFileFromUrl(url)
        author = ""
        
        try:
            authorList = articlePage.findAll("p", class_ = authorSearchParameters)

            for auth in authorList:
                author = auth.text
                
                print(author)
                print(url)
                print("--------------------------------------------------------------------")

            #if (count == 3):
               # break
            #count += 1

        except:
            author = "No Author Found"

            print(author)
            print(url)
            print("--------------------------------------------------------------------")
            
        
        print("--------------------------------------------------------------------")
        print("--------------------------------------------------------------------")
        print("--------------------------------------------------------------------")
        
        articlesAuthorList.append(author)
    
    return articlesAuthorList








# ----------------------------------- #
# -------------   Main  ------------- #
# ----------------------------------- #


siteUrl = "https://www.bbc.com"
sitePrefix = "https://www.bbc"

soupHtmlFile = getHtmlFileFromUrl(siteUrl)


# for titles in getArticlesTitles(soupHtmlFile):
#     print(titles)
#     print("-------------")

# print("")

# for links in getArticlesLinks(siteUrl, sitePrefix, soupHtmlFile):
#     print(links)
#     print("-------------")


getArticlesAuthors(siteUrl, sitePrefix, soupHtmlFile)

    
    










