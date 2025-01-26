# API com Flask e SQLAlchemy

Este projeto é uma aplicação simples utilizando **Flask** e **SQLAlchemy** para criar uma API que interage com um banco de dados. Ele tem três arquivos principais:

- **`entidades.py`**: Contém as entidades do banco de dados, mapeadas com SQLAlchemy.
- **`dao.py`**: Responsável pelas consultas e operações de acesso ao banco de dados.
- **`app.py`**: Contém o servidor Flask que expõe as interações via API.

### Detalhes Importantes:
* É necessário criar o banco de dados postgre primeiro, e configurar corretamente a string de conexão.
* O psycopg2-binary é o drive de conexão e é necessario para que o python consiga se comunicar com o PosgreSQL
* Esse código contem dois metodos HTTP que interagem com a entenidade 'tema':
    * get /temas: captura todos os temas disponiveis.
    * post /temas: para incluir um novo registro.