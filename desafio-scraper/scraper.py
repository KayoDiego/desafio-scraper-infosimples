from bs4 import BeautifulSoup
import requests
import json
from datetime import datetime

def pegar_dados_produto():
    # Pegar a página
    url = 'https://infosimples.com/vagas/desafio/commercia/product.html'
    pagina = requests.get(url)
    pagina.raise_for_status()
    
    # Analisar o HTML
    soup = BeautifulSoup(pagina.text, 'html.parser')
    
    # Objeto para guardar os dados
    dados = {
        "url": url,
        "title": None,
        "brand": None,
        "categories": [],
        "description": None,
        "skus": [],
        "properties": [],
        "reviews": [],
        "reviews_average_score": 0.0
    }
    
    # 1. Título do produto
    titulo = soup.find('h2', id='product_title')
    if titulo:
        dados['title'] = titulo.text.strip()
    
    # 2. Marca
    marca = soup.find('div', class_='brand')
    if marca:
        dados['brand'] = marca.text.strip()
    
    # 3. Categorias 
    navegacao = soup.find('nav', class_='current-category')
    if navegacao:
        for link in navegacao.find_all('a'):
            dados['categories'].append(link.text.strip())
    
    # 4. Descrição 
    descricao_div = soup.find('div', class_='proddet')
    if descricao_div:
        textos = [p.text.strip() for p in descricao_div.find_all('p')]
        dados['description'] = ' '.join(textos)
    
    # 5. SKUs 
    cards = soup.select('div.skus-area div.card')
    for card in cards:
        sku = {
            "name": None,
            "current_price": None,
            "old_price": None,
            "available": 'not-avaliable' not in card.get('class', [])
        }
        
        # Nome
        nome = card.find('div', class_='prod-nome')
        if nome:
            sku['name'] = nome.text.strip()
        
        # Preço atual
        preco_atual = card.find('div', class_='prod-pnow')
        if preco_atual:
            try:
                sku['current_price'] = float(preco_atual.text.replace('R$', '').replace(',', '.').strip())
            except:
                pass
        
        # Preço antigo
        preco_antigo = card.find('div', class_='prod-pold')
        if preco_antigo and preco_antigo.text.strip():
            try:
                sku['old_price'] = float(preco_antigo.text.replace('R$', '').replace(',', '.').strip())
            except:
                pass
        
        dados['skus'].append(sku)
    
    # 6. Propriedades das duas tables
    tabelas = soup.find_all('table', class_='pure-table')
    for tabela in tabelas:
        for linha in tabela.find_all('tr'):
            colunas = linha.find_all('td')
            if len(colunas) == 2:
                dados['properties'].append({
                    "label": colunas[0].text.strip(),
                    "value": colunas[1].text.strip()
                })
    
    # 7. Avaliações
    total_pontos = 0
    avaliacoes = soup.find_all('div', class_='analisebox')
    
    for av in avaliacoes:
        # Nome
        nome = av.find('span', class_='analiseusername')
        if not nome:
            continue
            
        # Data
        data = av.find('span', class_='analisedate')
        try:
            data_formatada = datetime.strptime(data.text.strip(), '%d/%m/%Y').strftime('%Y-%m-%d')
        except:
            continue
            
        # Estrelas
        estrelas = av.find('span', class_='analisestars')
        pontos = estrelas.text.count('★') if estrelas else 0
        
        # Texto
        texto = av.find('p')
        if not texto:
            continue
            
        dados['reviews'].append({
            "name": nome.text.strip(),
            "date": data_formatada,
            "score": pontos,
            "text": texto.text.strip()
        })
        total_pontos += pontos
    
    # 8. Média das avaliações
    if dados['reviews']:
        dados['reviews_average_score'] = round(total_pontos / len(dados['reviews']), 1)
    
    return dados

def salvar_json(dados, arquivo):
    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    try:
        dados_produto = pegar_dados_produto()
        salvar_json(dados_produto, 'produto.json')
        print("Dados salvos com sucesso no arquivo produto.json")
    except Exception as e:
        print("Ocorreu um erro:", e)