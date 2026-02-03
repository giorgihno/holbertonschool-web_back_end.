#!/usr/bin/env python3
"""Find schools by a specific topic."""


def schools_by_topic(mongo_collection, topic):
    """Return a list of school documents where topic is in topics array."""
    return list(mongo_collection.find({"topics": topic}))
