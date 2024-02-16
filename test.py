import requests
import xml.etree.ElementTree as ET

def send_xml_request(api_key):
    # Select request params
    xml_payload = open("API_request.xml").read()

    # API url
    endpoint_url = 'https://api.opentransportdata.swiss/trias2020'

    try:
        response = requests.post(endpoint_url, headers={'Content-Type': 'application/xml', 'Authorization': 'Bearer {}'.format(api_key)}, data=xml_payload)
        if response.status_code == 200:
            # Process the response data as needed
            return response
        else:
            print("Error: Unable to fetch data from the API. Status code:", response.status_code)
    except Exception as e:
        print("An error occurred:", e)

api_key = 'eyJvcmciOiI2NDA2NTFhNTIyZmEwNTAwMDEyOWJiZTEiLCJpZCI6ImFlMjA4ODJkZTRjMzRjYTY4NjVkNDJkOGM1MWFmM2YxIiwiaCI6Im11cm11cjEyOCJ9'

response = send_xml_request(api_key)
print(type(response))

tree = ET.ElementTree(ET.fromstring(response.text))
root = tree.getroot()

for child in tree:
    print(child.tag, child.attrib)
