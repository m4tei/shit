from entities.Event import Event
from entities.Participant import Participant


from entities.Participant import Participant
from service.ParticipantService import ParticipantService


class UI:
    def run(self):
        self.display_menu(self.main_menu)
    
    def __init__(self, event_service, participant_service):
        self.event_service = event_service
        self.participant_service = participant_service
        self.main_menu = {
            "1": ("Meniu Organizator", self.organizer_menu),
            "2": ("Meniu Participant", self.participant_menu),
            "0": ("Ieșire", exit)
        }
        self.organizer_menu_options = {
            "1": ("Adaugă un eveniment", self.add_event),
            "2": ("Șterge un eveniment", self.delete_event),
            "3": ("Actualizează un eveniment", self.update_event),
            "4": ("Vezi un eveniment după ID", self.get_event_by_id),
            "5": ("Vezi toate evenimentele", self.get_all_events),
            "6": ("Vezi evenimentele după oraș", self.get_events_by_city),
            "7": ("Vezi participanții unui eveniment", self.get_participants_for_event),
            "8": ("Vezi evenimentele cu participanți sortați", self.get_events_with_participants_sorted),
            "0": ("Înapoi", self.main_menu)
        }
        self.participant_menu_options = {
            "1": ("Vezi toate evenimentele", self.view_events),
            "2": ("Înregistrează-te la un eveniment", self.register_to_event),
            "3": ("Vezi evenimentele care încep în următoarele 7 zile", self.view_events_in_next_week_sorted),
            "4": ("Vezi evenimentele care încep într-o anumită lună, sortate după durată", self.view_events_in_month_sorted_by_duration),
            "0": ("Înapoi", self.main_menu)
        }

    def organizer_menu(self):
        self.display_menu(self.organizer_menu_options)

    def participant_menu(self):
        self.display_menu(self.participant_menu_options)

    def add_event(self):
        event_id = input("Vă rugăm să introduceți ID-ul evenimentului: ")
        event_title = input("Vă rugăm să introduceți numele evenimentului: ")
        event_city = input("Vă rugăm să introduceți orașul unde va avea loc evenimentul: ")
        event_max_participants = int(input("Vă rugăm să introduceți numărul maxim de participanți la eveniment: "))
        event_start_date = input("Vă rugăm să introduceți data de început a evenimentului (format aaaa-ll-zz): ")
        event_end_date = input("Vă rugăm să introduceți data de sfârșit a evenimentului (format aaaa-ll-zz): ")
        event_participants = []
    
        event = Event(event_id, event_title, event_city, event_participants, event_max_participants, event_start_date, event_end_date)
        self.event_service.add_event(event)
        print("Eveniment adăugat cu succes.")


    def delete_event(self):
        event_id = input("Vă rugăm să introduceți ID-ul evenimentului pe care doriți să îl ștergeți: ")
        self.event_service.delete_event(event_id)
        print("Eveniment șters cu succes.")

    def update_event(self):
        event_id = input("Vă rugăm să introduceți ID-ul evenimentului pe care doriți să îl actualizați: ")
        updated_event_title = input("Vă rugăm să introduceți noul nume al evenimentului: ")
        updated_event_city = input("Vă rugăm să introduceți noul oraș în care va avea loc evenimentul: ")
        updated_event_max_participants = int(input("Vă rugăm să introduceți noul număr maxim de participanți la eveniment: "))
        updated_event_start_date = input("Vă rugăm să introduceți noua dată de început a evenimentului (format aaaa-ll-zz): ")
        updated_event_end_date = input("Vă rugăm să introduceți noua dată de sfârșit a evenimentului (format aaaa-ll-zz): ")
        updated_event_participants = []
    
        updated_event = Event(event_id, updated_event_title, updated_event_city, updated_event_participants, updated_event_max_participants, updated_event_start_date, updated_event_end_date)
        self.event_service.update_event(event_id, updated_event)
        print("Eveniment actualizat cu succes.")
    

    def get_event_by_id(self):
        event_id = input("Vă rugăm să introduceți ID-ul evenimentului pe care doriți să îl vizualizați: ")
        event = self.event_service.get_event_by_id(event_id)
        print(event)

    def get_all_events(self):
        events = self.event_service.get_all_events()
        for event in events:
            print(event) 

    def get_events_by_city(self):
        city = input("Vă rugăm să introduceți orașul în care au avut loc evenimentele: ")
        events = self.event_service.get_events_by_city(city)
        for event in events:
            print(event) 

    def get_participants_for_event(self):
        event_id = input("Vă rugăm să introduceți ID-ul evenimentului pentru care doriți să vizualizați participanții: ")
        participants = self.event_service.get_participants_for_event(event_id)
        for participant in participants:
            print(participant) 

    def get_events_with_participants_sorted(self):
        events = self.event_service.get_events_with_participants_sorted()
        for event in events:
            print(event) 
    
    def view_events(self):
        events = self.event_service.get_all_events()
        for event in events:
            print(event)

    def register_to_event(self):
        event_id = input("Vă rugăm să introduceți ID-ul evenimentului la care doriți să vă înregistrați: ")
        participant_id = input("Vă rugăm să introduceți ID-ul dvs. de participant: ")
        self.participant_service.register_to_event(event_id, participant_id)
        print("Înregistrare reușită.")

    def view_events_in_next_week_sorted(self):
        events = self.participant_service.get_events_in_next_week_sorted()
        for event in events:
            print(event)

    def view_events_in_month_sorted_by_duration(self):
        month = input("Vă rugăm să introduceți luna pentru care doriți să vizualizați evenimentele (format ll): ")
        events = self.participant_service.get_events_in_month_sorted_by_duration(month)
        for event in events:
            print(event)
    
    def display_menu(self, menu_options):
        while True:
            print("\nOpțiuni meniu:")
            for key, value in menu_options.items():
                print(f"{key}: {value[0]}")
            user_choice = input("Alegeți o opțiune: ")
            if user_choice in menu_options:
                if user_choice == '0':
                    break
                else:
                    menu_options[user_choice][1]()
            else:
                print("Opțiune invalidă, încercați din nou.")


