# ConsumindoApi-Mysql
Projeto onde peguei os dados da API e transferi para um banco do mysql

Comandos da criação da table ultilizada no Banco mySQL \/

create database lojan;
use lojan;

create table usuario (
login varchar(200),
id varchar(200),
node_id varchar(200),
avatar_url varchar(200),
gravatar_id varchar(200),
url varchar(200),
html_url varchar(200),
followers_url varchar(200),
following_url varchar(200),
gists_url varchar(200),
starred_url varchar(200),
subscriptions_url varchar(200),
organizations_url varchar(200),
repos_url varchar(200),
events_url varchar(200),
received_events_url varchar(200),
type varchar(200),
site_admin varchar(200)
);
