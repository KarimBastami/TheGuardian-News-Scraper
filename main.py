import pymongo
import mongo
import scraper

# ---------------------------------------------------------------------------


def initializeUserInterface():
    print("")
    print("# ----------------------- #")
    print("# ------ Main Menu ------ #")
    print("# ----------------------- #")
    print("")
    print("0: Scrape New Articles")
    print("1: Search For Articles")
    print("--------------------------")
    print("")



# ----------------------------------- #
# -------------   Main  ------------- #
# ----------------------------------- #

client = pymongo.MongoClient("mongodb+srv://NewsScraper:mrbOkWRipWEGh1Bt@news-cluster.fvtga.mongodb.net/News?retryWrites=true&w=majority")

db = client["News"]
collection = db["TheGuardian"]


siteUrl = "https://www.theguardian.com/international"
sitePrefix = "https://www.theguardian"

soupHtmlFile = scraper.getHtmlFileFromUrl(siteUrl)

# ------------------------------------------------------------------------------------------------------------


initializeUserInterface()

choice = input("Enter your choice (0 - 1): ")

if (choice == "0"):

    print("Scraping in progress...")
    uniqueArticlesCount = mongo.addNewArticlesToDb(siteUrl, sitePrefix, soupHtmlFile, collection)
    print("")
    print(uniqueArticlesCount, "new articles found! uploading to database now....\n")
    
elif (choice == "1"):

    categoryInput = input("\nEnter category criteria: ")
    filteredArticlesList = mongo.getArticlesUsingCategory(collection, categoryInput)

    if (len(filteredArticlesList) > 0):

        for element in filteredArticlesList:
            print("\n\n---------------------------------------------------------------------------------------------")
            print("Title:", element["Title"])
            print("\nCategory:", element["Category"])
            print("\nAuthor:", element["Author"])
            print("\nUrl:", element["Url"])
            print("\nText Content:\n\n" + element["Text"])
            print("---------------------------------------------------------------------------------------------\n")
    else:
        print("\nNo articles with a category of", categoryInput, "found!\n")

else:
    print("")
    print("Please select a valid option (0-1) \n")