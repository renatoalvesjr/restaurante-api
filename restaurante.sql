create table restaurante (
	id serial NOT NULL UNIQUE PRIMARY KEY,
	nome varchar UNIQUE NOT NULL,
	endereco varchar UNIQUE NOT NULL,
	numero varchar(11) UNIQUE check(lenght(numero)==10 OR lenght(numero)==11) ,
	cnpj varchar(14) UNIQUE NOT NULL check(lenght(cnpj)==14),
	classificacao NUMERIC(2) check(classificacao>=0 AND classificacao<=5)
)