# Bus tracking web app (Flask + WebSockets + Leaflet (conversion to google maps api pending))

A real-time web app that fetches live bus data from the liverpool area, option to add custom bus route is live!

Right now its very bare-bones, you open the app, it shows you a map with all the bus services in the area through a blue marker. Updated every 10 seconds (although some buses have inconsistencies with how often they update their data so certain markers may be totally still).


## Setup
```bash
git clone https://github.com/LemarTokham/live-bus-tracker.git
cd live-bus-tracker
python -m venv env
source env/bin/activate  # or .\env\Scripts\activate on Windows
pip install -r requirements.txt
python app.py
```
To open, visit http://localhost:3000 on your machine

As you first load up the app, give it 10 seconds for the first set of bus data to come in.

## Planned Features
Live bus timings from specified bus stops

### Current challenge
Integrating the google maps api on a flask

### Next steps
Creating restful APIs for the front end to consume - allows for more flexibility with trying out and integrating features
Conversion to google maps api for further features such as satellite imagery