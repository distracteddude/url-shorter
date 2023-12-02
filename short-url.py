import pyshorteners

# create a func that short urls.
def shorty(URL):
    shortener = pyshorteners.Shortener()
    shortened_url = shortener.tinyurl.short(URL)
    return shortened_url

# create a loop that breaks when we put exit.
active = True

while active:
    url = input('Enter url: ')

    if url.lower() == 'exit':
        active = False

    elif url:
        shortened_url = shorty(url)
        print(shortened_url)
    
    else: 
        print('Invalid. please try again')
        continue
