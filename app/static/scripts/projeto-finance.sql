
-------------------------------------------------------------------
-------------------------------------------------------------------
-------------------------------------------------------------------

-- Esse script foi feito para executar no banco de dados em caso de perda

-------------------------------------------------------------------
-------------------------------------------------------------------
-------------------------------------------------------------------

-- 202302686851 Rian Carvalho dos Reis
-- 202302381626 Leonardo Rodrigues de Oliveira Nestri
-- 202303143699 Alejandro Monezzi Scarani
-- 202303321279 Derek Pires Bergesch da Costa
-- 202302700951 Joao Pedro Coelho Silva

-- Criando a tabela principal de meses

CREATE TABLE meses (
	id SERIAL PRIMARY KEY,
	mes VARCHAR(20) NOT NULL,
	total_despesas NUMERIC(10, 2),
	total_receitas NUMERIC(10, 2),
	saldo NUMERIC(10, 2)
);

INSERT INTO meses (mes, total_despesas, total_receitas, saldo)
VALUES
	('Janeiro', 0, 0, 0),
	('Fevereiro', 0, 0, 0),
	('Março', 0, 0, 0),
	('Abril', 0, 0, 0),
	('Maio', 0, 0, 0),
	('Junho', 0, 0, 0),
	('Julho', 0, 0, 0),
	('Agosto', 0, 0, 0),
	('Setembro', 0, 0, 0),
	('Outubro', 0, 0, 0),
	('Novembro', 0, 0, 0),
	('Dezembro', 0, 0, 0);

-- SELECT * FROM meses;

-----------------------------------------------------------

-- Criando tabela de desdesas

CREATE TABLE despesas (
    id SERIAL PRIMARY KEY,
    mes_id INTEGER REFERENCES meses(id),
    descricao VARCHAR(100) NOT NULL,
    valor NUMERIC(10, 2) NOT NULL
);

-- Despesas ficticias
INSERT INTO despesas (mes_id, descricao, valor) VALUES
(1, 'Aluguel', 1000.00),
(1, 'Contas', 505.00),
(2, 'Aluguel', 1050.00),
(2, 'Contas', 535.00),
(3, 'Aluguel', 1100.00),
(3, 'Contas', 637.00),
(4, 'Aluguel', 1150.00),
(4, 'Contas', 420.00),
(5, 'Aluguel', 1200.00),
(5, 'Contas', 650.00),
(6, 'Aluguel', 1200.00),
(6, 'Contas', 550.00),
(7, 'Aluguel', 1250.00),
(7, 'Contas', 565.00),
(8, 'Aluguel', 1300.00),
(8, 'Contas', 570.00),
(9, 'Aluguel', 1350.00),
(9, 'Contas', 610.00),
(10, 'Aluguel', 1400.00),
(10, 'Contas', 500.00),
(11, 'Aluguel', 1450.00),
(11, 'Contas', 530.00),
(12, 'Aluguel', 1500.00),
(12, 'Contas', 540.00);

-- Atualizando o total de despesas na tabela meses, de acordo com cada mes
UPDATE meses
SET total_despesas = (
    SELECT SUM(valor)
    FROM despesas
    WHERE despesas.mes_id = meses.id
);

-- SELECT * FROM meses;

-----------------------------------------------------------

-- Criando tabela de desdesas

CREATE TABLE receitas (
    id SERIAL PRIMARY KEY,
    mes_id INTEGER REFERENCES meses(id),
    descricao VARCHAR(100) NOT NULL,
    valor NUMERIC(10, 2) NOT NULL
);

-- Despesas ficticias
INSERT INTO receitas (mes_id, descricao, valor) VALUES
(1, 'Salário', 2200.00),
(1, 'Freelance', 335.00),
(2, 'Salário', 2200.00),
(3, 'Salário', 2200.00),
(4, 'Salário', 2400.00),
(5, 'Salário', 2400.00),
(6, 'Salário', 2400.00),
(6, 'Freelance', 160.00),
(7, 'Salário', 2400.00),
(8, 'Salário', 2400.00),
(9, 'Salário', 2800.00),
(10, 'Salário', 2800.00),
(11, 'Salário', 2800.00),
(11, 'Freelance', 1550.00),
(12, 'Salário', 2800.00);

-- Atualizando o total de receitas na tabela meses, de acordo com cada mes
UPDATE meses
SET total_receitas = (
    SELECT SUM(valor)
    FROM receitas
    WHERE receitas.mes_id = meses.id
);

-- SELECT * FROM meses;

-----------------------------------------------------------

-- Atualizando a coluna saldos em meses
UPDATE meses SET saldo = total_receitas - total_despesas;

-- SELECT * FROM meses;
