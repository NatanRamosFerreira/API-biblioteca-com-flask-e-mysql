USE natanramosferreira;

CREATE TABLE livros (
    id integer not null auto_increment,
    titulo varchar(100),
    autor varchar(100),
    PRIMARY KEY (id)
);

SET character_set_client = utf8;
SET character_set_connection = utf8;
SET character_set_results = utf8;
SET collation_connection = utf8_general_ci;

INSERT INTO livros (titulo, autor) VALUES ('O Senhor dos Anéis - A Sociedade do Anel', 'J.R.R Tolkien');
INSERT INTO livros (titulo, autor) VALUES ('Harry Potter e a Pedra Filosofal', 'J. K. Rowling');
INSERT INTO livros (titulo, autor) VALUES ('Harry Potter e a Câmara Secreta', 'J. K. Rowling');
