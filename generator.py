from bs4 import BeautifulSoup

import Blockchain


def user_page(DataBase, login, token):
    soup = BeautifulSoup(open('global_styles/home.html'), 'html.parser')
    result = soup.find(id='home_nic_container')
    result=result.find(id="home_nic")
    result.string.replace_with(login)
    with open("templates/home.html", "w") as file:
        file.write(str(soup))
DataBase=Blockchain.Blockchain()
