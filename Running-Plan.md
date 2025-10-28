# Running Plan

## 10 28 2025

Estamos tratando elaborar nos sistema



## 6 23 2025

We're currently knee deep in Sci Kit math documentation learning how to apply different regressions and analysis on data sets.

Let's pull aside for a bit and set up a pipeline to pull data from real APIs into a local setup that we can then go back and apply the math we're learning on.

### Plan

- [ ] Set up a simple Python Server
- [ ] Dockerize
- [ ] Set up an appropriate data store in another Docker Container
- [ ] Wire with Docker Compose
- [ ] Identify several different APIs with free tiers
- [ ] Run pods with simple server pulling data from APIs and storing it in data store

### Python Server

- [ ] Set up server
- [ ] Dockerize
- [ ] Pipe in Environment Variable

### Data Store

- [ ] Identify appropriate store which allows for time windows, maybe unstructured data, good for event streams and warehousing (Apache Druid?)
- [ ] Create dockerized instance of store

### Docker Compose

- [ ] Set up docker compose with Store and Server
- [ ] Ensure communication

### APIs with Free Tiers

- [ ] Identify APIs for different types of data with free tiers - government, finance, weather

### Start Pulling Data

- [ ] Pull from free tiers, store in data store
