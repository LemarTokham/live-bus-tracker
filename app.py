from flask import Flask, request, jsonify, render_template
from flask_sock import Sock
from flask_cors import CORS
import requests
import xml.etree.ElementTree as ET
import threading
from flask_socketio import SocketIO, send, emit
from dotenv import load_dotenv
import os
import connexion



# Setup
app = connexion.App(__name__, specification_dir="./")
app.add_api("swagger.yml")
# app.config['SECRET_KEY'] = 'secret!'
# CORS(app)
# socketio = SocketIO(app)

# load_dotenv()
# api_key = os.getenv("API_KEY")


# # Stores locations from api calls
# locations = []
# # Default bus line
# busLine = "17"
# # Fetching data
# def fetch_data():
#     global locations, busLine
#     api_url = f"https://data.bus-data.dft.gov.uk/api/v1/datafeed/708/?api_key={api_key}"

#     response = requests.get(api_url)
#     print("Hi")

#     # Writing to the file
#     with open('location.xml', 'wb') as f:
#         f.write(response.content)

#     # Parsing XML file
#     tree = ET.parse('location.xml')

#     # Getting the tree structure
#     root = tree.getroot()

#     # Dictionary mapping for namespace
#     ns = {'siri': 'http://www.siri.org.uk/siri'}

#     # Clear list before populating
#     locations = []



#     # Get all the 699 bus
#     for line in root.findall(f".//siri:VehicleActivity/siri:MonitoredVehicleJourney/[siri:LineRef='{busLine}']",ns):
#         # get their locations
#         long = line.find('siri:VehicleLocation/siri:Longitude', ns)
#         lat = line.find('siri:VehicleLocation/siri:Latitude', ns)
#         # currently stores the location of the very last bus
#         locations.append({'long': long.text, "lat":lat.text})

#     # Send to frontend
#     socketio.emit('bus locations', locations)

#     print(locations)

#     threading.Timer(10, fetch_data).start()
# fetch_data()


# # Flask endpoints

# @app.get("/locations")
# def get_locations():
#     return jsonify(locations)

@app.route('/')
def index():
    return render_template('index.html')

# @socketio.on('line')
# def handle_user_line(data):
#     global busLine
#     busLine = data.get('line', "17")
#     print(data['line'])


    

if __name__ == '__main__':
    app.run(debug=True, port=3000)