import pymongo
import scraper

# ---------------------------------------------------------------------------


def getUniqueArticleIndices(_titleList, _collection):
    indicesList = []

    for i in range(0, len(_titleList)):
        match = _collection.find_one({"Title": _titleList[i]})

        if (not match):
            indicesList.append(i)
        
    return indicesList
            
        
        

def addNewArticlesToDb(_siteUrl, _sitePrefix, _soupHtmlFile, _collection):

    articleTitles = scraper.getArticlesTitles(_soupHtmlFile)
    articleCategories = scraper.getArticlesCategories(_siteUrl, _sitePrefix, _soupHtmlFile)
    articleAuthors = scraper.getArticlesAuthors(_siteUrl, _sitePrefix, _soupHtmlFile)
    articleUrls = scraper.getArticlesLinks(_siteUrl, _sitePrefix, _soupHtmlFile)
    articleTextContent = scraper.getArticlesText(_siteUrl, _sitePrefix, _soupHtmlFile)


    uniqueArticleIndexList = getUniqueArticleIndices(articleTitles, _collection)

    for i in range(len(articleTitles)):

        if (i in uniqueArticleIndexList):

            row = {"Title": "", "Category": "", "Author": "", "Url" : "", "Text": ""}

            row["Title"] = articleTitles[i]
            row["Category"] = articleCategories[i]
            row["Author"] = articleAuthors[i]
            row["Url"] = articleUrls[i]
            row["Text"] = articleTextContent[i]

            _collection.insert_one(row)


    return len(uniqueArticleIndexList)





def getArticlesUsingCategory(_collection, _category):
    return list(_collection.find({"Category": {"$regex": _category}}))
    























    

