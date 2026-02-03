#!/usr/bin/env python3
"""Update topics of a school document by name."""


def update_topics(mongo_collection, name, topics):
    """Update (replace) the topics field for all documents matching name."""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
