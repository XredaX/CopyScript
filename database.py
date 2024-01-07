import pymongo

passd = "ckZpYU8HGpnc5i9i"
named = "CopySys"

client = pymongo.MongoClient("mongodb+srv://test:"+passd+"@cluster1.9glic.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.get_database(named)

class user():
    def findsession(collection, Owenr):
        collection = db[collection]
        session = {"Owenr":Owenr}
        data = collection.find(session)
        countsessions = collection.count_documents(session)
        return data, countsessions

    def findwords(collection, Owenr, target):
        collection = db[collection]
        words = {"Owenr":Owenr, "target":target}
        data = collection.find(words)
        countwords = collection.count_documents(words)
        return data, countwords
        
    def addsession(collection, Owenr, Session):
        collection = db[collection]
        newsession = {"Owenr":Owenr, "Session":Session}
        collection.insert_one(newsession)

    def findpost(collection, Owenr, target, share):
        collection = db[collection]
        post = {"Owenr":Owenr, "share":share, "target":target}
        data = collection.find(post)
        countposts = collection.count_documents(post)
        return data, countposts

    def addpost(collection, Owenr, share, post, target):
        collection = db[collection]
        newspost = {"Owenr":Owenr, "share":share, "post":post, "target":target}
        collection.insert_one(newspost)

    def editpost(collection, Owenr, share, post, target):
        collection = db[collection]
        post1 = {"Owenr":Owenr, "share":share, "target":target}
        new = {"$set":{"post":post}}
        collection.update_one(post1, new)

    def specifiChannel(collection, Owenr, target):
        collection = db[collection]
        channel = {"Owenr":Owenr, "target":target}
        data = collection.find(channel)
        countchannels = collection.count_documents(channel)
        return data, countchannels
