from ui.UI import UI
from entities.Event import Event
from entities.Participant import Participant
from repository.EventRepository import EventRepository
from repository.ParticipantRepository import ParticipantRepository
from service.EventService import EventService
from service.ParticipantService import ParticipantService


def main():
    # Creaza datele initiale

    participants = [
        Participant(1, "Matei Rus", "link_to_image1", []),
        Participant(2, "Maria Vasilescu", "link_to_image2", []),
        Participant(3, "Andrei Ionescu", "link_to_image3", []),
    ]

    events = [
        Event("E1", "Concert Rock", "Bucuresti", [], 100, "2023-08-30", "2023-09-02"),
        Event("E2", "Festival de Film", "Cluj", [], 200, "2023-10-15", "2023-10-20"),
        Event("E3", "Opera", "Iasi", participants, 50, "2023-11-05", "2023-11-08"),
        Event("E4", "UNTOLD", "Cluj-Napoca", participants, 50000, "2023-08-06", "2023-08-09"),
        Event("E4", "EC", "Cluj-Napoca", participants, 30000, "2023-08-01", "2023-08-01"),
    ]


    # Initializeaza repository-urile cu datele create
    event_repository = EventRepository(events)
    participant_repository = ParticipantRepository(events, participants)

    # Creaza serviciile bazate pe repository-urile create
    event_service = EventService(event_repository)
    participant_service = ParticipantService(participant_repository)

    # Creaza UI-ul bazat pe serviciile create
    ui = UI(event_service, participant_service)

    # Porneste aplicatia
    ui.run()


# Ruleaza functia main() doar daca acest fisier este executat direct (nu este importat ca un modul)
if __name__ == "__main__":
    main()