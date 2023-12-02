import pyshorteners

long_url = input("Enter the url to short: ");

tiny_url = pyshorteners.Shortener()

short_url = tiny_url.tinyurl.short(long_url)

print("The shortened url: " + short_url)