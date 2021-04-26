''' 
    Webscrapper for top league champs in the top lane from op.gg.
'''

from urllib.request import urlopen as uRequeset
from bs4 import BeautifulSoup as soup
from datetime import date


def get_champ_rank(index):
    return champ_container.contents[index].td.text

def get_champ_name(index):
    return champ_container.contents[index].find("td", class_="champion-index-table__cell champion-index-table__cell--champion").div.string

def get_champ_wr(index):
    return champ_container.contents[index].find("td", class_="champion-index-table__cell champion-index-table__cell--champion").next_sibling.next_sibling.text

def del_empty_elems():
    to_del = champ_container.contents[0]

    for index, child in enumerate(champ_container.children):
        #idk why .contents list gives me a empty elem every even number, so i just did this. I think its bc html elems are separated by \n
        if child == to_del:
            del champ_container.contents[index]

def write_date():
    today = date.today()

    f.write("Date written:" + ',' + str(today) + ',' + "\n")


site_url = 'https://na.op.gg/champion/statistics'
file_name = "./opgg_champs.csv"
f = open(file_name, "w")

header = "rank, champ_name, wr,\n"

f.write(header)

uClient = uRequeset(site_url)
# the entire html
page_html = uClient.read() 
uClient.close()

# parse html
page_soup = soup(page_html, "html.parser") 

# get the tbody html tag
champ_container = page_soup.select("tbody.champion-trend-tier-TOP.tabItem")[0]
del_empty_elems()

for index in range(len(champ_container)):
    f.write(get_champ_rank(index) + ',' + get_champ_name(index) + ',' + get_champ_wr(index) + ',' + "\n")
print('done writting to file')

write_date()

f.close()





