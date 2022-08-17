import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import sklearn


"""
    Works for imdb pages recommend using all the pages with genres informations 
    discards all the ones with less then 3 genre type
"""



def get_all_titles(soup):
    result_topics = []
    all_topics = soup.find_all('h3', {'class': 'lister-item-header'})

    # print(all_topics)
    for topic in all_topics:

        topic = topic.find('a').text

        # topic = str(topic.find('a'))
        # topic = topic.replace('<', '=')
        # topic = topic.replace('>', '=')
        # topic = topic.split('=')
        # topic = topic[int(len(topic)/2)]
        result_topics.append(topic)

    # print(result_topics)
    return result_topics

def get_all_genres(soup):
    result_genre = []
    all_genre = soup.find_all('p', {"class": 'text-muted'})
    # print(all_genre)

    for genre in all_genre:
        genre = str(genre.find_all('span', {'class': 'genre'}))
        if genre == '[]':
            pass
        else:
            genre = genre.replace('<', '=')
            genre = genre.replace('>', '=')
            genre = genre.split('=')
            genre = genre[int(len(genre)/2)]
            result_genre.append(genre)

    return result_genre



def post_process(genres):
    post_process_genre = []
    for i in genres:
        i = i.replace('\n', '')
        i = i.replace(' ', '')
        post_process_genre.append(i)
    return post_process_genre


def check_repeated_comma(x):
    list_x = x.split(',')
    if len(list_x) == 3:
        return x
    else:
        return np.nan


def data_set(url):

    data_set = pd.DataFrame(columns = ["Movies", "Primary_Genre", "Secondary_Genre", "Tertiary_Genre"])

    # Initially get the page from the url and from the content extract all the things properly so page is extracetd
    page = requests.get(url)
    # Soup is created where all the content is parsed as html format so it can be extracted as seen in webpages. 
    soup = BeautifulSoup(page.content, 'html.parser')

    
    title = get_all_titles(soup)
    genres = get_all_genres(soup)
    genres = post_process(genres)

    data_set["Movies"] = pd.Series(title)
    data_set["Primary_Genre"] = pd.Series(genres)
    data_set["Primary_Genre"] = data_set["Primary_Genre"].apply(check_repeated_comma)
    data_set["Secondary_Genre"] = data_set["Secondary_Genre"].fillna('To be filled')
    data_set["Tertiary_Genre"] = data_set["Tertiary_Genre"].fillna('To be filled')

    data_set = data_set.loc[data_set["Primary_Genre"] != np.NaN]
    data_set = data_set.dropna(how = 'any')

    data_set[["Primary_Genre", "Secondary_Genre", "Tertiary_Genre"]] = data_set['Primary_Genre'].str.split(',', expand=True)

    data_set.to_csv('Dataset.csv', mode = 'a', header=False)

    # print(data_set.head())


if __name__ == "__main__":
    import os
    os.system('clear')
    print('IMDB Scraper')
    # number_of_pages = int(input('Enter the number of various pages to scrap: '))
    # for i in range(number_of_pages):
    #     url = input('Enter a URL: ')
    #     data_set(url)
    number_of_genres  = int(input("Enter number of genres to scrap: "))
    for i in range(number_of_genres):
        genre = input('Enter a genre: ')
        url1 = "https://www.imdb.com/search/title/?title_type=feature&genres="+genre
        data_set(url1)
        more = input("Do you want to scrap more of "+genre+" genre(y/n): ")
        if more == "y":
            url2 = "https://www.imdb.com/search/title/?title_type=feature&genres="+genre+"&start=51&ref_=adv_nxt"
            data_set(url2)
