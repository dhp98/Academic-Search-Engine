# Academic-Search-Engine | ElasticSearch | OpenAlex 

Intro:

A highly usable academic search engine that can perform complex search and query tasks on the entire Open Alex academic dataset. The project involves implementing and configuring Elasticsearch on a multi-server instance, tuning configurations for optimized searching, developing APIs to use the system, and designing a frontend and backend for a search engine type web interface.


Work Done:
* Setup 5 Nodes ElasticSearch Cluster, with custom node roles ensuring fast ingestion and high availability.
* Ingested 300 Million +, records in the cluster, in 5 different indices for each entity types in Openalex dataset
* Python Ingestion Script to ingest 5000 records per second using bulk api and parallel processing.
* Transform data before indexing to enable full text search on the Research Papers/Journals Abstract in our search engine.
* Fast queires to extract records based on keywords.

Ongoing Work:
* Frontend(React.JS) - Search Engine type web interface, similar to Google Scholar, to perform search operations.
* Backend (ElasticSearch and Node.JS) -  REST API's to form ElasticSearch queries and send back seach results back to the user.


https://www.elastic.co/guide/en/elasticsearch/reference/7.17/index.html
https://openalex.org/

