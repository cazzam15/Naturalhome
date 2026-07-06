#!/usr/bin/env python3
"""Post one of the 12 prepared Natural Home images to Instagram via upload-post.

Usage:
  python3 post.py 1          # post 01-launch.png with its caption
  python3 post.py 7 --dry    # show what would be posted, send nothing

The upload-post profile is "naturalhome" (Instagram must be connected at
https://app.upload-post.com). API key is read from UPLOAD_POST_KEY, falling
back to the n8n container's stored credential.
"""
import os
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent
PROFILE = "naturalhome"

IMAGES = {
    1: "01-launch.png", 2: "02-green-clean.png", 3: "03-natural-beauty.png",
    4: "04-zero-waste.png", 5: "05-herbal-remedies.png", 6: "06-pet-care.png",
    7: "07-recipe-spray.png", 8: "08-recipe-lipbalm.png", 9: "09-recipe-pesto.png",
    10: "10-recipe-elderberry.png", 11: "11-recipe-pawbalm.png", 12: "12-free-guide.png",
}


def get_key():
    key = os.environ.get("UPLOAD_POST_KEY")
    if key:
        return key
    out = subprocess.run(
        ["docker", "exec", "n8n", "sh", "-c",
         "n8n export:credentials --decrypted --all --output=/tmp/c.json >/dev/null 2>&1;"
         " node -e \"const c=require('/tmp/c.json');"
         "console.log(c.find(x=>x.name.includes('Upload')).data.value)\";"
         " rm /tmp/c.json"],
        capture_output=True, text=True, check=True)
    return out.stdout.strip()


def get_caption(n):
    text = (HERE / "captions.md").read_text()
    sections = re.split(r"^## ", text, flags=re.M)[1:]
    for s in sections:
        header, _, body = s.partition("\n")
        if header.startswith(f"{n:02d} "):
            return header.split("—", 1)[1].strip(), body.replace("---", "").strip()
    sys.exit(f"caption {n:02d} not found in captions.md")


def main():
    if len(sys.argv) < 2 or not sys.argv[1].isdigit():
        sys.exit(__doc__)
    n = int(sys.argv[1])
    dry = "--dry" in sys.argv
    image = HERE / IMAGES[n]
    title, caption = get_caption(n)

    print(f"Post {n:02d}: {title}\nImage: {image.name}\n\n{caption}\n")
    if dry:
        print("(dry run — nothing sent)")
        return

    cmd = [
        "curl", "-s", "-X", "POST",
        "-H", f"Authorization: {get_key()}",
        "-F", f"user={PROFILE}",
        "-F", "platform[]=instagram",
        "-F", f"photos[]=@{image}",
        "-F", f"title={caption}",
        "-F", f"caption={caption}",
        "https://api.upload-post.com/api/upload_photos",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout or result.stderr)


if __name__ == "__main__":
    main()
