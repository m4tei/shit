
class ParticipantService:
    def __init__(self, participant_repository):
        self.participant_repository = participant_repository

    # Vizualizarea listei de evenimente (afisati toate datele evenimentelor, inclusiv id-urile lor)
    def view_events(self):
        return self.participant_repository.view_events()

    # Inscrierea la un anumit eveniment. Pentru inscrierea la un eveniment, se introduc id-ului
    # evenimentului si datele participantului.
    def register_to_event(self, event_id, participant_id):
        return self.repository.register_to_event(event_id, participant_id)
    
    # Vizualizarea evenimentelor care incep in urmatoarele 7 zile, sortate crescator dupa
    # numarul maxim de locuri (afisati toate detaliile evenimentelor)
    def get_events_in_next_week_sorted(self):
        return self.participant_repository.get_events_in_next_week_sorted()
    
    # Vizualizarea evenimentelor care au data de inceput intr-o anumita luna, sortate
    # descrescator dupa durata (se va citi intai luna si apoi se vor afisa toate evenimentele
    # corespunzatoare, inclusiv duratele lor! Durata unui eveniment reprezinta diferenta, in
    # zile, dintre data de final si data de inceput)
    def get_events_in_month_sorted_by_duration(self, month):
        return self.participant_repository.get_events_in_month_sorted_by_duration(month)
