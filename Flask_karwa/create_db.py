from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Boolean, Text, ARRAY, ForeignKey

engine = create_engine('sqlite:///Karwa.db', echo = True)
meta = MetaData()
user = Table(
   'Users', meta,
Column("PhoneNumber",String, primary_key = True),
Column("FirstName",String),
Column("LastName",String),
Column("PassWord",String),
Column("Credit",Integer),
)
reserve = Table(
   'Reserves', meta,
Column('id', Integer, primary_key = True),
Column('PhoneNumber', String,ForeignKey("Users.PhoneNumber")),
Column("Date",String),
Column("Hour",String),
Column("Time",String),
Column("CurrentDate",String),
Column("WashCarbody",Integer),
Column("WashEngine",Integer),
Column("WaxDashboard",Integer),
Column("WaxInsideDoor",Integer),
Column("WaxWheels",Integer),
Column("VacuumInside",Integer),
Column("VacuumTrunk",Integer),
Column("TotalCost",Integer),
Column("Situation",String),
)
dates = Table(
   'Dates', meta,
Column("Date",String, primary_key = True),
Column("eight",Integer),
Column("nine",Integer),
Column("ten",Integer),
Column("eleven",Integer),
Column("twelve",Integer),
Column("thirteen",Integer),
Column("fourteen",Integer),
Column("fifteen",Integer),
Column("sixteen",Integer),
Column("seventeen",Integer),
Column("eighteen",Integer),
Column("nineteen",Integer),
)
messages = Table(
   'Messages', meta,
Column('id', Integer, primary_key = True),
Column('PhoneNumber', String,ForeignKey("Users.PhoneNumber")),
Column("SubmitDate",String),
Column("Message",String),
)
meta.create_all(engine)