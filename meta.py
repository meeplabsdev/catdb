import os
import json

with open("meta.json", "r") as f:
    meta = json.loads(f.read().strip())
imageMeta = meta["images"]

images = os.listdir("images")
for i in images:
    imageMeta.append({
        "file": f"https://github.com/meeplabsdev/catdb/blob/main/images/{i}?raw=true",
        "tags": []
    })

seenFiles = []
finalImageMeta = []
for i in imageMeta:
    if i["file"] not in seenFiles:
        seenFiles.append(i["file"])
        finalImageMeta.append(i)

meta["images"] = finalImageMeta
with open("meta.json", "w") as f:
    f.write(json.dumps(meta, indent=2))
