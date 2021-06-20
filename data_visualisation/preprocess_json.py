import requests
from requests.exceptions import HTTPError
from datetime import datetime

# Read the API and get the json response, return empty string if error encountered
def get_json_response(api_url):
    json_response = ""
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        # access JSOn content
        json_response = response.json()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    
    return json_response

# Clean Json response to split the datetime into Year and month
def create_year_month(json_response):
    for item in json_response:
        split_datetime = item['Date'].split("T")
        date_time_obj = datetime.strptime(split_datetime[0], '%Y-%m-%d')
        split_date = str(date_time_obj).split("-")
        item['Year'] = split_date[0]
        item['Month'] = split_date[1]
        
    return json_response

# Extracting total covid case for each month and removing the confirmed cases of the previous month
def get_total_covid_case(json_response):
    # Initialise variables to be used
    year = ""
    month = ""
    prev_date_str = ""
    covid_case_dict = {}
    current_total_case = 0
    total_covid_case = 0

    for index, item in enumerate(json_response):
        if year == "":
            year = item['Year']
            month = item['Month']

        elif year != item['Year'] or month != item['Month']:
            new_date_str = year + "-" + month
            if not covid_case_dict:
                total_covid_case = json_response[index-1]['Confirmed']
                current_total_case = json_response[index-1]['Confirmed']
                covid_case_dict[new_date_str] = current_total_case
            else:
                current_total_case = json_response[index-1]['Confirmed'] - total_covid_case
                total_covid_case = json_response[index-1]['Confirmed']
                covid_case_dict[new_date_str] = current_total_case

            year = item['Year']
            month = item['Month']
            prev_date_str = new_date_str

        if index == len(json_response)-1:
            new_date_str = year + "-" + month
            # total_covid_case = total_covid_case + json_response[index]['Confirmed']
            current_total_case = json_response[index]['Confirmed'] - total_covid_case
            covid_case_dict[new_date_str] = current_total_case

    return covid_case_dict

# Main Method to consolidate the methods for preprocessing json data
def main_preprocess(api_url):
    json_response = get_json_response(api_url)
    json_response = create_year_month(json_response)
    covid_case_dict = get_total_covid_case(json_response)
    return covid_case_dict