from bs4 import BeautifulSoup
import requests, openpyxl

excel=openpyxl.Workbook()
sheet=excel.active
sheet.title="Movies"
sheet.append(['S.No','Movie_Title','Year','Rating','Description'])

# URL of the page to scrape
url = 'https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=adventure&sort=user_rating,desc'  # A simple test URL

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}

# Send an HTTP request
response = requests.get(url, headers=headers)


try:
    # Check if the request was successful
    if response.status_code == 200:

        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        movieslist=soup.find_all("li",class_='ipc-metadata-list-summary-item')
        for movie in movieslist:
             movie_title=movie.find('h3',class_="ipc-title__text").text.split(" ")
             m_title=""
             for title in movie_title[1:]:
                  m_title+=title+" "
             movie_year=movie.find('span',class_="dli-title-metadata-item").text
             rating=movie.find('span',class_="ipc-rating-star--rating").text
             description=movie.find('div',class_="ipc-html-content-inner-div").text
            #  print(movie_title[0][0:-1],m_title,movie_year,rating,description)
            #  print()
            #  print()
             sheet.append([movie_title[0][0:-1],m_title,movie_year,rating,description])
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
except Exception as e:
        print(e)

excel.save("Movies.xlsx")