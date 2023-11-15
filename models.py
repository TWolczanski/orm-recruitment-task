from typing import List
from sqlalchemy import ForeignKey, String, Numeric
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Product(Base):
    __tablename__ = "product"

    model: Mapped[str] = mapped_column(String(50), primary_key=True)
    maker: Mapped[str] = mapped_column(String(10))
    type: Mapped[str] = mapped_column(String(50))
    pcs: Mapped[List["PC"]] = relationship(back_populates="product")
    laptops: Mapped[List["Laptop"]] = relationship(back_populates="product")
    printers: Mapped[List["Printer"]] = relationship(back_populates="product")


class PC(Base):
    __tablename__ = "pc"

    code: Mapped[int] = mapped_column(primary_key=True)
    model: Mapped[str] = mapped_column(ForeignKey("product.model"))
    product: Mapped["Product"] = relationship(back_populates="pcs")
    speed: Mapped[int]
    ram: Mapped[int]
    hd: Mapped[int]
    cd: Mapped[str] = mapped_column(String(10))
    price = mapped_column(Numeric(8, 2), nullable=True)


class Laptop(Base):
    __tablename__ = "laptop"

    code: Mapped[int] = mapped_column(primary_key=True)
    model: Mapped[str] = mapped_column(ForeignKey("product.model"))
    product: Mapped["Product"] = relationship(back_populates="laptops")
    speed: Mapped[int]
    ram: Mapped[int]
    hd: Mapped[int]
    screen: Mapped[int]
    price = mapped_column(Numeric(8, 2), nullable=True)


class Printer(Base):
    __tablename__ = "printer"

    code: Mapped[int] = mapped_column(primary_key=True)
    model: Mapped[str] = mapped_column(ForeignKey("product.model"))
    product: Mapped["Product"] = relationship(back_populates="printers")
    color: Mapped[str] = mapped_column(String(1))
    type: Mapped[str] = mapped_column(String(10))
    price = mapped_column(Numeric(8, 2), nullable=True)