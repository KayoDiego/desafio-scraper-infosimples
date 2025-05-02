#  Desafio Scraper - Infosimples

Este projeto é um scraper feito com Python que acessa uma página de produto e salva as informações em um arquivo `.json`.

##  O que o script faz?

Ele acessa a seguinte página:

```
https://infosimples.com/vagas/desafio/commercia/product.html
```

E coleta os seguintes dados:
- Título do produto
- Marca
- Categorias
- Descrição
- Lista de SKUs (variações do produto)
- Propriedades técnicas
- Avaliações de usuários
- Média das avaliações

Tudo é salvo em um arquivo chamado `produto.json`.

---

##  Requisitos

Você precisa ter Python instalado 
Além disso, instale os seguintes pacotes:

```bash
pip install beautifulsoup4 requests
```

---

##  Como rodar

1. Baixe o script `scraper.py` ou copie o código do repositório.
2. No terminal ou CMD, vá até a pasta onde está o arquivo.
3. Execute o comando:

```bash
python scraper.py
```

Se tudo der certo, ele vai criar o arquivo `produto.json` com os dados extraídos da página.

---

##  Estrutura do JSON gerado

O arquivo `produto.json` terá uma estrutura parecida com esta:

```json
{
  "url": "https://infosimples.com/vagas/desafio/commercia/product.html",
  "title": "Rubber Duck MK Ultra",
  "brand": "Duck Makers Inc.",
  "categories": [
    "Commercia",
    "Health & Care",
    "Bath",
    "Rubber Ducks"
  ],
  "description": "Apresentando os Patos de Borracha Quânticos, a última palavra em diversão aquática! Criados pelo excêntrico Dr. Quacksalot, esses patinhos de borracha vão além do comum, com habilidades de fala, dança e personalidades únicas. Com sua durabilidade de alta qualidade, esses patos são garantia de diversão interminável na banheira. Escolha entre uma variedade de cores e estilos e mergulhe na loucura científica do Dr. Quacksalot hoje mesmo! Cada Patinho de Borracha Quântico vem equipado com um sistema de comunicação interdimensional, permitindo que eles conversem não apenas entre si, mas também com outros objetos inanimados no banheiro - prepare-se para diálogos improváveis entre seu pato de borracha e o sabonete! Além disso, esses patos têm uma habilidade secreta de transformação: basta apertar sua barriguinha e assistir enquanto se transformam em mini submarinos de borracha, prontos para explorar os confins da banheira em busca de aventuras subaquáticas surreais. Com os Patos de Borracha Quânticos, o limite da diversão é apenas sua imaginação (e talvez a sanidade do Dr. Quacksalot)!",
  "skus": [
    {
      "name": "Rubber Duck MK Ultra - Original",
      "current_price": 12.68,
      "old_price": 16.98,
      "available": true
    },
    {
      "name": "Rubber Duck MK Ultra - Summer Version",
      "current_price": null,
      "old_price": null,
      "available": false
    },
    {
      "name": "Rubber Duck MK Ultra - Batman Version",
      "current_price": 18.98,
      "old_price": null,
      "available": true
    }
  ],
  "properties": [
    {
      "label": "Color",
      "value": "Various"
    },
    {
      "label": "Material",
      "value": "Rubber"
    },
    {
      "label": "Shape",
      "value": "Ducky"
    },
    {
      "label": "Size",
      "value": "Medium"
    },
    {
      "label": "Weight",
      "value": "394 g"
    },
    {
      "label": "Radioactivity Level",
      "value": "Low"
    },
    {
      "label": "Warranty",
      "value": "1 year"
    },
    {
      "label": "Nutritious value",
      "value": "-"
    },
    {
      "label": "Origin",
      "value": "Camboja"
    },
    {
      "label": "Allergenics",
      "value": "None"
    },
    {
      "label": "Recyclable?",
      "value": "Yes"
    },
    {
      "label": "Harmful?",
      "value": "No"
    },
    {
      "label": "Health benefits",
      "value": "None"
    },
    {
      "label": "Storage temperature",
      "value": "0 - 25ºC"
    },
    {
      "label": "Expiration date",
      "value": "None"
    },
    {
      "label": "Carbon footprint",
      "value": "65 g CO2"
    }
  ],
  "reviews": [
    {
      "name": "Louisa Eliel",
      "date": "2021-07-28",
      "score": 4,
      "text": "Very good rubber ducks, however I think they are a bit too big for me."
    },
    {
      "name": "Kairo Josué",
      "date": "2021-05-12",
      "score": 1,
      "text": "Péssima qualidade. Já não fazem patos de borracha como antigamente."
    },
    {
      "name": "Victor Huey",
      "date": "2021-04-03",
      "score": 5,
      "text": "Very good"
    }
  ],
  "reviews_average_score": 3.3
}
```

---

##  Observações

- Se algum dado não estiver presente na página, o script ignora ou preenche com `None` ou listas vazias.
- O script usa `try/except` para evitar que erros quebrem a execução.

---


##  Desenvolvidor por Kayo Diego

Desenvolvido para o desafio de scraping da Infosimples.
