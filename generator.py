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
    users=DataBase.get_connections(login, token)
    container=soup.find(id="messeges_container")
    for user in users:
        message=DataBase.get_messages(login, user, token, 1)
        upper_tag =  BeautifulSoup('<p >')
        div_tag = soup.new_tag('nav class="navbar navbar-light sticky-top bg-light flex-md-nowrap p-0"')
        p_tag = soup.new_tag('p align="left" class="navbar-brand  mr-15"')
        log_tag=BeautifulSoup("<h3>"+user+"</h3>")
        tag=BeautifulSoup('<img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava3.webp" alt="avatar" class="rounded-circle img-fluid" style="width: 80px;">')
        tag.name="image"
        tag.src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava3.webp"
        p_tag.append(log_tag)
        div_tag.append(tag)
        div_tag.append(p_tag)
        upper_tag.append(div_tag)
        string = '<form id = "message_'+user+'" action="/home/mes' + '" method="GET" id="home_to_messages"><button name="code" value=' + login + '&token=' + token + '>'+message[0]["message"]+'</button></form>'
        upper_tag.append(BeautifulSoup(string))
        container.append(upper_tag)

    with open("templates/mes.html", "w") as file:
        file.write(str(soup))