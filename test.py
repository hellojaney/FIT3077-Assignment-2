"""
@author: David Lei
@since: 5/4/2017
"""
from flask import Flask
from flask import jsonify
from suds.client import Client

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Nothing to see here</h1>'

@app.route('/FIT3077-Example')
def example():
    url = 'http://viper.infotech.monash.edu.au:8180/axis2/services/MelbourneWeather2?wsdl'
    client = Client(url)
    res = []
    print(client)
    locations = client.service.getLocations()
    for loc in locations:
        # Note: client.service.getRainfall()/getTemperature() returns a list of form [date time, value]
        date_time, rainfall = client.service.getRainfall(loc)
        date, time = date_time.split(' ')
        temp = client.service.getTemperature(loc)[-1]
        s = "%s %s %s\nTemperature: %s\nRainfall: %s\n" % (loc, date, time, temp, rainfall)
        res.append(s)
    print("DONE")
    for r in res:  # Print to stdout.
        print(r)
    return jsonify(res)  # Return stuff to webpage


if __name__ == "__main__":
    app.run(debug=True)