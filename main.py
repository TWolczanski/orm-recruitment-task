from models import Product, PC, Laptop, Printer
from decimal import Decimal
from config import Session
from utils import *


with Session.begin() as session:
    pc_product = Product(model="pcmodel", maker="pcmaker", type="PC")
    pc = PC(product=pc_product, speed=1, ram=1, hd=1, cd="cd", price=Decimal("5499.99"))
    session.add(pc)

    laptop_product = Product(model="laptopmodel", maker="laptopmaker", type="Laptop")
    laptop = Laptop(product=laptop_product, speed=2, ram=2, hd=2, screen=2, price=Decimal("1999.99"))
    session.add(laptop)

    printer_product = Product(model="printermodel", maker="printermaker", type="Printer")
    printer = Printer(product=printer_product, color="y", type="type", price=Decimal("999.99"))
    session.add(printer)

calc_computer_rating("pcmodel")
calc_computer_rating("laptopmodel")

with Session() as session:
    pc = session.query(PC).filter(PC.model == "pcmodel").first()
    laptop = session.query(Laptop).filter(Laptop.model == "laptopmodel").first()
    printer = session.query(Printer).filter(Printer.model == "printermodel").first()

    create_banded_pack_1(pc, printer)
    create_banded_pack_2(laptop, printer)