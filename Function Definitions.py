from elasticsearch import Elasticsearch, helpers
import pandas as pd

es = Elasticsearch("http://localhost:9200")

def createCollection(p_collection_name):
    if not es.indices.exists(index=p_collection_name):
        es.indices.create(index=p_collection_name)
        print(f"Index {p_collection_name} created.")
    else:
        print(f"Index {p_collection_name} already exists.")


def indexData(p_collection_name, p_exclude_column):
    df = pd.read_csv('employee_dataset.csv') 
    df = df.drop(columns=[p_exclude_column])
    records = df.to_dict(orient='records')
    
    actions = [
        {
            "_index": p_collection_name,
            "_source": record
        }
        for record in records
    ]
    helpers.bulk(es, actions)
    print(f"Data indexed into {p_collection_name}, excluding column {p_exclude_column}.")


def searchByColumn(p_collection_name, p_column_name, p_column_value):
    body = {
        "query": {
            "match": {
                p_column_name: p_column_value
            }
        }
    }
    result = es.search(index=p_collection_name, body=body)
    print(f"Search Results for {p_column_name} = {p_column_value}:")
    for hit in result['hits']['hits']:
        print(hit['_source'])

def getEmpCount(p_collection_name):
    result = es.count(index=p_collection_name)
    print(f"Employee count in {p_collection_name}: {result['count']}")

def delEmpById(p_collection_name, p_employee_id):
    es.delete(index=p_collection_name, id=p_employee_id)
    print(f"Employee {p_employee_id} deleted from {p_collection_name}.")

def getDepFacet(p_collection_name):
    body = {
        "aggs": {
            "departments": {
                "terms": {
                    "field": "Department.keyword",
                    "size": 10
                }
            }
        }
    }
    result = es.search(index=p_collection_name, body=body, size=0)
    print(f"Department Facets for {p_collection_name}:")
    for bucket in result['aggregations']['departments']['buckets']:
        print(f"Department: {bucket['key']}, Count: {bucket['doc_count']}")
