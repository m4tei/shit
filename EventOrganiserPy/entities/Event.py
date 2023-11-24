class Event:
    def __init__(self, id, title, city, participants, max_participants, start_date, end_date):
        self.id = id
        self.title = title
        self.city = city
        self.participants = participants
        self.max_participants = max_participants
        self.start_date = start_date
        self.end_date = end_date

    def __str__(self):
        return f'Event(id: {self.id}, title: {self.title}, city: {self.city}, participants: {self.participants}, max_participants: {self.max_participants}, start_date: {self.start_date}, end_date: {self.end_date})'

    def __eq__(self, other):
        if not isinstance(other, Event):
            return NotImplemented
        return self.id == other.id
