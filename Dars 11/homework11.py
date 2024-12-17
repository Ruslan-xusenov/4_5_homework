from os import *
system('clear')


class Room:
    def __init__(self, room_number, room_type, is_occupied=False):
        self.room_number = room_number
        self.room_type = room_type
        self.is_occupied = is_occupied

    def __str__(self):
        status = "Band" if self.is_occupied else "Bo'sh"
        return f"Xona raqami: {self.room_number}, Turi: {self.room_type}, Holati: {status}"


class Guest:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    def __str__(self):
        return f"Ismi: {self.name}, Telefon raqami: {self.phone_number}"


class HotelManager:
    def __init__(self):
        self.rooms = []
        self.guests = {}

    def add_room(self, room_number, room_type):
        room = Room(room_number, room_type)
        self.rooms.append(room)
        print(f"{room_number}-raqamli xona muvaffaqiyatli qo'shildi")

    def list_rooms(self):
        print("Xonalar ro'yxati:")
        for room in self.rooms:
            print(room)

    def check_availability(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                return not room.is_occupied
        return False

    def book_room(self, room_number, guest_name, guest_phone):
        for room in self.rooms:
            if room.room_number == room_number:
                if not room.is_occupied:
                    guest = Guest(guest_name, guest_phone)
                    self.guests[room_number] = guest
                    room.is_occupied = True
                    print(f"{room_number}-raqamli xona {guest_name} uchun band qilindi")
                    return
                else:
                    print(f"{room_number}-raqamli xona allaqachon band")
                    return
        print(f"{room_number}-raqamli xona topilmadi")

    def release_room(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                if room.is_occupied:
                    room.is_occupied = False
                    del self.guests[room_number]
                    print(f"{room_number}-raqamli xona bo'shatildi")
                    return
                else:
                    print(f"{room_number}-raqamli xona allaqachon bo'sh")
                    return
        print(f"{room_number}-raqamli xona mavjud emas")

    def list_guests(self):
        print("Ijarachilar ro'yxati:")
        for room_number, guest in self.guests.items():
            print(f"Xona raqami: {room_number}, {guest}")


if __name__ == "__main__":
    manager = HotelManager()

    manager.add_room(101, "Yangi")
    manager.add_room(102, "Ikki kishilik")

    manager.list_rooms()

    manager.book_room(101, "Ali", "+998901234567")
    manager.book_room(102, "Vali", "+998931234567")

    manager.list_rooms()

    manager.list_guests()

    manager.release_room(101)

    manager.list_rooms()
    manager.list_guests()
