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
    return articleTitleList




def getArticlesAuthors(_siteUrl, _sitePrefix, _soupHtmlFile):

    articlesAuthorList = []
    articlesUrls = getArticlesLinks(_siteUrl, _sitePrefix, _soupHtmlFile)
    
    for url in articlesUrls:

        try:
            htmlFile = getHtmlFileFromUrl(url)
            authorOuterContainer = htmlFile.find("div", class_ = "dcr-1aul2ye")
            authorInnerContainer = authorOuterContainer.find("div", class_ = "dcr-q1awta")

            authorTags = authorInnerContainer.findAll("a")

            authorName = ""


            for tag in authorTags:
                authorName += tag.text.strip() + ", " 


            if (authorName == ""):
                authorName = "No Author"

            articlesAuthorList.append(authorName)
            

        except:
            articlesAuthorList.append("No Author")
    
    return articlesAuthorList





def getArticlesText(_siteUrl, _sitePrefix, _soupHtmlFile):

    articleTextlist = []
    articlesUrls = getArticlesLinks(_siteUrl, _sitePrefix, _soupHtmlFile)

    for url in articlesUrls:

        articleText = ""

        try:

            htmlFile = getHtmlFileFromUrl(url)
            articleTextContainer = htmlFile.find("div", class_ = "article-body-commercial-selector")
            articleTextParagraphs = articleTextContainer.findAll("p")

            for p in articleTextParagraphs:
                articleText += p.text.strip()

        except:
            articleText = "No article text content was found"
        

        articleTextlist.append(articleText)

    return articleTextlist




def getArticlesCategories(_siteUrl, _sitePrefix, _soupHtmlFile):

    articleCategoryList = []
    articlesUrls = getArticlesLinks(_siteUrl, _sitePrefix, _soupHtmlFile)

    for url in articlesUrls:

        try:
            htmlFile = getHtmlFileFromUrl(url)
            categoryOuterContainer = htmlFile.find("div", class_ = "dcr-hfp9tp")
            categoryInnerContainer = categoryOuterContainer.find("div", class_ = "dcr-1u8qly9")

            catTags = categoryInnerContainer.findAll("a")

            category = ""


            for tag in catTags:
                category += tag.text.strip() + ", " 


            if (category == ""):
                category = "No category tag found"

            articleCategoryList.append(category)
    
        except:
            articleCategoryList.append("No category tag found") 
    
    return articleCategoryList








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



# for links in getArticlesLinks(siteUrl, sitePrefix, soupHtmlFile):
#     print(links)
#     print("-------------")



# for authors in getArticlesAuthors(siteUrl, sitePrefix, soupHtmlFile):
#     print(authors)
#     print("-------------")
    
    
# for text in getArticlesText(siteUrl, sitePrefix, soupHtmlFile):
#     print(text)
#     print("-------------")


#getArticlesText(siteUrl, sitePrefix, soupHtmlFile)


for tag in getArticlesCategories(siteUrl, sitePrefix, soupHtmlFile):
    print(tag)
    print("-------------")



