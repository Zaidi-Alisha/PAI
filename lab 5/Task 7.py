'''Task 7'''

import re

text = """
Here are some emails: alice@example.com, bob.smith@domain.org, and invalid@domain, 
contact us at info@company.co, or admin@web-site.org.
"""

emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)

print("Valid emails found:")
for email in emails:
    print(email)