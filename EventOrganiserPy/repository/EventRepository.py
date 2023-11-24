
from entities.Event import Event


class EventRepository:
    def __init__(self, events):
        self.events = events
    # Adaugarea unui eveniment in lista de evenimente
    def add_event(self, event: Event):
        self.events.append(event)

    # Stergerea unui eveniment din lista de evenimente (identificat dupa id-ul evenimentului)
    def delete_event(self, event_id: str):
        self.events = [event for event in self.events if event.id != event_id]

    # Modificarea datelor unui eveniment din lista de evenimente (identificat dupa id-ul
    # evenimentului)
    def update_event(self, event_id: str, updated_event: Event):
        index = next((index for (index, event) in enumerate(
            self.events) if event.id == event_id), None)
        if index is not None:
            self.events[index] = updated_event

    def get_event_by_id(self, event_id: str):
        for event in self.events:
            if event.id == event_id:
                return event
        return None

    # Vizualizarea listei de evenimente
    def get_all_events(self):
        return self.events

    # Vizualizarea evenimentelor dintr-un anumit oras
    def get_events_by_city(self, city: str):
        return [event for event in self.events if event.city == city]

    # Vizualizarea participantilor de la un anumit eveniment
    def get_participants_for_event(self, event_id):
        event = [event for event in self.events if event.id == event_id][0]
        return event.participants
    
    # Vizualizarea evenimentelor care au participanti, sortate descrescator dupa numarul
    # de participanti (afisati numarul de participanti si restul detaliilor evenimentelor)
    def get_events_with_participants_sorted(self):
        # Pasul 1: filtram evenimente care au participanti
        events_with_participants = []
        for event in self.events:
            if event.participants:  # If the event has participants
                events_with_participants.append(event)

        # Pasul 2: sortam evenimentele dupa numarul de participanti
        sorted_events = sorted(events_with_participants, key=lambda event: len(event.participants), reverse=True)

        # Pasul 3: printam evenimentele sortate
        for event in sorted_events:
            print('Event ' + event.title + ' has ' + str(len(event.participants)) + ' participant(s):')
            print(str(event))
            print() 

        # Pasul 4: returnam evenimentele sortate
        return sorted_events




