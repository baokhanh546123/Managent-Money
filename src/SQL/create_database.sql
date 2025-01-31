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

CREATE TABLE list_needs (
    iduser INT NULL, 
    name_needs VARCHAR(50) NULL, 
    cost FLOAT NULL,
    times TIMESTAMP,
    CONSTRAINT fk_iduser FOREIGN KEY (iduser) REFERENCES users(iduser)
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
    CONSTRAINT fk_iduser_stoge_data FOREIGN KEY (iduser) REFERENCES users(iduser)
);

CREATE TABLE list_wants (
    iduser INT NULL, 
    name_wants VARCHAR(50), 
    cost FLOAT,
    times TIMESTAMP,
    CONSTRAINT fk_iduser FOREIGN KEY (iduser) REFERENCES users(iduser)
);

CREATE TABLE list_savings (
    iduser INT NULL, 
    name_savings VARCHAR(50) NULL, 
    cost FLOAT NULL,
    times TIMESTAMP,
    CONSTRAINT fk_iduser FOREIGN KEY (iduser) REFERENCES users(iduser)
);