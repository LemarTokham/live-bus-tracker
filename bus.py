import json
from flask import Flask, jsonify, request

app = Flask(__name__)

busses = {
    '699': {
        'stops': { 
            '2800S42048C' : 
            {
                'Street' :'Oxford Street',
                'long': '-2.96761',
                'lat': '53.40349'
            },
            '2800S42041A' :
            {
                'Street' :'Grove Street',
                'long': '-2.9618',
                'lat': '53.4055'   
            },
        },
        'locations':{
            'Bus A': {
                'VehicleRef' : '4489',
                'long' : '-2.979453',
                'lat': '53.406046',
            },
            'Bus B': {
                'VehicleRef' : '4438',
                'long' : '-2.925693',
                'lat': '53.388451',
            },
        }
    }
}


busStops = {
    'StopID' : 'merdjdgp',
    'Name' : 'Brownlow Hill',
    'Longitute' : '-2.96636',
    "Latitude" : '53.40555',
    'Busses' : ['699']
}


@app.route('/timetable', methods=['GET'])
def get_timetable():
    return jsonify(busStops)


if __name__ == '__main__':
    app.run(port=5000, debug=True)

