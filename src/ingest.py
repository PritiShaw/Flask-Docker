import json
import csv
import os
import sys
import re
import subprocess
import urllib3

from flask_sqlalchemy import SQLAlchemy
from db import db, Journal

http = urllib3.PoolManager()
journal_names = []

# Get year from environment 
target_year = os.getenv('TARGET_YEAR')
if target_year is None:
    print("Please set year in environment variable 'TARGET_YEAR' and try again")
    print("Failed to ingest")
    exit(0)
elif int(target_year)>2018 or int(target_year)<1999:    
    print("Outof bound TARGET_YEAR, set within [1999,2018] in environment variable 'TARGET_YEAR' and try again")
    print("Failed to ingest")
    exit(0)
try:
    encoded_body = json.dumps({"query":'{ documentsByIdentifier(identifier: "taxonomy:9606") { count searchkey documents { journal_title publication_year article_type } } }'})
    api_request = http.request('POST', 'http://reach-api.nrnb-docker.ucsd.edu',
                     headers={'Content-Type': 'application/json'},
                     body=encoded_body)
    subprocess.check_output(["wget" ,"--output-document=scimagojr.csv", "https://www.scimagojr.com/journalrank.php?out=xls&year=" + target_year])    
except Exception as e:
    print("Error in getting files")
    print(e)
    exit(0)

data = json.loads(api_request.data.decode('utf-8'))["data"]["documentsByIdentifier"]["documents"]
for journal in data:
    if (journal["publication_year"] != "" and int(journal["publication_year"]) == int(target_year)):
        journal_names.append((journal["journal_title"]).lower())
counter=0
with open("scimagojr.csv") as csvfile:
    rows = csv.reader(csvfile, delimiter=';', quotechar='"')
    next(rows, None)  # skip the headers
    journal_names.sort()
    for row in rows:
        if row[2].lower() in journal_names:
            journal = Journal(row)
            db.session.add(journal)
            counter=counter+1
        if counter%15==0:
            db.session.commit()
    db.session.commit()
    print("Successfully ingested the CSV file")
subprocess.check_output(["rm", "scimagojr.csv"])