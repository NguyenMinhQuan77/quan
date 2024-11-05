import requests, json

def get_geo_info(url):
    try:
        r = requests.get(url)
        print("HTTP status code: " + str(r.status_code))
        print(r.headers)
        if r.status_code == 200:
            data = r.json()
            for d in data.items():
                print(d)
            print("Header response:")
            for header, value in r.headers.items():
                print(header, "-->",value)
            print("Header request")
            for header, value in r.request.headers.items():
                print(header, "-->",value)
            print("server: " + r.headers['server'])
        else:
            print(f"Error: HTTP status code {r.status_code}")

        # r = requests.get(url)
        # r.raise_for_status()
        # geo_info = r.json()
        # print("IP address: ", geo_info.get('ip'))
        # print("Hostname: ", geo_info.get('hostname'))
        # print("Country: ", geo_info.get('country'))
        # print("Region: ", geo_info.get('region'))
        # print("City: ", geo_info.get('city'))
        # print("Location: ", geo_info.get('loc'))
#        print(geo_info)
    except requests.RequestException as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    url = 'https://ipinfo.io/111.65.249.59/json'
    get_geo_info(url)
