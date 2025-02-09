from collections import UserDict

class InvalidPhoneNumberException(Exception):
    pass

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        if len(value) == 10 and all(x.isdigit() for x in value[::1]):
            super().__init__(value)
        else:
            raise InvalidPhoneNumberException()        

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))
    
    def edit_phone(self, oldphone, newphone):
        phones = []
        for phone in self.phones:
            if phone.value == oldphone:
                phone.value = newphone
            phones.append(phone)
        self.phones = phones
    
    def remove_phone(self, phone_to_remove):
        phones = []
        for phone in self.phones:
            if phone.value != phone_to_remove:
                phones.append(phone)
        self.phones = phones

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data[name]
    
    def delete(self, name):
        self.data.pop(name)

def main():
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    john.remove_phone("1112223333")
    print(john)  # Виведення: Contact name: John, phones: 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone.value if found_phone else "Phone not found."}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")
    for name, record in book.data.items():
        print(record)

if __name__ == "__main__":
    main()