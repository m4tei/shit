from datetime import datetime, timedelta


class ParticipantRepository:

    def __init__(self, events, participants):
        self.events = events
        self.participants = participants

    # Vizualizarea listei de evenimente (afisati toate datele evenimentelor, inclusiv id-urile lor)
    def view_events(self):
        return self.events

    def find_participant_by_id(self, participant_id):
        for participant in self.participants:
            if participant.id == participant_id:
                return participant
        return None
    
    def find_event_by_id(self, event_id):
        for event in self.events:
            if event.id == event_id:
                return event
        return None


    # Inscrierea la un anumit eveniment. Pentru inscrierea la un eveniment, se introduc id-ului
    # evenimentului si datele participantului. In momentul inscrierii, se va incrementa numarul
    # de participanti pentru evenimentul respectiv. In cazul in care nu mai sunt locuri disponibile
    # la eveniment, se va afisa un mesaj corespunzator
    def register_to_event(self, event_id, participant_id):
        event = self.find_event_by_id(event_id)
        participant = self.find_participant_by_id(participant_id)
        if event and participant and len(event.participants) < event.max_participants:
            event.participants.append(participant)
            participant.event_ids.append(event.id)
            return "Registration successful."
        else:
            return "Registration failed. Either the event is full, the event doesn't exist or the participant doesn't exist."

    # Vizualizarea evenimentelor care incep in urmatoarele 7 zile, sortate crescator dupa
    # numarul maxim de locuri (afisati toate detaliile evenimentelor)
    def get_events_in_next_week_sorted(self):
        today = datetime.today()
        next_week = today + timedelta(days=7)
        return sorted([event for event in self.events if datetime.strptime(event.start_date, "%Y-%m-%d") >= today and datetime.strptime(event.start_date, "%Y-%m-%d") <= next_week], key=lambda event: event.max_participants)

    # Vizualizarea evenimentelor care au data de inceput intr-o anumita luna, sortate
    # descrescator dupa durata (se va citi intai luna si apoi se vor afisa toate evenimentele
    # corespunzatoare, inclusiv duratele lor! Durata unui eveniment reprezinta diferenta, in
    # zile, dintre data de final si data de inceput)

    def get_events_in_month_sorted_by_duration(self, month):
        relevant_events = [event for event in self.events if datetime.strptime(event.start_date, "%Y-%m-%d").month == int(month)]
        return sorted(relevant_events, key=lambda event: (datetime.strptime(event.end_date, "%Y-%m-%d") - datetime.strptime(event.start_date, "%Y-%m-%d")).days, reverse=True)
