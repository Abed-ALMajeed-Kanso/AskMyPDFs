from .elastic_service import search as es_search

def keyword_search(query):
    keyword_results = es_search(query)
    return [hit.get("text") for hit in keyword_results if hit.get("text")][:8]