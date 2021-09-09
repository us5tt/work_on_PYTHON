import pyowm
from pyowm import OWM

owm = OWM ('401c2528345ba1056c169070c57f5cee')

mgr = owm.weather_manager()

observation = mgr.weather_at_place ('Orynyn')
w = observation.weather

temperatura=w.temperature ('celsius')['temp']


print (str (w) + str(temperatura))
print (str(temperatura))