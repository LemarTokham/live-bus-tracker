# people.py

BUSES = { 
    "699": { 
        "locations": [{'long': '-2.733096', 'lat': '53.453126'}],
    },
    "84": {
        "locations": [{'long': '-2.710538','lat': '53.467378'}]
        
    },
    "14": { 
        "locations": [{'long': '-2.720581','lat': '53.450166'}]
    }
}
serviceNum = 0
def create(service): # Service is a json doc
    service.get()
    return serviceNum, 200 # Ok

def fetch_data():
    return BUSES