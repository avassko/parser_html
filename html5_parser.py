from bs4 import BeautifulSoup
import requests
import time

input_year = str(input('Input one or few (separated by a space) year "1930-2023" or "all" for parsing music: '))

info = []


def music_parser(year_of_music):
    url = "https://radiopotok.ru/best_songs/" + str(year_of_music)
    print(f'The music of {year_of_music} is being processed!')
    response = requests.get(url)
    html_soup = BeautifulSoup(response.text, "html.parser")
    music_data = html_soup.find_all('div', class_='theme-surface video-item mb-3 js--video-item')
    info.extend(music_data)


if len(input_year) > 4:
    years = input_year.split(" ")
    for year in years:
        if year.isnumeric() is True and 1930 <= int(year) <= 2023:
            music_parser(year)
            time.sleep(1)
        else:
            print(f'{year} not in a list year or word is incorrect!')
            exit()
    for number_music in range(len(info)):
        print(info[number_music].find('h3', class_='block primary p-2 leading-tight text-lg').text)
    exit()
if input_year == "all":
    for i in range(1930, 2024):
        music_parser(i)
    for number_music in range(len(info)):
        print(info[number_music].find('h3', class_='block primary p-2 leading-tight text-lg').text)
elif input_year.isnumeric() is True and 1930 <= int(input_year) <= 2023:
    music_parser(input_year)
    time.sleep(1)
    for number_music in range(len(info)):
        print(info[number_music].find('h3', class_='block primary p-2 leading-tight text-lg').text)
else:
    print(f'{input_year} not in a list year or word is incorrect!')
