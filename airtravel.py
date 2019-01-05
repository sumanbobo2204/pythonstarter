"""Model for aircraft flights """


class Flight:
    """A flight with a particular passenger aircraft. """

    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError("No airline code in {}".format(number))
        if not number[:2].isupper():
            raise ValueError("Invalid airline code {}".format(number))
        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError("Invalid route number {}".format(number))
        self._number = number
        self._aircraft = aircraft

        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def flight_number(self):
        return self._number

    def airline_code(self):
        return self._number[:2]

    def aircraft_model(self):
        return self._aircraft.model_number()

    def allocate_seat(self, seat, passenger_name):
        """
        Args:
            seat: A seat designator such as '12C' or '21F' etc.
            passenger_name: The passenger name

        :param passenger_name:
        :param seat
        :return:
        """
        rows, seat_letters = self._aircraft.seating_plan()
        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError("Invalid seat number {}".format(letter))
        row_num = seat[:-1]
        try:
            row = int(row_num)
        except ValueError:
            raise ValueError("Invalid seat row number".format(row_num))

        if row not in rows:
            raise ValueError("Invalid row number {}".format(row))

        if self._seating[row][letter] is not None:
            raise ValueError("Seat already occupied {}".format(seat))

        self._seating[row][letter] = passenger_name
        print("Allocating seat -->> {}".format(self._seating[row][letter]))

    def unpack_seat(self, seat):
        """
        :param seat:
        :return:
        """
        row_num = seat[:-1]
        seat_letter = seat[-1]
        return row_num, seat_letter

    def relocate_passenger(self, from_seat, to_seat):
        """
        :param from_seat:
        :param to_seat:
        :return:
        """
        from_row, from_seat_num = self.unpack_seat(from_seat)
        if self._seating[from_row][from_seat_num] is None:
            raise ValueError("No passenger to relocate from {a} {b}".format(a=from_row, b=from_seat))

        to_row, to_seat_num = self.unpack_seat(to_seat)
        if self._seating[to_row][to_seat_num] is not None:
            raise ValueError("Passenger already occupied in the to seat {0} {1}".format(to_row, to_seat))

        self._seating[to_row][to_seat_num] = self._seating[from_row][from_seat_num]
        self._seating[from_row][from_seat_num] = None

    def number_of_available_seat(self):
        """
        number_of_available_seat
        :return:
        """
        return sum(sum(1 for s in row.values() if s is None) for row in self._seating if row is not None)

    def make_boarding_cards(self, card_printer):
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(passenger, seat, self.flight_number(), self.aircraft_model())

    def _passenger_seats(self):
        """An iterable series of passenger seating allocations."""
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield (passenger, "{}{}".format(row, letter))


class Aircraft:

    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration_number(self):
        return self._registration

    def model_number(self):
        return self._model

    def seating_plan(self):
        return range(1, self._num_rows), "ABCDEFGHJK"[:self._num_seats_per_row]


def console_card_printer(passenger, seat, flight_number, aircraft):
    output = "| Name: {0}"     \
             "  Flight: {1}"   \
             "  Seat: {2}"     \
             "  Aircraft: {3}" \
             " |".format(passenger, flight_number, seat, aircraft)
    banner = '+' + '-' * (len(output) - 2) + '+'
    border = '|' + ' ' * (len(output) - 2) + '|'
    lines = [banner, border, output, border, banner]
    card = '\n'.join(lines)
    print(card)
    print()
