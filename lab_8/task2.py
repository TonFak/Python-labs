from peewee import *
from datetime import date

db = SqliteDatabase("lr8.db")

class Vehicle(Model):
    id_vehicle = PrimaryKeyField()
    mark = TextField()
    date = DateField()
    color = TextField()

    class Meta:
        database = db

class Sender(Model):
    id_sender = PrimaryKeyField()
    last_name = TextField()
    name = TextField()
    patronymic= TextField()
    birth = DateField()
    code = TextField()
    city = TextField()
    street = TextField()
    house = TextField()
    flat = TextField()
    phone= TextField()

    class Meta:
        database = db

class Order(Model):
    id_order = PrimaryKeyField()
    id_sender = IntegerField()
    id_recipient = IntegerField()
    date = DateField()
    delivery_date = DateField()
    delivery_price = FloatField()
    id_courier = IntegerField()
    id_vehicle= IntegerField()

    class Meta:
        database = db


db.create_tables([Vehicle, Sender, Order])

transport_1 = Vehicle(mark="Audi", date=date(2023, 11, 2), color="Red")
transport_1.save()

transport_2 = Vehicle(mark="BMW", date=date(2023, 8, 12), color="Black")
transport_2.save()

sender_1 = Sender(last_name="Rampamzam",name="Susan", patronymic="Lzurovich",
                      birth=date(1980, 11, 30), code="101000", city="Saint Petersburg",
                      street="Nevsky Prospect", house="103", flat="4", phone="89031111255")
sender_1.save()

sender_2 = Sender(last_name="Sidrov", name="Petr", patronymic="Sidrovich",
                     birth=date(1990, 7, 25), code="211020", city="Moscow",
                      street="Tverskaya", house="25", flat="5", phone="89413366677")
sender_2.save()

order_1 = Order(id_sender=2, id_recipient=1, date=date(2024, 12, 10),
                delivery_date=date(2024, 12, 15), delivery_price=13.75, id_courier=2, id_vehicle=1)
order_1.save()

order_2 = Order(id_sender=1, id_recipient=2, date=date(2024, 11, 13),
                delivery_date=date(2024, 11, 14), delivery_price=372.40, id_courier=2, id_vehicle=2)
order_2.save()