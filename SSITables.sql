-- Tables:

-- Categories
CREATE TABLE Category (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    description VARCHAR(255)
);

CREATE TABLE Category (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(50),description VARCHAR(255));


INSERT INTO Category (name, description) VALUES ('Category 1', 'This is a description');
INSERT INTO Category (name, description) VALUES ('Category 2', 'This is a description');
INSERT INTO Category (name, description) VALUES ('Category 3', 'This is a description');


CREATE TABLE Projects (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    description TEXT,
    photo LONGBLOB,
    category INT,
    FOREIGN KEY (category) REFERENCES Category(id)
);

CREATE TABLE Projects (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), description TEXT, photo MEDIUMBLOB, category INT, FOREIGN KEY (category) REFERENCES category(id));


INSERT INTO Projects (name, description, photo, category) VALUES ('Project 1', 'Description for Project 1', 'http://project1.com', 1), ('Project 2', 'Description for Project 2', 'http://project2.com', 1), ('Project 3', 'Description for Project 3', 'http://project3.com', 1);

INSERT INTO Projects (name, description, photo, category) VALUES ('Project 4', 'Description for Project 4', 'http://project4.com', 2), ('Project 5', 'Description for Project 5', 'http://project5.com', 2), ('Project 6', 'Description for Project 6', 'http://project6.com', 2);

-- Inserting data for category 3
INSERT INTO Projects (name, description, photo, category) VALUES ('Project 7', 'Description for Project 7', 'http://project7.com', 3), ('Project 8', 'Description for Project 8', 'http://project8.com', 3), ('Project 9', 'Description for Project 9', 'http://project9.com', 3);



INSERT INTO Projects (name, description, link, category) VALUES ('Project 1', 'Description for Project 1', 'https://project1.example.com', 'C1');

-- Insert the second random project
INSERT INTO Projects (name, description, link, category) VALUES ('Project 2', 'Description for Project 2', 'https://project2.example.com', 'C2');

-- Insert the third random project
INSERT INTO Projects (name, description, link, category)
VALUES ('Project 3', 'Description for Project 3', 'https://project3.example.com', 'C3');




CREATE TABLE Business (
    name VARCHAR(255),
    description VARCHAR(255), -- Change to VARCHAR or CHAR if you want to store email addresses
    service VARCHAR(255)
);

-- Insert the first random business
INSERT INTO Business (name, description, service)
VALUES ('Business A', 'email1@example.com', 'Service A');

-- Insert the second random business
INSERT INTO Business (name, description, service)
VALUES ('Business B', 'email2@example.com', 'Service B');

-- Insert the third random business
INSERT INTO Business (name, description, service)
VALUES ('Business C', 'email3@example.com', 'Service C');



Department:
id: Primary key
name: Unique

Experience Level:
id: Primary key
name: Unique

CREATE TABLE Department (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(50) UNIQUE);

CREATE TABLE Experience_Level (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(50) UNIQUE);

CREATE TABLE Careers (
    name VARCHAR(255),
    description VARCHAR(255) -- Assuming you want to store email addresses
);

-- Insert the first random career
INSERT INTO Careers (name, description)
VALUES ('Career A', 'email1@example.com');

-- Insert the second random career
INSERT INTO Careers (name, description)
VALUES ('Career B', 'email2@example.com');

-- Insert the third random career
INSERT INTO Careers (name, description)
VALUES ('Career C', 'email3@example.com');


-- Partners
CREATE TABLE Partners (
    partnerID INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    imageData BLOB
);

CREATE TABLE Partners (partnerID INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), imageData BLOB);

-- Inquiry

CREATE TABLE Inquiries (
    inquiryID INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    service_ID int(11),
    meeting_date DATE,
    confirmed tinyint(1) default 0;
);

CREATE TABLE Inquiries_Test2 (inquiryID INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255), service_ID int(11), meeting_date DATE, confirmed tinyint(1) default 0);

-- Insert IDS: 1, 16, 17, 18

INSERT INTO Inquiries_Test2 (name, email, service_ID, meeting_date, confirmed)
VALUES
  ('John Doe', 'john.doe@example.com', 1, '2023-10-15', 1),
  ('Alice Smith', 'alice.smith@example.com', 1, '2023-10-15', 0),
  ('Bob Johnson', 'bob.johnson@example.com', 16, '2023-10-15', 1),
  ('Eva Williams', 'eva.williams@example.com', 17, '2023-10-15', 0),
  ('Charlie Brown', 'charlie.brown@example.com', 18, '2023-10-15', 1);

INSERT INTO Inquiries_Test2_2 (name, email, service_ID, meeting_date, confirmed) VALUES ('John Doe', 'john.doe@example.com', 1, '2023-10-15', 1), ('Alice Smith', 'alice.smith@example.com', 1, '2023-10-16', 0), ('Bob Johnson', 'bob.johnson@example.com', 16, '2023-10-17', 1), ('Eva Williams', 'eva.williams@example.com', 17, '2023-10-18', 0), ('Charlie Brown', 'charlie.brown@example.com', 18, '2023-10-19', 1);
  
-- Calendar

CREATE TABLE CalendarTest2 (
    calendar_id INT AUTO_INCREMENT PRIMARY KEY,
    calendar_date DATE,
    timeslot_1 int(11),
    timeslot_2 int(11),
    timeslot_3 int(11),
    timeslot_4 int(11),
    timeslot_5 int(11),

    FOREIGN KEY (timeslot_1) REFERENCES Inquiries_Test2(inquiryID),
    FOREIGN KEY (timeslot_2) REFERENCES Inquiries_Test2(inquiryID),
    FOREIGN KEY (timeslot_3) REFERENCES Inquiries_Test2(inquiryID),
    FOREIGN KEY (timeslot_4) REFERENCES Inquiries_Test2(inquiryID),
    FOREIGN KEY (timeslot_5) REFERENCES Inquiries_Test2(inquiryID)
);

CREATE TABLE Calendar_Test2 (calendar_id INT AUTO_INCREMENT PRIMARY KEY, calendar_date DATE, timeslot_1 int(11), timeslot_2 int(11), timeslot_3 int(11), timeslot_4 int(11), timeslot_5 int(11), FOREIGN KEY (timeslot_1) REFERENCES Inquiries_Test2(inquiryID), FOREIGN KEY (timeslot_2) REFERENCES Inquiries_Test2(inquiryID), FOREIGN KEY (timeslot_3) REFERENCES Inquiries_Test2(inquiryID), FOREIGN KEY (timeslot_4) REFERENCES Inquiries_Test2(inquiryID), FOREIGN KEY (timeslot_5) REFERENCES Inquiries_Test2(inquiryID));


-- 21, 22, 23, 24, 25

INSERT INTO Calendar (calendar_date, timeslot_1, timeslot_2, timeslot_3, timeslot_4, timeslot_5) VALUES ('2023-10-12', 21, 21, 22, 22, 23);

INSERT INTO Calendar (calendar_date) VALUES ('2023-10-13');

INSERT INTO Calendar (calendar_date) VALUES ('2023-10-14');

INSERT INTO Calendar (calendar_date, timeslot_1, timeslot_2, timeslot_3, timeslot_4, timeslot_5) VALUES ('2023-10-15', 24, 24, 25, 25, 25);

INSERT INTO Calendar (calendar_date, timeslot_2, timeslot_3, timeslot_5) VALUES ('2023-10-16', 24, 22, 21);

INSERT INTO Calendar (calendar_date) VALUES ('2023-10-17');

INSERT INTO Calendar (calendar_date) VALUES ('2023-10-18');

INSERT INTO Calendar (calendar_date) VALUES ('2023-10-19');

INSERT INTO Calendar (calendar_date, timeslot_1, timeslot_2, timeslot_3, timeslot_4, timeslot_5) VALUES ('2023-10-20', 21, 22, 23, 24, 25);


-- Clients

CREATE TABLE Clients (
    clientID INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    description TEXT,
    client_category INT,
    FOREIGN KEY (client_category) REFERENCES clientCategories(cc_id)
);

CREATE TABLE Calendar (calendar_id INT AUTO_INCREMENT PRIMARY KEY, calendar_date DATE, timeslot_1 int(11) FOREIGN KEY (timeslot_1) REFERENCES Inquiries(inquiryID), timeslot_2 int(11) FOREIGN KEY (timeslot_2) REFERENCES Inquiries(inquiryID), timeslot_3 int(11) FOREIGN KEY (timeslot_3) REFERENCES Inquiries(inquiryID), timeslot_4 int(11) FOREIGN KEY (timeslot_4) REFERENCES Inquiries(inquiryID), timeslot_5 int(11) FOREIGN KEY (timeslot_5) REFERENCES Inquiries(inquiryID));

-- Service

CREATE TABLE Services (
    serviceID INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255)
);

CREATE TABLE Services (serviceID INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), description VARCHAR(255));

-- Client Category
CREATE TABLE clientCategories (
    cc_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
);

CREATE TABLE clientCategories (cc_id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255));

INSERT INTO clientCategories (name) VALUES ('Government');
INSERT INTO clientCategories (name) VALUES ('Education');
INSERT INTO clientCategories (name) VALUES ('Banking');
INSERT INTO clientCategories (name) VALUES ('Healthcare');
INSERT INTO clientCategories (name) VALUES ('Networks & Telco');
INSERT INTO clientCategories (name) VALUES ('Malls & Food Industry');


-- Categories
('categoryId', 'int(11)', 'NO', 'PRI', None, 'auto_increment')
('name', 'text', 'NO', '', None, '')
('description', 'text', 'NO', '', None, '')


INSERT INTO categories (name, description) VALUES ('Category 2', 'This is a description');
INSERT INTO categories (name, description) VALUES ('Category 3', 'This is a description');

-- Client
CREATE TABLE Clients (
    clientID INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    description TEXT,
    client_category INT,
    FOREIGN KEY (client_category) REFERENCES clientCategories(cc_id)
);


-- Time SLots

CREATE TABLE Calendar (
    timeID INT AUTO_INCREMENT PRIMARY KEY,
    month INT,
    year INT,
    days: INT,
    timeSlots: [] # 10:00, 11:00, 12:00, 13:00, 14:00, 15:00
)

-- Opportunities

INSERT INTO Opportunities (title, location, department, experience_level, description, qualifications, skills, responsibilities) VALUES('Software Developer', 'New York', 'Engineering', 'Entry Level', 'We are looking for a software developer to join our team', 'BS degree in Computer Science', 'Java Python SQL', 'Develop and maintain software applications'), ('Marketing Manager', 'Los Angeles', 'Marketing', 'Mid Level', 'We are hiring a Marketing Manager to lead our marketing campaigns.', "Bachelor's degree in Marketing", 'Digital marketing, SEO, SEM', 'Plan and execute marketing strategies.'), ('Sales Representative', 'Chicago', 'Sales', 'Entry Level', 'Join our sales team and help us drive revenue growth.', 'High School diploma', 'Sales, negotiation, communication', 'Identify and approach potential clients.');


