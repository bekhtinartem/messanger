from bs4 import BeautifulSoup

def user_page(DataBase, login, token):
    soup = BeautifulSoup(open('global_styles/home.html'), 'html.parser')
    result = soup.find(id='home_nic')
    result.string.replace_with(login)
    result=soup.find(id="home_name")
    result.string.replace_with(login)
    result=soup.find(id="home_to_messages")
    string = '<form id = "auth_reg" action="/home/mes' +'" method="GET" id="home_to_messages"><button name="code" value='+login+'&token='+token+'>Сообщения</button></form>'
    print(string)
    result.replace_with(BeautifulSoup(string))
    print(str(result))
    with open("templates/home.html", "w") as file:
        file.write(str(soup))


def mes_page(DataBase, login, token):
    soup = BeautifulSoup(open('global_styles/mes.html'), 'html.parser')
    p_tag = soup.new_tag("p")
    p_tag.string = 'This is the new paragraph'
    soup.body.append(p_tag)
    with open("templates/mes.html", "w") as file:
        file.write(str(soup))