import pyshorteners
import validators 

# create a function that short urls.
def shorty(URL):
    if validators.url(URL):
        shortener = pyshorteners.Shortener()
        shortened_url = shortener.tinyurl.short(URL)
        return shortened_url
    else:
        return 'Invalid URL.'


# create a loop that breaks if we type exit.
while True:
    url = input('Enter URL (type "exit" to quit): ')

    if url.lower() == 'exit':
        print('Exiting...')
        break

    shortened_url = shorty(url)
    print({shortened_url})