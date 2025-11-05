#!/usr/bin/env python3
"""
Task 2: Consuming and processing data from an API using Python
This module contains functions to fetch and process data from
JSONPlaceholder API.
"""

import csv

import requests


def fetch_and_print_posts():
    """
    Fetches all posts from JSONPlaceholder and prints their titles.
    Also prints the status code of the response.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """
    Fetches all posts from JSONPlaceholder and saves them to a CSV file.
    Saves data to posts.csv with columns: id, title, body
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200:
        posts = response.json()

        with open("posts.csv", "w", newline="") as csvfile:
            writer = csv.DictWriter(
                csvfile, fieldnames=[
                    "id", "title", "body"])
            writer.writeheader()
            for post in posts:
                writer.writerow({
                    "id": post["id"],
                    "title": post["title"],
                    "body": post["body"]
                })
