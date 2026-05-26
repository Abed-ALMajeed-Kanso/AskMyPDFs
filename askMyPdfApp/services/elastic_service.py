import os
import requests

ES_URL = os.environ.get("ELASTICSEARCH_URL", "http://localhost:9200")
INDEX = "docs"


def _ensure_index():
    url = f"{ES_URL}/{INDEX}"

    try:
        response = requests.head(url, timeout=5)

        if response.status_code == 404:
            requests.put(
                url,
                json={
                    "settings": {
                        "number_of_shards": 1,
                        "number_of_replicas": 0
                    },
                    "mappings": {
                        "properties": {
                            "text": {
                                "type": "text"
                            },
                            "source": {
                                "type": "keyword"
                            },
                            "page": {
                                "type": "integer"
                            }
                        }
                    }
                },
                timeout=5
            )

    except requests.RequestException as e:
        print("Elasticsearch not reachable:", e)


def index_document(chunk, meta=None):
    meta = meta or {}

    _ensure_index()

    url = f"{ES_URL}/{INDEX}/_doc"

    payload = {
        "text": chunk,
        "source": meta.get("source"),
        "page": meta.get("page")
    }

    try:
        res = requests.post(url, json=payload, timeout=10)
        res.raise_for_status()
    except requests.RequestException as e:
        print("Indexing failed:", e)


def index_chunk(chunks, meta=None):
    """
    chunks MUST be a list of strings
    """
    meta = meta or {}

    if not isinstance(chunks, list):
        chunks = [chunks]

    for chunk in chunks:
        if not chunk:
            continue
        index_document(chunk, meta=meta)


def delete_by_source(source_filename):
    """
    Delete all indexed documents with a specific source (PDF filename).
    """
    _ensure_index()

    url = f"{ES_URL}/{INDEX}/_delete_by_query"

    try:
        res = requests.post(
            url,
            json={
                "query": {
                    "term": {
                        "source": source_filename
                    }
                }
            },
            timeout=10
        )

        res.raise_for_status()
        data = res.json()
        deleted_count = data.get("deleted", 0)
        print(f"Deleted {deleted_count} document(s) from Elasticsearch for source: {source_filename}")
        return deleted_count

    except requests.RequestException as e:
        print(f"Delete by source failed for {source_filename}: {e}")
        return 0


def search(query):
    _ensure_index()

    url = f"{ES_URL}/{INDEX}/_search"

    try:
        res = requests.post(
            url,
            json={
                "size": 5,
                "query": {
                    "match": {
                        "text": query
                    }
                }
            },
            timeout=10
        )

        res.raise_for_status()
        data = res.json()

        return [
            hit["_source"]
            for hit in data.get("hits", {}).get("hits", [])
        ]

    except requests.RequestException as e:
        print("Search failed:", e)
        return []