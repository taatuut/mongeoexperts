from pymongo import MongoClient

# Examples:

#client = MongoClient('mongodb://localhost:27017/test')
#client = MongoClient("mongodb+srv://<user>:<pass>@yourserver.at.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

# TODO: add your own Atlas connection string for Python to the next line between the double quotes
client = MongoClient("")

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
