import os
import json
import subprocess

with open("meta.json", "r") as f:
    meta = json.loads(f.read().strip())

seenUrls = []
for i in meta["images"]:
    seenUrls.append(i["file"])

images = os.listdir("images")
for num, i in enumerate(images):
    url = f"https://github.com/meeplabsdev/catdb/blob/main/images/{i}?raw=true"

    if url not in seenUrls:
        subprocess.run(["/usr/bin/kitty", "icat", os.path.abspath(f"images/{i}")])
        print(f"{num+1} of {len(images)}")
        tags = input("Tags (comma-separated): ").strip().split(",")

        if len(tags) == 1 and tags[0] == "":
            os.remove(f"images/{i}")
            tags = []

        if len(tags) > 0:
            meta["images"].append({"file": url, "tags": tags})

            for tag in tags:
                if tag not in meta["tags"]:
                    meta["tags"].append(tag)

    with open("meta.json", "w") as f:
        f.write(json.dumps(meta, indent=2))
