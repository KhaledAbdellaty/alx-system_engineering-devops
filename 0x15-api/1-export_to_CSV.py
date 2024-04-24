#!/usr/bin/python3
"""Script that list To-do information for a employee Id."""
import csv
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    with open("{}.csv".format(sys.argv[1]), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [sys.argv[1], username, t.get("completed"), t.get("title")]
         ) for t in todos]
