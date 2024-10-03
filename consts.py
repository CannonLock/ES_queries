import requests

SUMMARY_INDEX = "gracc.osg.summary"
ENDPOINT = "https://gracc.opensciencegrid.org:443/q"
HEADERS = {
    'Content-Type': 'application/json',
    'authority': 'gracc.opensciencegrid.org',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9'
}
SESSION = requests.Session()
SESSION.headers.update(HEADERS)