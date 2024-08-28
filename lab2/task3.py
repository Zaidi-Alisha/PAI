def convert_url(url):
    if url.startswith("http://www."):
        new_url = url[11:]
        if not new_url.endswith(".com"):
            new_url += ".com"
        return new_url
    else:
        print("Invalid URL. Please enter a URL that starts with http://www.")
        return None


# Get the URL from the user
url = input("Please enter the URL that starts with http://www.: ")

# Convert the URL
new_url = convert_url(url)

# Print the result
if new_url:
    print("Your converted URL is:", new_url)

