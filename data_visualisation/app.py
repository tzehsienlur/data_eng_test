from preprocess_json import main_preprocess
from data_visualisation import plot_barchart

if __name__ == "__main__":
    api_url = 'https://api.covid19api.com/total/country/singapore'
    barchart_columns = ['Date', 'Total Covid Case For Each Month']
    covid_case_dict = main_preprocess(api_url)
    plot_barchart(covid_case_dict, barchart_columns)