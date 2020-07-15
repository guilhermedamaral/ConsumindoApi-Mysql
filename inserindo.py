import mysql.connector
import requests

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="lojan"
)

cursor = banco.cursor()

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

resposta = requests.get('https://api.github.com/users')

for res in resposta.json():
#    cursor.execute
    login = (res['{}'.format('login')])
    id = (res['{}'.format('id')])
    node_id = (res['{}'.format('node_id')])
    avatar_url = (res['{}'.format('avatar_url')])
    gravatar_id = (res['{}'.format('gravatar_id')])
    url = (res['{}'.format('url')])
    html_url = (res['{}'.format('html_url')])
    followers_url = (res['{}'.format('followers_url')])
    following_url = (res['{}'.format('following_url')])
    gists_url = (res['{}'.format('gists_url')])
    starred_url = (res['{}'.format('starred_url')])
    subscriptions_url = (res['{}'.format('subscriptions_url')])
    organizations_url = (res['{}'.format('organizations_url')])
    repos_url = (res['{}'.format('repos_url')])
    events_url = (res['{}'.format('events_url')])
    received_events_url = (res['{}'.format('received_events_url')])
    type = (res['{}'.format('type')])
    site_admin = (res['{}'.format('site_admin')])

    cursor.execute('INSERT INTO usuario (login,id,node_id,avatar_url,gravatar_id,url,html_url,followers_url,following_url,gists_url,starred_url,subscriptions_url,organizations_url,repos_url,events_url,received_events_url,type,site_admin) Values ("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")'.format(login,id,node_id,avatar_url,gravatar_id,url,html_url,followers_url,following_url,gists_url,starred_url,subscriptions_url,organizations_url,repos_url,events_url,received_events_url,type,site_admin))
