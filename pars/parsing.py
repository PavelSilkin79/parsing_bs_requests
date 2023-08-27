import requests
from bs4 import BeautifulSoup as bs
# получаем код страницы
get_html = requests.get('https://books.toscrape.com/')
#get_html.status_code
html = get_html.content
#html
soup = bs(html, 'html.parser')
soup
sections = soup.select('section')
sections
section = sections[0]
books_block = section.select_one('ol[class=row]')
books_block
books = books_block.select('li')
#print(len(books))
books_data = []
for book in books:
    image = 'https://books.toscrape.com/' + book.find('div', attrs={'class': 'image_container'}).find('img')['src']
    title = book.find('h3').find('a')['title']
    price = book.find('p', attrs={'class': 'price_color'}).text
   
    book_dict = {
		'image': image,
        'title': title,
        'price': price
	}
    books_data.append(book_dict)
    
print(books_data[10])
   