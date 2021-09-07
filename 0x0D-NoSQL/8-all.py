#!/usr/bin/env python3
"""8-all"""


def list_all(mongo_collection):
    """list_all
        display all documents of given collection
    """
    doc = mongo_collection.find({})
    if doc:
        return doc
    return []
