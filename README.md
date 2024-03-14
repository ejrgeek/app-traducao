# Mini Tradutor de Textos

## Descrição do Projeto
Permite aos utilizadores digitar um texto em um idioma e traduzi-lo automaticamente para outro idioma usando a biblioteca de tradução do Google Translate.

OBS: A biblioteca ```googletrans``` utiliza a API pública do Google Tradutor, é importante notar que **haverá diferenças** entre a tradução fornecida pela biblioteca e a tradução exata no site do Google Tradutor. A biblioteca é uma interface para a API e vai ocorrer variações na qualidade da tradução.

Para obter traduções consistentes como a do Google Tradutor, você pode usar da biblioteca ```google-cloud-translate``` no lugar da ```googletrans```. A biblioteca ```google-cloud-translate``` requer autenticação e a configuração de uma conta de serviço do Google Cloud.

## Como Executar

1. Certifique-se de ter o Python 3.7 ou superior instalado.

2. Clone o repositório para o seu ambiente local.
```
git clone git@github.com:2wo-Labs/app-traducao.git
```

3. Instale as dependências usando o comando:
```
pip install -r requirements.txt
```

4. Execute o aplicativo utilizando o comando:
```
streamlit run app.py
```

5. O aplicativo será aberto em seu navegador padrão. Você pode interagir com as diferentes funcionalidades do sistema.


## Funcionalidade

- Traduzir texto para outros idiomas


## Screenshots (GIF)

****

![Traduzindo texto](screenshots/traducao.gif)

O GIF mostra como funcionam o sistema.


## Dependências

O sistema depende das seguintes bibliotecas Python:

- streamlit
- googletrans==4.0.0-rc1

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request com melhorias ou correções.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
