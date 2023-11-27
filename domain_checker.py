import http.client
import json

# Replace 'YOUR_API_KEY' with your actual API key
api_key = 'Your whoisfreaks.com API'
domain_name = 'Your Domain'

conn = http.client.HTTPSConnection("api.whoisfreaks.com")

# Use f-string to insert variables into the URL
url = f"/v1.0/whois?whois=live&domainName={domain_name}&apiKey={api_key}"

payload = ''
headers = {}

try:
    conn.request("GET", url, payload, headers)
    res = conn.getresponse()

    if res.status == 200:
        data = res.read()
        response_json = json.loads(data.decode("utf-8"))

        # Extract specific fields
        status = response_json.get('status', False)
        domain_name = response_json.get('domain_name', '')
        domain_registered = response_json.get('domain_registered', '')
        create_date = response_json.get('create_date', '')
        expiry_date = response_json.get('expiry_date', '')
        registrar_info = response_json.get('domain_registrar', {})

        # Format the extracted information
        formatted_data = f"Status: {status}\nDomain Name: {domain_name}\nDomain Registered: {domain_registered}\nCreate Date: {create_date}\nExpiry Date: {expiry_date}\n"

        # Add registrar information
        if registrar_info:
            formatted_data += "\nRegistrar Information:\n"
            formatted_data += f"IANA ID: {registrar_info.get('iana_id', '')}\n"
            formatted_data += f"Registrar Name: {registrar_info.get('registrar_name', '')}\n"
            formatted_data += f"Whois Server: {registrar_info.get('whois_server', '')}\n"
            formatted_data += f"Website URL: {registrar_info.get('website_url', '')}\n"
            formatted_data += f"Email Address: {registrar_info.get('email_address', '')}\n"
            formatted_data += f"Phone Number: {registrar_info.get('phone_number', '')}\n"

        print(formatted_data)

    else:
        print(f"Error: {res.status}, {res.reason}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    conn.close()
