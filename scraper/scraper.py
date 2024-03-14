import requests, time, os
from bs4 import BeautifulSoup 
from selenium import webdriver

years = ["2015", "2016", "2017"]
base_url = "http://cs231n.stanford.edu/"

# Initiate the webdriver.
driver = webdriver.Safari('/usr/bin/safaridriver')
# driver = webdriver.Chrome('./chromedriver')

for year in years:
    url = base_url + year + "/reports.html"

    driver.get(url)
    time.sleep(5)
    html = driver.page_source

    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("a", href=lambda x: x and x.endswith(".pdf"))
    links = [link.get('href') for link in links if 'pdfs' in link.get('href')]

    if year == '2017':
        # Modify each link to include the full URL
        links = [base_url + link.replace('../', '') for link in links]
        links = list(set(links))

    # Directory where you want to save the downloaded PDFs
    download_directory = './scraper/Downloads/' + year + '/'
    os.makedirs(download_directory, exist_ok = True)

    # Download each PDF
    for i, url in enumerate(links):
        # Get the file name by splitting the URL
        file_name = url.split('/')[-1]
        
        # Full path to save the file
        file_path = os.path.join(download_directory, file_name)
        
        # Make the GET request to download the PDF
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Write the content to the file
            with open(file_path, 'wb') as file:
                file.write(response.content)
            print(f'({i}/{len(links)}) Downloaded {url}')
        else:
            print(f'({i}/{len(links)}) Failed to download {url}')

# Closing the webdriver
driver.close()