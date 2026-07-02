import re

url = input("whats your username? ").strip()

if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/(\w+)$",url,re.IGNORECASE):
    print("hello",matches.group(1))