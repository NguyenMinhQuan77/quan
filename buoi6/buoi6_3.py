from geoip import geolite2
import dnspython
result = geolite2.lookup(ipaddress)
if result is None:
    print("country: ", result.country)
    result.continent
    result.timezone

dnspython.resolver
result = dnspython.resolver.query('www.abc.com', 'A')
for i in result:
    print("IP:", i.to_text())
