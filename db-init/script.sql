CREATE DATABASE  exo;
 
USE exo;

CREATE TABLE user (
    id INT PRIMARY KEY,
    nom VARCHAR(30) NOT NULL,
    prenom VARCHAR(30)NOT NULL
);
 
INSERT INTO user VALUES('1','Denorme','Nicolas');
INSERT INTO user VALUES('2','Delrue','Pierre');
INSERT INTO user VALUES('3','Denorme','Albert');
INSERT INTO user VALUES('4','Denorme ','Evelyne');