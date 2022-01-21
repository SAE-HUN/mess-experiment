from re import A
import sys
import json

key = sys.argv[0]
a = {"key": key}
with open("a.json", "w") as f:
    json.dump(a, f)