#!/usr/bin/env python3
""" 11-schools_by_topics """


def schools_by_topic(mongo_collection, topic):
    """schools_by_topic:
        a function that return documents that matches
        with topic
    """
    return list(mongo_collection.find({'topics': topic}))
