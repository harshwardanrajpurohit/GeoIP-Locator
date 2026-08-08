import requests

def get_location(ip_address=""):
    """Fetches and prints the location details of a given IP address."""
    # If ip_address is empty, ip-api automatically uses the caller's public IP
    url = f"http://ip-api.com/json/{ip_address}"

    try:
        response = requests.get(url)
        data = response.json()

        if data.get('status') == 'success':
            print("\n=== Location Results ===")
            print(f"IP Address:   {data.get('query')}")
            print(f"Country:      {data.get('country')}")
            print(f"Region/State: {data.get('regionName')}")
            print(f"City:         {data.get('city')}")
            print(f"Coordinates:  {data.get('lat')}, {data.get('lon')}")
            print("========================\n")
        else:
            print(f"\nError: Could not locate IP. Reason: {data.get('message', 'Unknown')}\n")

    except Exception as e:
        print(f"\nAn error occurred while fetching data: {e}\n")

# Main Menu
print('''Checking your last location using IP address
Chose your option:
1. Manually enter an IP Address
2. Fetch My IP Address automatically
3. Exit
''')

uip = input("Enter your Option: ")

if uip == '1':
    ip = input("Enter your IP Address: ")
    print("Your IP Address is: ", ip)
    get_location(ip)

elif uip == '2':
    print("Fetching your public IP and location...")
    # Passing an empty string forces the API to automatically detect your public IP
    get_location("")

elif uip == '3':
    print("Exiting the program...")
else:
    print("Invalid option selected.")