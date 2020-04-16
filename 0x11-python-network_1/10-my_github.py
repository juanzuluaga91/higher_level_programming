#!/usr/bin/python3
"""
"""

if __name__ == "__main__":
    import requests
    from sys import argv
    url = "https://api.github.com/user"
    auth = (argv[1], argv[2])
    response = requests.get(url, auth=auth)
    try:
        print(response.json().get("id"))
    except ValueError:
        print("Not a valid JSON")
