# Ária da Eutimia Onírica

Site do RPG de fantasia sombria e feérica ambientado no passado do universo de um livro em desenvolvimento. Reúne a campanha atual, missões, regiões, personagens, crônicas, arsenal, grimório e trilhas sonoras.

## Executar localmente

O site é estático e não exige instalação de dependências. Na raiz do projeto, execute:

```sh
python -m http.server 8000 --directory docs
```

Abra http://localhost:8000 no navegador. Também é possível abrir `docs/index.html` diretamente.

## Estrutura

- `docs/index.html`: página do RPG e conteúdo da campanha.
- `docs/css/style.css`: identidade visual e layout responsivo.
- `docs/assets/`: imagens e capas das playlists.
- `docs/CNAME`: domínio personalizado `walpurgis.uk`.
- `archive/tcc/`: proposta, referências e protótipo Python do projeto acadêmico anterior; não fazem parte do site.

## Publicação

Para publicação com GitHub Pages, use a pasta `/docs` da branch escolhida no repositório. O arquivo CNAME mantém o domínio personalizado; a configuração de DNS é feita no provedor do domínio.

## Conteúdo e cronologia

O foco é a campanha de RPG. Seus acontecimentos antecedem a narrativa do livro em desenvolvimento. O site não apresenta o enredo futuro do livro nem presume datas ou relações entre eventos que ainda não foram definidas pelo autor.

Consulte [CONTRIBUTING.md](CONTRIBUTING.md) para orientações de edição.
