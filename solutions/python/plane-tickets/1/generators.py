"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    for i in range(number):
        yield chr(i % 4 + 65) 


def generate_seats(number):
    letter = generate_seat_letters(number)
    for i in range(number):
        if i // 4 +1 >= 13 :
            i += 4
        yield str(i // 4 +1) + next(letter)


def assign_seats(passengers):
    seats = generate_seats(len(passengers))
    result = {}
    for passenger, seat in zip(passengers, seats):
        result[passenger] = seat
    return result

def generate_codes(seat_numbers, flight_id):
    for seat in seat_numbers:
        yield seat + flight_id + '0' * (6 - len(seat)) 