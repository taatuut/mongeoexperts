# Uh, mongeoexperts ?
Ok, bit tongue in cheek, but MongoDB + GeoExperts = mongeoexperts right?

This repository contains the code that I demoed during the `Expert Sessie` presentation for GeoExperts, GeoBIMExperts, Ruimteschepper, NieuwlandGEO on March 23rd 2021.

You can clone/copy/use this code and play with it yourself to explore the two (2) available features:

1. Load data into an MongoDB Atlas cluster
2. Retrieve data using a spatial query

# Prerequisites

* MongoDB Atlas account -> go to https://www.mongodb.com/cloud and click [ Try Free ] to register
* Visual Studio Code, or your favorite Python editor and a command line terminal
* MongoDB Database tools for your operating system. https://www.mongodb.com/try/download/database-tools NOTE: you could write the data loading part in Python only, but the tool fucntionality is nice to explore too.   
* Python 3.7 or higher with pip installed, preferably the latest version of Python for your operating system 
* PyMongo driver, install running `python -m pip install pymongo[snappy,gssapi,srv,tls]` NOTE: this assumes that `python` calls your Python 3.x executable, depending on how you installed Python version(s), you might need to use `python3` or a full path

## Optional

* MongoDB Compass <TODO: link>

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

As a first test to see the output of the data creation, run the following command:

`python create_grid.py`

This prints unique 648 points in geojson format  

Now run `python create_grid.py | mongoimport --uri mongodb+srv://<user>:<pass>@yourserver.at.mongodb.net/test --drop --collection gridder --jsonArray`

This does a one time import of the data, deleting the collection if it already existed , and returns something like:

```
2021-03-24T02:12:20.493+0100    connected to: atlas-lzg21q-shard-0/yourserver-shard-00-00.at.mongodb.net:27017,yourserver-shard-00-01.at.mongodb.net:27017,yourserver-shard-00-02.at.mongodb.net:27017
2021-03-24T02:12:20.567+0100    dropping: test.gridder
2021-03-24T02:12:21.069+0100    imported 648 documents
```

# Extra

* Load the sample data
* Use Compass to connect to Atlas, then explore the datasets, e.g. the shipwreck data <TODO: description schema analysis with map image, select, export code>
