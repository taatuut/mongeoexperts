from pymongo import MongoClient

# Examples:

#client = MongoClient('mongodb://localhost:27017/test')
#client = MongoClient("mongodb+srv://<user>:<pass>@yourserver.at.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

# TODO: replace YOUR_CONNECTION_STRING_HERE with your own Atlas connection string for Python in the next line, and leave out the Pymongo prefix
client = YOUR_CONNECTION_STRING_HERE

filter={
    'geometry': {
        '$geoWithin': {
            '$centerSphere': [
                [
                    9.73292112350464, 60.04167133076125
                ], 0.1
            ]
        }
    }
}

result = client['test']['gridder'].find(
  filter=filter
)

for document in result: 
    print(document)
