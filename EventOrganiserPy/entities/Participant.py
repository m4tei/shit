class Participant:
    def __init__(self, id, name, picture_link, event_ids):
        self.id = id
        self.name = name
        self.picture_link = picture_link
        self.event_ids = event_ids

    def __str__(self):
        return f'Participant(id: {self.id}, name: {self.name}, picture_link: {self.picture_link}, event_ids: {self.event_ids})'

    def __eq__(self, other):
        if not isinstance(other, Participant):
            return NotImplemented
        return self.id == other.id
