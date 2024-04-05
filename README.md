# Web Scraping Job Vacancies from Starbucks Careers API

This repository contains a Python script to scrape job vacancies from the Starbucks Careers API. The script utilizes the `requests` library to fetch data from the API endpoint, then parses the response into JSON format. The JSON data is normalized into a pandas DataFrame using `pd.json_normalize`, and finally, the collected data is saved into a CSV file.

## Process

1. **Fetching Data**: The script sends a GET request to the Starbucks Careers API endpoint to retrieve job vacancy information.

2. **Parsing Response**: The response from the API is in JSON format. The script parses this JSON data to extract relevant job vacancy details.

3. **Data Normalization**: Using `pd.json_normalize`, the JSON data is converted into a pandas DataFrame, allowing for easier manipulation and analysis.

4. **Saving Data**: The collected job vacancy data, including VacancyID, jobTitle, jobCategory, jobFunction, jobLevel, country, stateProvince, city, postalCode, lat, lng, and Distance, is saved into a CSV file.

## Data Fields

- `VacancyID`: Unique identifier for each job vacancy.
- `jobTitle`: Title of the job.
- `jobCategory`: Category of the job.
- `jobFunction`: Function of the job.
- `jobLevel`: Level of the job.
- `country`: Country where the job is located.
- `stateProvince`: State or province where the job is located.
- `city`: City where the job is located.
- `postalCode`: Postal code of the job location.
- `lat`: Latitude coordinate of the job location.
- `lng`: Longitude coordinate of the job location.
- `Distance`: Distance of the job location from a specified point (if available).

## Usage

1. Clone the repository to your local machine.
2. Ensure you have Python installed.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Run the `job_vaccancies.py` script.
5. Once the script finishes execution, you will find the scraped job vacancy data saved in a CSV file named `grande_careers.csv`.

## Note

- This script is provided for educational and informational purposes only. Usage of this script to scrape data from the Starbucks Careers API should comply with Starbucks' terms of service and data usage policies.

Feel free to explore and adapt the script as needed for your own projects or analysis. If you encounter any issues or have suggestions for improvement, please open an issue or submit a pull request. Contributions are welcome!

### website view

![image](https://github.com/FaeyO/webscrapping-job-vacancies-from-starbuckscareers.api/assets/118575325/b9d30f33-c142-4c28-9b2c-55c153eead3c)
