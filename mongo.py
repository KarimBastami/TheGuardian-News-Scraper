import pymongo
import dns

import scraper




# ----------------------------------- #
# -------------   Main  ------------- #
# ----------------------------------- #


siteUrl = "https://www.theguardian.com/international"
sitePrefix = "https://www.theguardian"

soupHtmlFile = scraper.getHtmlFileFromUrl(siteUrl)



articleTitles = scraper.getArticlesTitles(soupHtmlFile)
articleCategories = scraper.getArticlesCategories(siteUrl, sitePrefix, soupHtmlFile)
articleAuthors = scraper.getArticlesAuthors(siteUrl, sitePrefix, soupHtmlFile)
articleUrls = scraper.getArticlesLinks(siteUrl, sitePrefix, soupHtmlFile)
articleTextContent = scraper.getArticlesText(siteUrl, sitePrefix, soupHtmlFile)




client = pymongo.MongoClient("mongodb+srv://NewsScraper:mrbOkWRipWEGh1Bt@news-cluster.fvtga.mongodb.net/News?retryWrites=true&w=majority")

db = client["News"]
article = db["TheGuardian"]

for i in range(len(articleTitles)):

    row = {"Title": "", "Category": "", "Author": "", "Url" : "", "Text": ""}

    row["Title"] = articleTitles[i]
    row["Category"] = articleCategories[i]
    row["Author"] = articleAuthors[i]
    row["Url"] = articleUrls[i]
    row["Text"] = articleTextContent[i]

    article.insert_one(row)

    

