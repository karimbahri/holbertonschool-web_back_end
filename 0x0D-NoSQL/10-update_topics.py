#!/usr/bin/env python3
"""10-udate_topics"""


def update_topics(mongo_collection, name, topics):
    """update_topics:
        function to update documents
    """
    mongo_collection.update_many({'name': name}, { '$set': {'topics': topics}})
