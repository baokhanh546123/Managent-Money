CREATE SCHEMA chat_app;

USE chat_app;

CREATE TABLE users (
    iduser INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL, 
    password VARCHAR(1000) NOT NULL, 
    phone VARCHAR(10) NULL,
    address VARCHAR(20) NULL, 
    fullname VARCHAR(20) NULL,
    times TIMESTAMP,
    PRIMARY KEY (iduser)
);

CREATE TABLE stoge_data (
    id INT NOT NULL AUTO_INCREMENT,
    iduser INT NOT NULL, 
    income FLOAT DEFAULT NULL, 
    tax_rate FLOAT DEFAULT NULL, 
    income_after FLOAT NOT NULL, 
    needs FLOAT NOT NULL,
    wants FLOAT NOT NULL,
    savings FLOAT NOT NULL,
    times TIMESTAMP,
    last_activity DATETIME DEFAULT NOW()
    PRIMARY KEY (id),
    FOREIGN KEY (iduser) REFERENCES users(iduser)
);

CREATE TABLE needs (
    iduser INT NULL, 
    ten VARCHAR(50) NULL, 
    cost FLOAT NULL,
    times TIMESTAMP,
    FOREIGN KEY (iduser) REFERENCES users(iduser)
);

CREATE TABLE wants (
    iduser INT NULL, 
    ten VARCHAR(50), 
    cost FLOAT,
    times TIMESTAMP,
    FOREIGN KEY (iduser) REFERENCES users(iduser)
);

CREATE TABLE savings (
    iduser INT NULL, 
    ten VARCHAR(50) NULL, 
    cost FLOAT NULL,
    times TIMESTAMP,
    FOREIGN KEY (iduser) REFERENCES users(iduser)
);