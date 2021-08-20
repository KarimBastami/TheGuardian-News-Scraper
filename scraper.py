from bs4 import BeautifulSoup
import requests
import csv

from requests.api import get

# ---------------------------------------------------------------------------



def removeDuplicates(list):
    uniqueList = []

    for item in list:
        if item not in uniqueList:
            uniqueList.append(item)
    
    return uniqueList



def getHtmlFileFromUrl(url):
    htmlFile = requests.get(url).text
    return BeautifulSoup(htmlFile, "lxml")



def getArticleLinkContainers(_soupHtmlFile):
    
    mediaContainers = []

    for articlesContainer in _soupHtmlFile.findAll("div", class_ = "fc-slice-wrapper"):

        try:
            articlesList = articlesContainer.find("ul")
            articlesListItems = articlesList.findAll("li", class_="fc-slice__item")

            for list in articlesListItems:

                try:
                    mediaContent = list.find("h3", class_ = "fc-item__title")
                    mediaLink = mediaContent.find("a" ,class_ = "fc-item__link")
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


    articleLinkList = removeDuplicates(articleLinkList)
    print("No of URLs: ",len(articleLinkList))
    return articleLinkList




def getArticlesTitles(_soupHtmlFile):

    articleTitleList = []
    linkContainers = getArticleLinkContainers(_soupHtmlFile)

    for link in linkContainers:

        try:
            articleTitle = link.find("span", class_ = "js-headline-text").text.strip()
        except:
            continue

        articleTitleList.append(articleTitle)


    articleTitleList = removeDuplicates(articleTitleList)
    print("No of Titles: ", len(articleTitleList))
    return articleTitleList






# def getArticlesAuthors(_siteUrl, _sitePrefix, _soupHtmlFile):

#     articlesAuthorList = []
#     articlesUrls = getArticlesLinks(_siteUrl, _sitePrefix, _soupHtmlFile)
#     authorSearchParameters = ["lx-commentary__meta-reporter",
#                               "ssrcss-1gg9z89-Contributor",
#                               "qa-contributor-name"]

#     count = 0

#     for url in articlesUrls:
#         articlePage = getHtmlFileFromUrl(url)
#         author = ""
        
#         try:
#             authorList = articlePage.findAll("p", class_ = authorSearchParameters)

#             for auth in authorList:
#                 author = auth.text
                
#                 print(author)
#                 print(url)
#                 print("--------------------------------------------------------------------")

#             #if (count == 3):
#                # break
#             #count += 1

#         except:
#             author = "No Author Found"

#             print(author)
#             print(url)
#             print("--------------------------------------------------------------------")
            
        
#         print("--------------------------------------------------------------------")
#         print("--------------------------------------------------------------------")
#         print("--------------------------------------------------------------------")
        
#         articlesAuthorList.append(author)
    
#     return articlesAuthorList






# ----------------------------------- #
# -------------   Main  ------------- #
# ----------------------------------- #


siteUrl = "https://www.theguardian.com/international"
sitePrefix = "https://www.theguardian"

soupHtmlFile = getHtmlFileFromUrl(siteUrl)


# for i in getArticleLinkContainers(soupHtmlFile):
#     print(i.prettify())



# for titles in getArticlesTitles(soupHtmlFile):
#     print(titles)
#     print("-------------")

# print("")

# for links in getArticlesLinks(siteUrl, sitePrefix, soupHtmlFile):
#     print(links)
#     print("-------------")



getArticlesTitles(soupHtmlFile)
getArticlesLinks(siteUrl, sitePrefix, soupHtmlFile)
    
    










