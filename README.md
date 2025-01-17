# Sistema de Cadastro de Produtos

Este é um projeto de cadastro de produtos desenvolvido em Python durante graduação na Gran Faculdades, utilizando os conceitos de **acoplamento** e **coesão**. O programa permite realizar operações básicas de CRUD (Criar, Consultar, Alterar e Excluir) em uma base de dados simples armazenada em um arquivo de texto.

## 📋 Funcionalidades

- **Incluir produto**: Adiciona um novo produto ao sistema.
- **Consultar produto**: Busca informações de um produto pelo código.
- **Alterar produto**: Permite modificar os dados de um produto existente.
- **Excluir produto**: Remove um produto do sistema.
- **Listar produtos**: Exibe todos os produtos cadastrados.

## 🛠️ Estrutura do Projeto

O projeto é composto por três arquivos principais:

1. **`produto.py`**  
   Contém a classe `Produto`, que define os atributos e métodos relacionados a um produto.

2. **`gerenciador_produtos.py`**  
   Contém a classe `GerenciadorProdutos`, responsável por manipular o arquivo de texto onde os produtos são armazenados. Implementa as operações de CRUD e garante a integridade dos dados.

3. **`main.py`**  
   Arquivo principal que exibe o menu e interage com o usuário. Usa as classes `Produto` e `GerenciadorProdutos` para executar as funcionalidades.

## 📦 Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/sistema-cadastro-produtos.git


2. Acesse o diretório:
   ```bash
   cd sistema-cadastro-produtos


3. Certifique-se de que você tem o Python 3 instalado:
   ```bash
   python --version


4. Execute o programa:
   ```bash
   python main.py



📝 Uso

Ao executar o programa, será exibido um menu com as opções disponíveis:

1. Incluir produto
2. Consultar produto
3. Alterar produto
4. Excluir produto
5. Listar produtos
6. Sair

Escolha a opção desejada e siga as instruções fornecidas pelo sistema.

📂 Estrutura do Arquivo de Dados

Os produtos são armazenados em um arquivo de texto (lista_produtos.txt), no seguinte formato:

codigo;nome;quantidade;valor_unitario
001;Caneta Azul;100;1.50
002;Caderno;50;10.00

Cada linha representa um produto.

🤝 Contribuindo

Contribuições são bem-vindas! Se você encontrou um problema ou tem sugestões de melhoria, faça um fork do projeto.


🛡️ Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais informações.

📧 Contato

Se tiver dúvidas ou sugestões, sinta-se à vontade para entrar em contato:

Email: klausmachado1@gmail.com 

GitHub: KlausMachado 

