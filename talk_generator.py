import sys
import json
talks = json.load(open(sys.argv[1]))

result = {
    i: dict(
        title=talk["title"],
        name=talk["name"],
        abstract=talk["abstract"],
        description=talk["description"],
        bio=talk["bio"],
    ) for i, talk in enumerate(t for t in talks if t["state"] == "accepted")
}

json.dump(result, open("talks.json", "w"), indent=4)
