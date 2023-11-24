class EventService:
    def __init__(self, event_repository):
        self.event_repository = event_repository

    # Adăugarea unui eveniment în lista de evenimente
    def add_event(self, event):
        self.event_repository.add_event(event)

    # Ștergerea unui eveniment din lista de evenimente (identificat după id-ul evenimentului)
    def delete_event(self, event_id):
        self.event_repository.delete_event(event_id)

    # Modificarea datelor unui eveniment din lista de evenimente (identificat după id-ul evenimentului)
    def update_event(self, event_id, updated_event):
        self.event_repository.update_event(event_id, updated_event)

    # Obținerea unui eveniment după id
    def get_event_by_id(self, event_id):
        return self.event_repository.get_event_by_id(event_id)

    # Vizualizarea listei de evenimente
    def get_all_events(self):
        return self.event_repository.get_all_events()

    # Vizualizarea evenimentelor dintr-un anumit oraș
    def get_events_by_city(self, city):
        return self.event_repository.get_events_by_city(city)

    # Vizualizarea participanților de la un anumit eveniment
    def get_participants_for_event(self, event_id):
        return self.event_repository.get_participants_for_event(event_id)

    # Vizualizarea evenimentelor care au participanți, sortate descrescător după numărul de participanți
    def get_events_with_participants_sorted(self):
        return self.event_repository.get_events_with_participants_sorted()
