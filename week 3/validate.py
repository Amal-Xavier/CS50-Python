import re
email = input("whats your email? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.com$",email,re.IGNORECASE):
    print("valid")
else:
    print("invalid")