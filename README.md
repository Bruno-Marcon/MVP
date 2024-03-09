# livraria

Este é um aplicativo web simples construído em Flask para gerenciar um catálogo de livros. Os usuários podem adicionar, editar e excluir livros do catálogo.

# Estrutura
 A aplicação segue o padrão arquitetônico Model-View-Presenter (MVP), dividindo responsabilidades para melhor organização do código.

*app.py: Contém a configuração e roteamento da aplicação Flask.*

*models.py: Define o modelo SQLAlchemy para a entidade Book.*

*book_catalog.html: Modelo HTML para renderizar a página web do catálogo de livros.*

# Componentes do MVP

Model (BookCatalogModel): Manipula dados e interage com o banco de dados.

View (BookCatalogView): Responsável por renderizar a interface do usuário.

Presenter (BookCatalogPresenter): Conecta o Model e a View, lidando com a entrada do usuário e atualizando a interface.

# Funcionalidades
Adicionar Livro: Os usuários podem incluir novos livros no catálogo.

Editar Livro: Permite aos usuários modificar o título de um livro existente.

Excluir Livro: Possibilita a exclusão de um livro do catálogo.

# Banco de Dados

A aplicação utiliza o SQLite como banco de dados, armazenando as informações no arquivo book_catalog.db.
