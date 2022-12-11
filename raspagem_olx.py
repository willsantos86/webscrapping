import sqlite3
from requests_html import HTMLSession

sessao = HTMLSession()
imoveis = []
url = "https://www.olx.com.br/imoveis/aluguel/estado-sp/sao-paulo-e-regiao" #Acessa a pagina web
resposta = sessao.get(url)
links = resposta.html.find("#ad-list li a")
for link in links:
    url_imovel = link.attrs['href']
    resposta_imovel = sessao.get(url_imovel)
    titulo = resposta_imovel.html.find('h1', first=True).text
    preco = resposta_imovel.html.find('h2')[2].text
    imoveis.append({
        'url': url_imovel,
        'titulo': titulo,
        'preco': preco
    })
   
conexao = sqlite3.connect("banco.sqlite3")
cursor = conexao.cursor()
sql = 'insert into imovel (url, titulo, preco) values (?, ?, ?)'
for imovel in imoveis:
    valores = [imovel['url'], imovel['titulo'], imovel['preco']]
    cursor.execute(sql, valores)
conexao.commit()
conexao.close()
