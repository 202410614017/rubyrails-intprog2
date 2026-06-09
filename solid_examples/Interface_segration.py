# Interface Segregation — Hilmi Arda Dagci

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def eat(self): pass

    @abstractmethod
    def fly(self): pass

    @abstractmethod
    def swim(self): pass


class Eagle(Animal):
    def eat(self): print("Kartal yiyor")
    def fly(self): print("Kartal ucuyor")
    def swim(self): pass  # Kartal yuzmez!


class Dog(Animal):
    def eat(self): print("Kopek yiyor")
    def fly(self): pass   # Kopek ucamaz!
    def swim(self): print("Kopek yuzuyor")


class Eatable(ABC):
    @abstractmethod
    def eat(self): pass


class Flyable(ABC):
    @abstractmethod
    def fly(self): pass


class Swimmable(ABC):
    @abstractmethod
    def swim(self): pass


class EagleGood(Eatable, Flyable):
    def eat(self): print("Kartal yiyor")
    def fly(self): print("Kartal ucuyor")


class DogGood(Eatable, Swimmable):
    def eat(self): print("Kopek yiyor")
    def swim(self): print("Kopek yuzuyor")


class Cat(Eatable):
    def eat(self): print("Kedi yiyor")
