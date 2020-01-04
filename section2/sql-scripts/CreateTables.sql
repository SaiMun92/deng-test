Create Table Customers
(
    CustomerID int not null,
    Customer_Name varchar(25),
    Customer_Phone varchar(25),
    PRIMARY KEY (CustomerID)
);

Create Table Salespeople
(
  SalespersonID int not null,
  Salesperson_Name varchar(25),
  PRIMARY KEY (SalespersonID)
);

Create Table Car_Models
(
  Model_ID int not null,
  Model_Name varchar(25),
  Model_Variant varchar(25),
  Primary Key (Model_ID)
);

Create Table Car_Manufacturers
(
  Manufacturer_ShortName varchar(10) not null,
  Manufacturer_FullName varchar(25),
  PRIMARY KEY (Manufacturer_ShortName)
);

Create Table Engine_CC_Types
(
  Engine_CC_Type_ID int not null,
  Engine_Capacity_Range varchar(20),
  PRIMARY KEY (Engine_CC_Type_ID)
);

Create Table Cars_for_Sale
(
  CarsID int not null,
  ModelID int not null,
  Manufacturer_ShortName varchar(10) not null,
  Engine_CC_TypeID int not null,
  Used_or_New varchar(5),
  Price decimal(10, 2),
  SerialNum varchar(25),
  Weight decimal(10, 2),
  PRIMARY KEY (CarsID),
  FOREIGN KEY (ModelID) references Car_Models(Model_ID),
  FOREIGN KEY (Manufacturer_ShortName) references Car_Manufacturers(Manufacturer_ShortName),
  FOREIGN KEY (Engine_CC_TypeID) references Engine_CC_Types(Engine_CC_Type_ID)
);

Create Table Cars_Sold
(
    Cars_Sold_ID int not null,
    CarsID  int NOT NULL,
    CustomerID int not null,
    SalespersonID int not null,
    date_Sold date,
    Primary Key (Cars_Sold_ID),
    FOREIGN KEY (CarsID) references Cars_for_Sale(CarsID),
    FOREIGN KEY (CustomerID) references Customers(CustomerID),
    FOREIGN KEY (SalespersonID) references Salespeople(SalespersonID)
);

