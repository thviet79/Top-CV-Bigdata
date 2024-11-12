# Define a headers dictionary to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive'
}

def get_titles(list_link):
    titles = []
    for link in list_link:
        response = requests.get(link, headers=headers)  # Add headers here
        if response.status_code == 403:
            print("Access denied on:", link)
            continue
        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.findAll('h3', class_='title')
        for tit in title:
            titles.append(tit)
    return titles

def crawl_contents(filename, links_company):
    setup_file(filename, False)
    deli = ""

    for link in links_company:
        news = requests.get(link, headers=headers)  # Add headers here
        if news.status_code == 403:
            print("Access denied on:", link)
            continue
        soup = BeautifulSoup(news.content, "html.parser")
        names_obj = soup.find('a', class_="company-logo")
        if names_obj is None:
            continue
        names = names_obj.attrs["title"]
        contents = soup.find("div", class_="job-data")

        data = {}
        data['name'] = names
        add_contents(contents, data)
        print("Response status:", response.status_code)  # Check if the response is 200
        print("Fetched titles:", title)  # After fetching titles

        write_file(filename, data, deli)
        deli = ",\n"
        print(data)
    setup_file(filename, True)
