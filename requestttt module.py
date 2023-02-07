import requests

# browser save get url in history but in post method url not save it in it history

r = requests.get("https://financialmodelingprep.com/api/v3/historical-chart/1min/AAPL?apikey=YOUR_API_KEY")
print(r.text)
print(r.status_code)
print(r)

u = "https://financialmodelingprep.com/api/v3/historical-chart/1min/AAPL?apikey=YOUR_API_KEY"
d = {
    "p1":4,
    "p2":8
}
r1 = requests.post(url=u, data=d)
print(r1.text)
print(r1.status_code)
print(r1)