import requests

def ping(url):
    res = requests.get(url)
    print(f"{url}: {res.text}")

urls = [
    'http://httpstat.us/200',
    'http://httpstat.us/400',
    'http://httpstat.us/404',
    'http://httpstat.us/408',
    'http://httpstat.us/500',
    'http://httpstat.us/511'
]

if __name__ == '__main__':
    for url in urls:
        ping(url)

    print("Done")