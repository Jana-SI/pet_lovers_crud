create table if not exists cliente(
    id serial primary key not null,
    cpf varchar(11) unique not null,
    nome varchar(50) not null,
    telefone varchar(20) not null,
    numPet smallint check(numPet>=0) default 0
);

create table if not exists pet(
    id serial primary key not null,
    nome varchar(50) not null,
    nascimento date not null,
    raca varchar(50) not null,
    tipo varchar(50) not null
);

create table if not exists donoPet(
    id serial primary key not null,
    cpfCliente int references cliente(cpf),
    idPet int references pet(id) 
);

create table if not exists Consulta(
    id serial primary key not null,
    idDonoPet int references donoPet(id),
    data date not null
);