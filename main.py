from monitor import Monitor
from suds.client import Client


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
    res.append(Monitor(loc, temp, rainfall))

