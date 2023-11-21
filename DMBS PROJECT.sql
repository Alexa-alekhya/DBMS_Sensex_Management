CREATE DATABASE IF NOT EXISTS SSM;
USE SSM;

CREATE TABLE Stock_info(
	stock_id VARCHAR(5),
	date_time DATE,
	change_abs float(5),
    change_per float(5),
	PRIMARY KEY (stock_id)
	);
DESC Stock_info;

#Now instead of change_per, it is perf. Will say inc or dec in price.

ALTER TABLE Stock_info
ADD perf VARCHAR(255);

ALTER TABLE Stock_info
DROP COLUMN LTP;

CREATE TABLE LTP(
	LastTradedPrice FLOAT(10) PRIMARY KEY,
    stock_id VARCHAR(25),
    FOREIGN KEY (stock_id) REFERENCES stock_info(stock_id)
);

CREATE TABLE Stock_Details(
	stock_id varchar(5),
	best_price VARCHAR(5),
    company_name varchar(20),
    primary key(stock_id),
    foreign key(stock_id) references Stock_info(stock_id)
	);
-- DESC Stock_Details;


CREATE TABLE favourites(
	email_id VARCHAR(25),
	stock_id VARCHAR(5) NOT NULL,
	Quantity int(5) DEFAULT 0,
    Login_id varchar(25),
	PRIMARY KEY (email_id),
    FOREIGN KEY (Login_id) REFERENCES Login_Details(Login_ID),
	FOREIGN KEY (stock_id) REFERENCES stock_info(stock_id)
	);
-- DESC favourites;
#make another table for buying price as its multi valued.

CREATE TABLE BuyingPrice(
	BuyingPrice FLOAT(10) PRIMARY KEY,
    email_id VARCHAR(25),
    FOREIGN KEY (email_id) REFERENCES favourites (email_id)
);

CREATE TABLE login_details(
	password VARCHAR(25),
	status VARCHAR(5) NOT NULL,
    email_id varchar(25),
    login_id varchar(25),
	PRIMARY KEY (login_id),
    FOREIGN KEY (email_id) REFERENCES User(email_id)
	);
    
-- DROP TABLE login_details;

--  DESC login_details;
--  
SHOW TABLES;

CREATE TABLE user(
	email_id VARCHAR(25),
	f_name VARCHAR(20) NOT NULL,
	l_name VARCHAR(20) NOT NULL,
    gender ENUM('M','F'),
    dob DATE,
	PRIMARY KEY (email_id)
	);
DESC user;


CREATE TABLE sensex_val(
	stock_id VARCHAR(40),
	value VARCHAR(40) NOT NULL,
	change_sensex float(40) DEFAULT 0,
    sensex_per float(40) DEFAULT 0,
    email_id varchar(40),
	PRIMARY KEY (stock_id),
    FOREIGN KEY (email_id) REFERENCES Favourites(email_id)
	);
    
-- SHOW TABLES;

INSERT INTO stock_info(stock_id,Date_time,Change_Abs,perf) 
		VALUES('INF1','2023-10-16','10','I'),
		('TCS1','2023-10-16','10','D'),
		('CTS1','2023-10-16','0','S'),
		('WIP1','2023-10-16','5','I');

SELECT * FROM stock_info;

INSERT INTO stock_info(stock_id,Date_time,Change_Abs,perf) 
		VALUES('INF1','2023-10-16','10','I'),
		('TCS1','2023-10-16','10','D'),
		('CTS1','2023-10-16','0','S'),
		('WIP1','2023-10-16','5','I');
INSERT INTO stock_info(stock_id,Date_time,Change_Abs,perf) 
VALUES
        ('HCL1', '2023-10-16', '8', 'I'),
		('MIND1', '2023-10-16', '12', 'D'),
		('TEM1', '2023-10-16', '6', 'I');
INSERT INTO stock_info(stock_id,Date_time,Change_Abs,perf) 
VALUES
('INF2', '2023-10-17', '12', 'I'),
('TCS2', '2023-10-17', '8', 'D'),
('CTS2', '2023-10-17', '2', 'S'),
('WIP2', '2023-10-17', '6', 'I');
       
INSERT INTO LTP(stock_id,LastTradedPrice) 
		VALUES('INF1','85'),
		('TCS1','60'),
		('CTS1','75'),
		('WIP1','70');

INSERT INTO LTP(stock_id, LastTradedPrice) 
VALUES('HCL1','55'),
    ('MIND1','65'),
    ('TEM1','45'),
    ('INF2','95'),
    ('TCS2','62'),
    ('CTS2','78'),
    ('WIP2','73');

SELECT * FROM LTP;

INSERT INTO Stock_Details (stock_id, best_price, company_name)
VALUES
    ('INF1', '100.0', 'Infosys'),
    ('TCS1', '85.5', 'Tata Consultancy'),
    ('WIP1', '90.0', 'Wipro');

INSERT INTO Stock_Details (stock_id, best_price, company_name)
VALUES
    ('CTS1', '75.0', 'Company CTS1'),
    ('HCL1', '70.0', 'HCL Technologies'),
    ('MIND1', '110.0', 'Mindtree'),
    ('TEM1', '55.0', 'Company TEM1'),
    ('INF2', '105.0', 'Infosys'),
    ('TCS2', '87.5', 'Tata Consultancy'),
    ('CTS2', '72.0', 'Company CTS2'),
    ('WIP2', '92.0', 'Wipro');

SELECT * FROM Stock_Details;

INSERT INTO user (email_id, f_name, l_name, gender, dob)
VALUES
    ('john.doe@example.com', 'John', 'Doe', 'M', '1990-05-15'),
    ('jane.smith@example.com', 'Jane', 'Smith', 'F', '1985-09-28'),
    ('robert.john@example.com', 'Robert', 'Johnson', 'M', '1980-03-10'),
    ('susan.wilson@example.com', 'Susan', 'Wilson', 'F', '1995-12-07'),
    ('mik.brown@example.com', 'Michael', 'Brown', 'M', '1982-07-19'),
    ('linda.will@example.com', 'Linda', 'Williams', 'F', '1978-11-02'),
    ('will.davis@example.com', 'William', 'Davis', 'M', '1992-06-14'),
    ('emily.jones@example.com', 'Emily', 'Jones', 'F', '1987-04-23'),
    ('james.ander@example.com', 'James', 'Anderson', 'M', '1989-10-30'),
    ('olivia.miller@example.com', 'Olivia', 'Miller', 'F', '1993-02-08');
    
SELECT * FROM user;

INSERT INTO login_details (password, status, email_id, login_id)
VALUES
    ('P@ssw0rd1', 'A', 'john.doe@example.com', 'john.doe'),
    ('SecurePwd2', 'A', 'jane.smith@example.com', 'jane.smith'),
    ('Strong123', 'A', 'robert.john@example.com', 'robert.john'),
    ('SecretPwd4', 'A', 'susan.wilson@example.com', 'susan.wilson'),
    ('Pa$$w0rd5', 'P', 'mik.brown@example.com', 'mik.brown'),
    ('PrivatePwd6', 'A', 'linda.will@example.com', 'linda.will'),
    ('ProtectPwd7', 'P', 'will.davis@example.com', 'will.davis'),
    ('SuperSecure8', 'A', 'emily.jones@example.com', 'emily.jones'),
    ('SecureLogin9', 'P', 'james.ander@example.com', 'james.ander'),
    ('MySecret10', 'A', 'olivia.miller@example.com', 'olivia.miller');

SELECT * FROM login_details;

INSERT INTO favourites (email_id, stock_id, Quantity, Login_id)
VALUES
    ('john.doe@example.com', 'INF1', 100, 'john.doe'),
    ('jane.smith@example.com', 'TCS1', 50, 'jane.smith'),
    ('robert.john@example.com', 'CTS1', 75, 'robert.john'),
    ('susan.wilson@example.com', 'WIP1', 60, 'susan.wilson'),
    ('mik.brown@example.com', 'HCL1', 120, 'mik.brown'),
    ('linda.will@example.com', 'MIND1', 80, 'linda.will'),
    ('will.davis@example.com', 'TEM1', 110, 'will.davis'),
    ('emily.jones@example.com', 'INF2', 90, 'emily.jones'),
    ('james.ander@example.com', 'TCS2', 70, 'james.ander'),
    ('olivia.miller@example.com', 'CTS2', 85, 'olivia.miller');

SELECT * FROM favourites;

INSERT INTO sensex_val (stock_id, value, change_sensex, sensex_per, email_id)
VALUES
    ('INF1', '100.0', 0.4, 30, 'john.doe@example.com'),
    ('TCS1', '85.5', 0.6, 60, 'jane.smith@example.com'),
    ('CTS1', '75.0', 0.7, 60, 'robert.john@example.com'),
    ('WIP1', '90.0', 0.8, 70, 'susan.wilson@example.com'),
    ('HCL1', '120.0', 0.9, 50, 'mik.brown@example.com'),
    ('MIND1', '80.0', 0.2, 60, 'linda.will@example.com'),
    ('TEM1', '110.0', 0.3, 70, 'will.davis@example.com'),
    ('INF2', '90.0', 0.4, 80, 'emily.jones@example.com'),
    ('TCS2', '70.0', 0.1, 90, 'james.ander@example.com'),
    ('CTS2', '85.0', 0.7, 10, 'olivia.miller@example.com');

SELECT * FROM sensex_val;


INSERT INTO BuyingPrice (BuyingPrice, email_id)
VALUES
    (100.0, 'john.doe@example.com'),
    (85.5, 'jane.smith@example.com'),
    (75.0, 'robert.john@example.com'),
    (90.0, 'susan.wilson@example.com'),
    (120.0, 'mik.brown@example.com'),
    (80.0, 'linda.will@example.com'),
    (110.0, 'will.davis@example.com'),
    (60.0, 'emily.jones@example.com'),
    (70.0, 'james.ander@example.com'),
    (85.0, 'olivia.miller@example.com');

SELECT * FROM buyingprice;


DELIMITER //
CREATE TRIGGER check_duplicate_trigger
BEFORE INSERT ON stock_info
FOR EACH ROW
BEGIN
    DECLARE duplicate_count INT;

    SELECT COUNT(*) INTO duplicate_count
    FROM your_table
    WHERE stock_id = NEW.stock_id;

    IF duplicate_count > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Duplicate entry for primary key';
    END IF;
END;
//
DELIMITER ;

-- Assuming you have a table named 'stock_info' with a primary key column 'stock_id'
-- Replace 'stock_info' and 'stock_id' with your actual table and primary key column names

SELECT * FROM user;

SELECT * FROM stock_info;

INSERT INTO stock_info(stock_id,Date_time,Change_Abs,perf) 
VALUES('INF2', '2023-10-17', '12', 'I');

ALTER TABLE user
ADD balance_amt VARCHAR(255);

ALTER TABLE user
ADD stocks VARCHAR(100);

UPDATE user
SET balance_amt= 10000;

ALTER TABLE stock_info
ADD price VARCHAR(255);

UPDATE stock_info
SET price= 500;

SELECT COUNT(*) FROM stock_info;
DESC user;
DESC stock_info;

CREATE TABLE user_stocks (
    email_id VARCHAR(25),
    stock_id VARCHAR(5),
    PRIMARY KEY (email_id, stock_id),
    FOREIGN KEY (email_id) REFERENCES user(email_id),
    FOREIGN KEY (stock_id) REFERENCES stock_info(stock_id)
);

INSERT INTO user_stocks (email_id, stock_id) VALUES
('jane.smith@example.com','CTS1'),
('jane.smith@example.com','CTS2'),
('jane.smith@example.com','TCS2');

SELECT * FROM user_stocks;
SELECT * FROM user;
SELECT * FROM stock_info;
SELECT * FROM sensex_val;

ALTER TABLE user_stocks
ADD price VARCHAR(255);

UPDATE user_stocks
SET price= 500;

SHOW TABLES;
SELECT * FROM ltp;
SELECT * FROM favourites;

DESC favourites;

DELIMITER //
CREATE PROCEDURE CalculateStockCost(IN p_email_id VARCHAR(25), IN p_stock_id VARCHAR(5))
BEGIN
    DECLARE v_stock_price DECIMAL(10, 2);
    DECLARE v_quantity INT;
    DECLARE v_total_cost DECIMAL(10, 2);

    -- Get stock price from stock_info
    SELECT price INTO v_stock_price
    FROM stock_info
    WHERE stock_id = p_stock_id
    ORDER BY date_time DESC
    LIMIT 1;

    -- Get quantity from favourites
    SELECT Quantity INTO v_quantity
    FROM favourites
    WHERE email_id = p_email_id AND stock_id = p_stock_id;

    -- Calculate total cost
    SET v_total_cost = v_stock_price * v_quantity;

    -- Print the result
    SELECT v_total_cost AS TotalCost;
END //
DELIMITER ;

CALL CalculateStockCost('emily.jones@example.com', 'INF2');
