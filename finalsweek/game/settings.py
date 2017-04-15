settings = {
    "hand_size": 6,
    "total_cards": 1000,
    "seat_rows": 5,
    "seat_columns": 4,
    "game_definition": [
        {
            "name": "GameStart",
            "phase_sets": 1,
            "phases": [
                {
                    "name": "Choose Seats",
                    "turn_sets": 1,
                    "automatic": False
                }
            ]
        },
        {
            "name": "Play",
            "phase_sets": 10,
            "phases": [
                {
                    "name": "Accumulation",
                    "turn_sets": 1,
                    "automatic": True
                },
                {
                    "name": "Classtime",
                    "turn_sets": 2,
                    "automatic": False
                },
                {
                    "name": "Dismissal",
                    "turn_sets": 1,
                    "automatic": False
                },
                {
                    "name": "After School",
                    "turn_sets": 1,
                    "automatic": False
                }
            ]
        },
        {
            "name": "Scoring",
            "phase_sets": 1,
            "phases": [
                {
                    "name": "Score",
                    "turn_sets": 1,
                    "automatic": True
                }
            ]
        }
    ]
}