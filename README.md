# Jogo de Blackjack

Este é um projeto de software que implementa um jogo de Blackjack em Python. O jogo segue as regras tradicionais do Blackjack, onde o jogador compete contra o dealer para chegar o mais próximo possível de 21 sem ultrapassá-lo.

## Estrutura do Projeto

O projeto é organizado da seguinte forma:

``` bash
.
└── src
    ├── controllers
    │   ├── __init__.py
    │   └── gameController.py
    ├── models
    │   ├── __init__.py
    │   ├── card.py
    │   ├── deck.py
    │   └── game.py
    └── views
        ├── __init__.py
        └── gameView.py
```

- `controllers`: Contém o controlador do jogo, responsável por controlar o fluxo do jogo.
- `models`: Contém as classes que representam os componentes do jogo, como cartas, baralho e o próprio jogo.
- `views`: Contém a classe responsável pela visualização do jogo.

## Como Jogar

### Baixar o repositório do jogo de Blackjack

``` bash
git clone https://github.com/samuelncaetano/blackjack_python
cd blackjack_python
```

### Baixar o ambiente virtual

``` bash
pip3 install virtualenv
```

### Inicializar o ambiente virtual

``` bash
virtualenv -p python3 venv
```

### Ativar o ambiente virtual

``` bash
source venv/bin/activate
```

### Baixar todos os pacotes necessários

``` bash
venv/bin/pip3 install -r requirements.txt
```

### Executar o jogo de Blackjack

Para iniciar o jogo, execute o arquivo `gameController.py`. Você será apresentado com as opções disponíveis, incluindo "Hit" (pedir uma carta adicional), "Stand" (manter a mão atual) e "Quit" (sair do jogo).

``` bash
python3 src/controllers/gameController.py
```

## Funcionalidades

- O jogo segue as regras padrão do Blackjack.
- O jogador pode solicitar uma nova carta ("Hit") ou manter sua mão atual ("Stand").
- O jogo termina quando o jogador decide parar ("Stand") ou ultrapassa 21 pontos ("bust").
- Após o término do jogo, o jogador tem a opção de reiniciar ou sair do jogo.

## Como executar os testes

Para executar os testes, basta navegar até o diretório raiz do projeto e executar o pytest:

``` bash
pytest
```

Isso executará todos os testes no diretório de testes padrão. Se você quiser executar testes específicos ou de um determinado arquivo, pode passar o caminho para o arquivo como um argumento para o pytest.

Para executar os testes de forma mais detalhada, basta navegar até o diretório raiz do projeto e executar o pytest com a opção -v:

``` bash
pytest -v
```

### Verificar Cobertura de Código

Além de executar os testes, é útil verificar a cobertura de código para garantir que todos os aspectos do código estejam sendo testados adequadamente. Certifique-se de ter executado os testes primeiro para que o coverage possa analisar os resultados dos testes.

``` bash
coverage run -m pytest
```

Depois de executar o coverage, você pode gerar um relatório de cobertura para visualizar a porcentagem de código testada e identificar áreas que precisam de mais testes.

``` bash
coverage report
```

Isso exibirá um relatório detalhado mostrando a cobertura de cada arquivo do projeto. Além de verificar a cobertura de código através do relatório textual, você também pode gerar um relatório HTML mais detalhado para uma análise mais aprofundada.

### Gerar Relatório HTML

``` bash
coverage html
```

Isso criará um diretório chamado `htmlcov` contendo arquivos HTML que representam a cobertura de código do seu projeto.

### Visualizar Relatório HTML

Você pode visualizar o relatório HTML abrindo o arquivo `index.html` no diretório `htmlcov` em seu navegador da web. Isso fornecerá uma visualização mais detalhada da cobertura de código, incluindo métricas específicas e uma representação gráfica da cobertura por arquivo. Com o relatório HTML, você pode identificar áreas específicas do código que precisam de mais testes e tomar medidas para melhorar a cobertura de código do seu projeto.

## Desenvolvedores

- [samuelncaetano](https://github.com/samuelncaetano) - Desenvolvedor principal

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT).
