from flask import Flask, redirect, url_for, request, make_response, jsonify
from sqlalchemy import Column, Integer, String, Boolean, Text
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine('sqlite:///Karwa.db', echo=True,
                       connect_args={"check_same_thread": False})
conn = engine.connect()
trans = conn.begin()
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)
session.commit()


class User(Base):
    __tablename__ = 'Users'

    phonenumber = Column(String, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    password = Column(String)
    credit = Column(Integer)

    def init(self, phonenumber, firstname, lastname,
             password, credit):
        self.phonenumber = phonenumber
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
        self.credit = credit


class Reserve(Base):
    __tablename__ = 'Reserves'

    id = Column(Integer, primary_key=True)
    phonenumber = Column(String)
    date = Column(String)
    hour = Column(String)
    time = Column(String)
    currentdate = Column(String)
    washcarbody = Column(Integer)
    washengine = Column(Integer)
    waxdashboard = Column(Integer)
    waxinsidedoor = Column(Integer)
    waxwheels = Column(Integer)
    vacuuminside = Column(Integer)
    vacuumtrunk = Column(Integer)
    totalcost = Column(Integer)
    situation = Column(String)

    def init(self, id, phonenumber, date, hour, time, currentdate, washcarbody, washengine, waxdashboard, waxinsidedoor,
             waxwheels, vacuuminside, vacuumtrunk, totalcost, situation):
        self.id = id
        self.phonenumber = phonenumber
        self.date = date
        self.hour = hour
        self.time = time
        self.currentdate = currentdate
        self.washcarbody = washcarbody
        self.washengine = washengine
        self.waxdashboard = waxdashboard
        self.waxinsidedoor = waxinsidedoor
        self.waxwheels = waxwheels
        self.vacuuminside = vacuuminside
        self.vacuumtrunk = vacuumtrunk
        self.totalcost = totalcost
        self.situation = situation

class Message(Base):
    __tablename__ = 'Messages'

    id = Column(Integer, primary_key=True)
    phonenumber = Column(String)
    submitdate = Column(String)
    message = Column(String)

    def init(self, id, phonenumber, submitdate,
             message):
        self.id = id
        self.phonenumber = phonenumber
        self.submitdate = submitdate
        self.message = message

class Date(Base):
    __tablename__ = 'Dates'

    date = Column(String, primary_key=True)
    eight = Column(Integer)
    nine = Column(Integer)
    ten = Column(Integer)
    eleven = Column(Integer)
    twelve = Column(Integer)
    thirteen = Column(Integer)
    fourteen = Column(Integer)
    fifteen = Column(Integer)
    sixteen = Column(Integer)
    seventeen = Column(Integer)
    eighteen = Column(Integer)
    nineteen = Column(Integer)

    def init(self, date, eight, nine, ten, eleven, twelve, thirteen, fourteen,
             fifteen, sixteen, seventeen, eighteen, nineteen):
        self.date = date
        self.eight = eight
        self.nine = nine
        self.ten = ten
        self.eleven = eleven
        self.twelve = twelve
        self.thirteen = thirteen
        self.fourteen = fourteen
        self.fifteen = fifteen
        self.sixteen = sixteen
        self.seventeen = seventeen
        self.eighteen = eighteen
        self.nineteen = nineteen


# Connecting to database
engine = create_engine('sqlite:///Karwa.db', echo=True)
conn = engine.connect()

app = Flask(__name__)


@app.route('/sign_up', methods=['POST'])
def sign_up():
    print(request.data.decode("utf-8"))
    phonenumber = request.json.get('PhoneNumber')
    firstname = request.json.get('FirstName')
    lastname = request.json.get('LastName')
    password = request.json.get('Password')
    result = session.query(User).filter(User.phonenumber == phonenumber).first()
    if result is None:
        user = User(phonenumber=phonenumber, firstname=firstname,
                    lastname=lastname, password=password, credit=0)
        session.add(user)
        try:
            session.commit()
        except:
            session.rollback()
        print(phonenumber, firstname, lastname, password, "Registered Successfully.")
        return jsonify(
            Answer="Registered Successfully"
        )

    else:
        return jsonify(
            Answer="phonenumber existed"
        )


@app.route('/login', methods=['POST'])
def login():
    print(request.data.decode("utf-8"))
    phonenumber = request.json.get('PhoneNumber')
    password = request.json.get('Password')
    result = session.query(User).filter(User.phonenumber == phonenumber, User.password == password).first()
    if result is not None:
        print(phonenumber, password, "loged in Successfully.")
        return jsonify(
            Answer="Logged in successfully"
        )

    else:
        return jsonify(
            Answer="phone number or password are wrong"
        )


@app.route('/credit', methods=['POST'])
def credit():
    print(request.data.decode("utf-8"))
    phonenumber = request.json.get('PhoneNumber')
    result = session.query(User).filter(User.phonenumber == phonenumber).first()
    credit = result.credit
    if result is not None:
        print(credit, "is the current credit")
        return jsonify(
            Credit=credit
        )

    else:
        print("something is wrong")
        return jsonify(
            Answer="something is wrong"
        )


@app.route('/add_credit', methods=['POST'])
def add_credit():
    print(request.data.decode("utf-8"))
    phonenumber = request.json.get('PhoneNumber')
    credit2 = request.json.get('Credit')
    result = session.query(User).filter(User.phonenumber == phonenumber).first()
    if result is not None:
        result.credit = credit2 + result.credit
        session.commit()
        print(result.credit, "is updated")
        return jsonify(
            Credit="credit updated:" + str(result.credit)
        )

    else:
        print(result.credit, "is the current credit")
        return jsonify(
            Answer="something is wrong"
        )


@app.route('/order', methods=['POST'])
def order():
    print(request.data.decode("utf-8"))
    phonenumber = request.json.get('PhoneNumber')
    date = request.json.get('Date')
    currentdate = request.json.get('CurrentDate')
    hour = request.json.get('Hour')
    washcarbody = int(request.json.get('WashCarbody'))
    washengine = int(request.json.get('WashEngine'))
    waxdashboard = int(request.json.get('WaxDashboard'))
    waxinsidedoor = int(request.json.get('WaxInsideDoor'))
    waxwheels = int(request.json.get('WaxWheels'))
    vacuuminside = int(request.json.get('VacuumInside'))
    vacuumtrunk = int(request.json.get('VacuumTrunk'))
    cost = int(request.json.get('Cost'))

    result = session.query(Date).filter(Date.date == date).first()
    result1 = session.query(User).filter(User.phonenumber == phonenumber).first()
    if result is not None:
        result1.credit = result1.credit - int(cost)
        if hour == "eight":
            if result.eight == 0:
                return jsonify(
                    Answer="capacity is full"
                )
            time = date + " 08:00:00"
            result.eight = result.eight - 1
        elif hour == "nine":
            if result.nine == 0:
                return jsonify(
                    Answer="capacity is full"
                )
            time = date + " 09:00:00"
            result.nine = result.nine - 1
        elif hour == "ten":
            if result.ten == 0:
                return jsonify(
                    Answer="capacity is full"
                )
            time = date + " 10:00:00"
            result.ten = result.ten - 1
        elif hour == "eleven":
            if result.eleven == 0:
                return jsonify(
                    Answer="capacity is full"
                )
            time = date + " 11:00:00"
            result.eleven = result.eleven - 1
        elif hour == "twelve":
            if result.twelve == 0:
                return jsonify(
                    Answer="capacity is full"
                )
            time = date + " 12:00:00"
            result.twelve = result.twelve - 1
        elif hour == "thirteen":
            if result.thirteen == 0:
                return jsonify(
                    Answer="capacity is full"
                )
            time = date + " 13:00:00"
            result.thirteen = result.thirteen - 1
        elif hour == "fourteen":
            if result.fourteen == 0:
                return jsonify(
                    Answer="capacity is full"
                )
            time = date + " 14:00:00"
            result.fourteen = result.fourteen - 1
        elif hour == "fifteen":
            if result.fifteen == 0:
                return jsonify(
                    Answer="capacity is full"
                )
            time = date + " 15:00:00"
            result.fifteen = result.fifteen - 1
        elif hour == "sixteen":
            if result.sixteen == 0:
                return jsonify(
                    Answer="capacity is full"
                )
            time = date + " 16:00:00"
            result.sixteen = result.sixteen - 1
        elif hour == "seventeen":
            if result.seventeen == 0:
                return jsonify(
                    Answer="capacity is full"
                )
            time = date + " 17:00:00"
            result.seventeen = result.seventeen - 1
        elif hour == "eighteen":
            if result.eighteen == 0:
                return jsonify(
                    Answer="capacity is full"
                )
            time = date + " 18:00:00"
            result.eighteen = result.eighteen - 1
        elif hour == "nineteen":
            if result.nineteen == 0:
                return jsonify(
                    Answer="capacity is full"
                )
            time = date + " 19:00:00"
            result.nineteen = result.nineteen - 1
        try:
            session.commit()
        except:
            session.rollback()
        reserve = Reserve(phonenumber=phonenumber, date=date, hour=hour, time=time, currentdate=currentdate,
                          washcarbody=washcarbody, washengine=washengine, waxdashboard=waxdashboard,
                          waxinsidedoor=waxinsidedoor, waxwheels=waxwheels, vacuuminside=vacuuminside,
                          vacuumtrunk=vacuumtrunk, totalcost=cost, situation = "okay")
        session.add(reserve)
        try:
            session.commit()
            print(str(reserve.phonenumber) + "reserved successfully")
        except Exception as e:
            print(e)
            session.rollback()
        print(date, hour, phonenumber, "Successfully reserved.")
        return jsonify(
            Answer="Successfully reserved."
        )

    else:
        return jsonify(
            Answer="somethings wrong"
        )


@app.route('/show_hours', methods=['POST'])
def show_hours():
    print(request.data.decode("utf-8"))
    date = request.json.get('Date')
    result = session.query(Date).filter(Date.date == date).first()
    if result is not None:
        print(result.date, "founded")
        return jsonify(
            eight=str(result.eight),
            nine=str(result.nine),
            ten=str(result.ten),
            eleven=str(result.eleven),
            twelve=str(result.twelve),
            thirteen=str(result.thirteen),
            fourteen=str(result.fourteen),
            fifteen=str(result.fifteen),
            sixteen=str(result.sixteen),
            seventeen=str(result.seventeen),
            eighteen=str(result.eighteen),
            nineteen=str(result.nineteen)
        )

    else:
        print("we have no such date")
        return jsonify(
            Answer="something is wrong"
        )


@app.route('/show_reserves', methods=['POST'])
def show_reserves():
    print(request.data.decode("utf-8"))
    phonenumber = request.json.get('PhoneNumber')
    result = session.query(Reserve).filter(Reserve.phonenumber == phonenumber).all()
    all_reserves = [{'Date': Reserve.date, 'Hour': Reserve.hour, 'Time': Reserve.time, 'CurrentDate': Reserve.currentdate,
                     'WashCarbody': Reserve.washcarbody,
                     'WashEngine': Reserve.washengine, 'WaxDashboard': Reserve.waxdashboard,
                     'WaxInsideDoor': Reserve.waxinsidedoor, 'WaxWheels': Reserve.waxwheels,
                     'VacuumInside': Reserve.vacuuminside, 'VacuumTrunk': Reserve.vacuumtrunk,
                     'TotalCost': Reserve.totalcost,
                     'Situation': Reserve.situation
                     } for Reserve in result]
    if result is not None:

        return jsonify(reserves=all_reserves)

    else:
        print("we have no such date")
        return jsonify(
            Answer="something is wrong"
        )




@app.route('/cancel_reserve', methods=['POST'])
def cancel_reserve():
    print(request.data.decode("utf-8"))
    phonenumber = request.json.get('PhoneNumber')
    current_time = request.json.get('CurrentTime')
    result = session.query(Reserve).filter(Reserve.phonenumber == phonenumber, Reserve.currentdate == current_time, Reserve.situation == "okay").first()
    result2 = session.query(Date).filter(Date.date == result.date).first()
    result3 = session.query(User).filter(User.phonenumber == phonenumber).first()
    if result is not None :
        result3.credit = result3.credit + result.totalcost
        result.situation = "canceled"
        if result.hour == "eight":
            result2.eight = result2.eight + 1
        if result.hour == "nine":
            result2.nine = result2.nine + 1
        if result.hour == "ten":
            result2.ten = result2.ten + 1
        if result.hour == "eleven":
            result2.eleven = result2.eleven + 1
        if result.hour == "twelve":
            result2.twelve = result2.twelve + 1
        if result.hour == "thirteen":
            result2.thirteen = result2.thirteen + 1
        if result.hour == "fourteen":
            result2.fourteen = result2.fourteen + 1
        if result.hour == "fifteen":
            result2.fifteen = result2.fifteen + 1
        if result.hour == "sixteen":
            result2.sixteen = result2.sixteen + 1
        if result.hour == "seventeen":
            result2.seventeen = result2.seventeen + 1
        if result.hour == "eighteen":
            result2.eighteen = result2.eighteen + 1
        if result.hour == "nineteen":
            result2.nineteen = result2.nineteen + 1
        try:
            session.commit()
        except:
            session.rollback()
        return jsonify(
            Answer="Successfully Canceled"
        )

    else:
        print("we have no such date")
        return jsonify(
            Answer="something is wrong"
        )




@app.route('/contact_us', methods=['POST'])
def contact_us():
    print(request.data.decode("utf-8"))
    phonenumber = request.json.get('PhoneNumber')
    submitdate = request.json.get('SubmitDate')
    message = request.json.get('Message')
    result = session.query(User).filter(User.phonenumber == phonenumber).first()
    if result is not None:
        m = Message(phonenumber=phonenumber, submitdate=submitdate,
                    message=message)
        session.add(m)
        try:
            session.commit()
        except Exception as e:
            session.rollback()
            print(e)
        return jsonify(
            Answer="Message Received Successfully"
        )

    else:
        return jsonify(
            Answer="something is wrong"
        )





@app.route('/get_name', methods=['POST'])
def get_name():
    print(request.data.decode("utf-8"))
    phonnumber = request.json.get('PhoneNumber')
    result = session.query(User).filter(User.phonenumber == phonnumber).first()
    if result is not None:
        print(result.phonenumber, "founded")
        firstname = result.firstname
        lastname = result.lastname
        return jsonify(
            FirstName = firstname,
            LastName = lastname
        )

    else:
        print("we have no such date")
        return jsonify(
            Answer="something is wrong"
        )












if __name__ == "__main__":
    app.run()
