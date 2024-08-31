from bs4 import BeautifulSoup
import requests

# URL of the page to scrape
url = 'https://www.imdb.com/search/title/?genres=Adventure&sort=user_rating,desc&title_type=feature&num_votes=25000,&ref_=chttp_gnr_1'  # A simple test URL

# Send an HTTP request
response = requests.get(url)
print(response.text)

try:
    # Check if the request was successful
    if response.status_code == 200:

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the title using .string
        title_string = soup.title.string
        print('Title using .string:', title_string)

        # Extract the title using .text
        title_text = soup.title.text
        print('Title using .text:', title_text)
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
except Exception as e:
        print(e)

