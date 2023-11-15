from models import Product
from config import Session
import os
import csv
from decimal import Decimal


def save_to_csv(filename, fieldnames, data_dict):
    file_exists = os.path.exists(filename)
    with open(filename, "a", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(data_dict)


def calc_computer_rating(model):
    with Session() as session:
        product = session.get(Product, model)
        if product is None:
            raise ValueError("Invalid model name")

        if product.type == "PC":
            computers = product.pcs
        elif product.type == "Laptop":
            computers = product.laptops
        else:
            raise ValueError("Invalid product type")
        
        for computer in computers:
            if computer.price is None:
                raise ValueError("The computer has no price")
            rating = (computer.ram + computer.hd) / computer.price * computer.speed
            save_to_csv("computer_rating.csv", ["model", "rating"], {"model": model, "rating": rating})


def create_banded_pack_1(pc, printer):
    save_to_csv(
        "banded_packs_1.csv",
        ["pack_name", "pc_code", "pc_price", "printer_code", "printer_price", "price"],
        {
            "pack_name": "pc + printer",
            "pc_code": pc.code,
            "pc_price": pc.price,
            "printer_code": printer.code, 
            "printer_price": printer.price, 
            "price": Decimal("0.9") * (pc.price + printer.price)
        }
    )


def create_banded_pack_2(laptop, printer):
    save_to_csv(
        "banded_packs_2.csv",
        ["pack_name", "laptop_code", "laptop_price", "printer_code", "printer_price", "price"],
        {
            "pack_name": "laptop + printer",
            "laptop_code": laptop.code,
            "laptop_price": laptop.price,
            "printer_code": printer.code, 
            "printer_price": printer.price, 
            "price": Decimal("0.9") * (laptop.price + printer.price)
        }
    )