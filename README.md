# Smile :) Child Care directory
This is a light service that can consume multiple data sources and make a uniform data set.

## Current Setup
You should install [docker-compose](https://docs.docker.com/compose/install/), clone the repo and run `$ docker-compose up --build`

To ingest data, run 
```$ pipenv run python API_ingest.py && pipenv run python csv_ingest.py && pipenv run python web_scrape_ingest.py```


### todos

#### done (with time taken)
- Compare ds Columns - 15 min
- define initial schema - 15 min
- setup database container with test seed script - 1 hour
- env security? - 15 min
- set up and test dedoop - 1 hour
- setup and test scrape ingest- 5 hours
- setup and test csv ingest - 30 min
- setup and test API ingest - 30 min
- SQL scripts - 1 hour
- document!! - 1 hour

#### todo
- needs way more tests
- multi-state support (not just California!)
- examine errors in logs and fix (looks like off by one errors persist in web scraper)
- Theres extremely large amounts of duplication according to our dedup method (phone number)
This is a data smell for sure, work with stakeholders to come up with a better uniqueness system
- see commented TODOs
- data ingestion should be a script or single command
