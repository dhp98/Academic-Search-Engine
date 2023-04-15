import json
import jsonlines
import elasticsearch.helpers

from datetime import datetime
from elasticsearch import Elasticsearch
from ssl import create_default_context


# es = Elasticsearch(
#     ["localhost"], request_timeout=30, api_key=("XwI104YBGZAj3XIhC-x2", "xVE1zNGjS1acurq6WjOj_Q")
#     # verify_certs=True,
#     # ca_certs="ca.crt"
# )
# es = Elasticsearch(["localhost"],
#                    port=443,
#                    http_auth=('elastic', 'E7AaHfVPLZ93b75ZSi=y'),
#                    scheme="https",)

es = Elasticsearch(
    ["https://elastic:E7AaHfVPLZ93b75ZSi=y@localhost:9200"],
    ssl_assert_fingerprint="9cd149588d337aed62d90fcf9fca5570beb3b0b4e5730ba37c6ccb280fc52ef9",
)
print(es.info())

template_name = "opealex_works_template"

with open("works_template.json", "r") as f:
    index_template = json.load(f)

es.indices.put_template(
    name=template_name,
    settings=index_template["template"]["settings"],
    mappings=index_template["template"]["mappings"],
    aliases=index_template["template"]["aliases"],
    index_patterns= ["openalex_works_*"]
)
