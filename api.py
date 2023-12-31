import requests
import json

def make_api_call(pdf_file_path):
    base_url = "http://74.235.130.132:8080"
    api_path = "/document-ai"
    api_endpoint = f"{base_url}{api_path}"


    files = {'pdf_file': open(pdf_file_path, 'rb')}


    response = requests.post(api_endpoint, files=files)

    if response.status_code == 200:

        try:
            json_response = response.json()
            l = json.dumps(json_response, indent=2)
            return l

        except json.JSONDecodeError:
            print("Response is not in JSON format.")
            print(response.text)  
            return None
    else:
        print(f"API call failed with status code {response.status_code}")
        print(response.text)  
        return None

# Example usage:
# pdf_file_path = "F:/testntrack/Adobe Scan Dec 29, 2023 (2).pdf"
# result = make_api_call(pdf_file_path)