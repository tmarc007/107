import pymongo
import certifi

con_str ="mongodb+srv://thomasmarcello:estrella123@cluster0.vniyapv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())
db = client.get_database("107test")