# Uh, mongeoexperts ?
Ok, bit tongue in cheek, but MongoDB + GeoExperts = mongeoexperts right?

This repository contains the code that I demoed during the `Expert Sessie` presentation for GeoExperts, GeoBIMExperts, Ruimteschepper, NieuwlandGEO on March 23rd 2021.

You can clone/copy/use this code and play with it yourself to explore the two (2!) available features:

1. Load data into an MongoDB Atlas cluster
2. Retrieve data using a spatial query

However, since these features run on a Atlas cluster you just created yourself without much of a hassle, I believe they showcase the value of the flexible data application platform in the cloud pretty well especially since setting up databases in the cloud is still not daily practice for most people. But now you can easily do it so let's go!

# Prerequisites

* MongoDB Atlas account -> go to https://www.mongodb.com/cloud and click [ Try Free ] to register
* Visual Studio Code, or your favorite Python editor and a command line terminal
* MongoDB Database Tools for your operating system. https://www.mongodb.com/try/download/database-tools NOTE: you could do the data loading part in Python only, but the database tools functionality is interesting to explore too. We'll only cover `mongoimport` here, but there are other tools for statistics on your MongoDB instance, data backup etc. See https://docs.mongodb.com/database-tools/ for more info
* Python 3.7 or higher with `pip` installed, preferably the latest version of Python for your operating system 
* PyMongo driver, install running `python -m pip install pymongo[snappy,gssapi,srv,tls]` NOTE: this assumes that `python` calls your Python 3.x executable, depending on how you installed Python version(s), you might need to use `python3` or a full path
* Module `dnspython`, install running `python -m pip install dnspython`

## Optional

* MongoDB Compass is the GUI for MongoDB, it allows you to make smarter decisions about document structure, querying, indexing, document validation, and more. You can download the installer for the full version of MongoDB Compass, with all features and capabilities at https://www.mongodb.com/try/download/compass 

# Steps

1. Get started with Atlas

See https://docs.atlas.mongodb.com/getting-started/ for the manual. Atlas Free Tier clusters provide a small-scale development environment to host your data. Free Tier clusters never expire. Execute the steps from part 1-6:

Part 1: Create an Atlas Account. https://docs.atlas.mongodb.com/tutorial/create-atlas-account/ This is a one time registration

Part 2: Deploy a Free Tier Cluster. https://docs.atlas.mongodb.com/tutorial/deploy-free-tier-cluster/ NOTE: Click [ Create a new cluster] and select the free M0 Sandbox Cluster Tier in the wizard

Part 3: Add Your Connection IP Address to Your IP Access List. https://docs.atlas.mongodb.com/security/add-ip-address-to-list/ NOTE: for access to your cluster from any IP address, use 0.0.0.0/0 as mask

Part 4: Create a Database User for Your Cluster. https://docs.atlas.mongodb.com/tutorial/create-mongodb-user-for-cluster/ NOTE: This will be your Atlas admin user 

Part 5: Connect to Your Cluster. https://docs.atlas.mongodb.com/tutorial/connect-to-your-cluster/ You can copy the required connections strings to use with `mongoimport` and the Python code directly from your cluster in Atlas

Part 6: Insert and View Data in Your Cluster. To use the code from the presentation, add your connection strings to the two Python in this repository and run them. See Step 2. on how to do this. Alternatively you can look at the examples at https://docs.atlas.mongodb.com/tutorial/insert-data-into-your-cluster/   

2. Configure and run the example application

## Load data

As a first test to see the output of the data creation, run the following command:

`python create_grid.py`

This prints unique 648 points in geojson format if you use the code as is. Of course you can change it to create more/less data. To use the spatial capabilities

Install the MongoDB Database Tools if you have not already done so. This will add the database tools to your path so you can directly use them on the command line.

To get the connection string for your cluster, go to the Clusters overview in the Atlas UI and click [ Connect ]

![image](https://user-images.githubusercontent.com/2260360/112276619-3d2d9780-8c81-11eb-85b3-63d86f6baea9.png)


Now run `python create_grid.py | mongoimport --uri mongodb+srv://<user>:<pass>@yourserver.at.mongodb.net/test --drop --collection gridder --jsonArray`

This does a one time import of the data, deleting the collection if it already existed , and returns something like:

```
2021-03-24T02:12:20.493+0100    connected to: atlas-lzg21q-shard-0/yourserver-shard-00-00.at.mongodb.net:27017,yourserver-shard-00-01.at.mongodb.net:27017,yourserver-shard-00-02.at.mongodb.net:27017
2021-03-24T02:12:20.567+0100    dropping: test.gridder
2021-03-24T02:12:21.069+0100    imported 648 documents
```

## Query data

<TODO: describe how to add Python connection string to the script>

To see  the output for the spatial query run `python query_grid.py`

This returns 3 documents after the initial data load:

```
{'_id': ObjectId('605a92c9be9b2e7d85af4848'), 'type': 'Feature', 'geometry': {'type': 'Point', 'coordinates': [0.0, 60.0]}, 'properties': {'name': 'Point340'}}
{'_id': ObjectId('605a92c9be9b2e7d85af485d'), 'type': 'Feature', 'geometry': {'type': 'Point', 'coordinates': [10.0, 60.0]}, 'properties': {'name': 'Point358'}}
{'_id': ObjectId('605a92c9be9b2e7d85af486c'), 'type': 'Feature', 'geometry': {'type': 'Point', 'coordinates': [20.0, 60.0]}, 'properties': {'name': 'Point376'}}
```

3. 'Automate it'

To create your own two continously running 'microservices' we will kick-off the above Python scripts in the most simple automated way right from the command line in a terminal.

* To load data continuously run the following command in a terminal, and make sure to replace the connection string with your own first:

`while :; do echo $(date); python create_grid.py | mongoimport --uri mongodb+srv://<user>:<pass>@yourserver.at.mongodb.net/test --collection gridder --jsonArray; sleep 15; done`

NOTE: this command does not use the `--drop` parameter anymore so it keeps adding new documents to the `gridder` collection in the `test` database every 15 seconds as long as the command runs

* To query continuously run the following command in another terminal:

`while :; do echo $(date); python query_grid.py; sleep 30; done`

Note: you should already have added your own Atlas connection string for Python to the `query_grid.py` script in Step 2, and running this command returns a growing result set every 30 seconds that matches the spatial filter (growing because more and more data is loaded over time) 

![image](https://user-images.githubusercontent.com/2260360/112276160-b678ba80-8c80-11eb-8af5-e0f2494144a0.png)

4. Be happy

You are done! You just set up an Atlas cluster in the cloud, and from the application code created a database with a collection holding data, with a spatial query returning the results your business needs. What more do you want to achieve in 60 minutes? Time for a cup of coffee and some fresh air.

# Extra

* Create a spatial index! We run this example without using an index. This works but if we would really have humungous loads of data an index will help to speed up queries.
* Load the sample data that comes with MongoDB Atlas. Go to your cluster in the Atlas UI and click [ Load Sample Dataset ] as in the image below

![image](https://user-images.githubusercontent.com/2260360/112274883-487fc380-8c7f-11eb-9401-88a157bb1762.png)

More information on loading the data with examples on how to use it, can be found at https://docs.atlas.mongodb.com/sample-data/ NOTE: the Atlas Free Tier comes with 512 MB storage space, the sample dataset takes ~330 MB. You can always delete and reload it later on. 

* Use Compass to connect to Atlas, then explore the datasets, e.g. the shipwreck data <TODO: description schema analysis with map image, select, export code>. Compass also includes a beta version of the MongoDB Shell, an interactive JavaScript interface to MongoDB. MongoDB Shell is available as a standalone product you can run from the command line, see https://www.mongodb.com/try/download/shell

# Contact

Feel free to contact me with any questions and remarks. Also about issues you run into and possible improvements. The usual works-on-my-machine-disclaimer: this code should run out of the box with just an Atlas connection string added, if not ping me and we'll dive into it. Of course I envourage everyone to adapt the code at their needs, change it to load real world data, and add more features! :-) 

```
{
  "name": "Emil Zegers",
  "title": "Senior Solutions Architect",
  "phone": "+31 6 19929703",
  "email": "emil.zegers@mongodb.com",
  "location": "Nijmegen, Netherlands",
  "twitter": ["@emilzegers", "@mongodb"],
  "linkedin": "https://www.linkedin.com/in/emilzegers"
}
```
