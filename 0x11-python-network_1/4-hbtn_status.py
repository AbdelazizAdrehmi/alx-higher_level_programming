#!/usr/bin/python3
"""- fetches https://intranet.hbtn.io/status."""
import requests


if __name__ == "__main__":
    r = requests.get("https://intranet.hbtn.io/status")
    print("Body response:\t")
    print("- type: {}\t".format(type(r.text)))
    print("- content: {}".format(r.text)))
