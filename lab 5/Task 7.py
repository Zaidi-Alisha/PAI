'''Task 7'''

import re

text = "My email address is example15363@gmail.com"

emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)

print("Valid emails found:")
for email in emails:
    print(email)
