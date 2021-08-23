import pymongo
import dns

import scraper



def getUniqueArticleIndices(_titleList, _collection):
    indicesList = []

    for i in range(0, len(_titleList)):
        match = _collection.find_one({"Title": _titleList[i]})

        if (not match):
            indicesList.append(i)
        
    return indicesList
            
        
        




# ----------------------------------- #
# -------------   Main  ------------- #
# ----------------------------------- #

client = pymongo.MongoClient("mongodb+srv://NewsScraper:mrbOkWRipWEGh1Bt@news-cluster.fvtga.mongodb.net/News?retryWrites=true&w=majority")

db = client["News"]
collection = db["TheGuardian"]

# -----------------------------------------------------------------------------------------------



siteUrl = "https://www.theguardian.com/international"
sitePrefix = "https://www.theguardian"

soupHtmlFile = scraper.getHtmlFileFromUrl(siteUrl)


articleTitles = scraper.getArticlesTitles(soupHtmlFile)
articleCategories = scraper.getArticlesCategories(siteUrl, sitePrefix, soupHtmlFile)
articleAuthors = scraper.getArticlesAuthors(siteUrl, sitePrefix, soupHtmlFile)
articleUrls = scraper.getArticlesLinks(siteUrl, sitePrefix, soupHtmlFile)
articleTextContent = scraper.getArticlesText(siteUrl, sitePrefix, soupHtmlFile)


# -----------------------------------------------------------------------------------------------



uniqueArticleIndexList = getUniqueArticleIndices(articleTitles, collection)

for i in range(len(articleTitles)):

    if (i in uniqueArticleIndexList):

        row = {"Title": "", "Category": "", "Author": "", "Url" : "", "Text": ""}

        row["Title"] = articleTitles[i]
        row["Category"] = articleCategories[i]
        row["Author"] = articleAuthors[i]
        row["Url"] = articleUrls[i]
        row["Text"] = articleTextContent[i]

        collection.insert_one(row)

    

