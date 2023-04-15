import json

import os
import gzip
import json
import jsonlines
import elasticsearch.helpers

from datetime import datetime
from elasticsearch import Elasticsearch
from ssl import create_default_context


# es = Elasticsearch(
#     ["https://elastic:E7AaHfVPLZ93b75ZSi=y@localhost:9200"],
#     ssl_assert_fingerprint="9cd149588d337aed62d90fcf9fca5570beb3b0b4e5730ba37c6ccb280fc52ef9",
#     request_timeout=10000,
# )
# print(es.info())

json_lines = []
# line_limit = 10
# Create an index

with open("/Users/dhyeypandya/academic_search_service/updated_date=2023-02-17/part_000", 'r') as fh:
    for fobj in fh:
        json_lines.append(json.loads(fobj))
        print('new line added')


# es.indices.create('concepts_test',
#     {
#         'mappings': {
#             'properties': {
#                 # A keyword argument for the `type` property.
#                 'tags': {
#                     'type': 'concepts'
#                 }
#             }
#         }
#     })


for item in json_lines:
    # Index the JSON object
    if "abstract_inverted_index" in item:
        print(item["abstract_inverted_index"])



def get_abstract(idx):
    if not idx:
        return None
    
    abstract = [""]*1000
    for k,v in idx.items():
        for pos in v:
            abstract[pos] = k
    abstract = " ".join(abstract).strip()
    return abstract

        
