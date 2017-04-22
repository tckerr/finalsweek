class PhaseTypeName:
    ChooseSeats = "Choose Seats"
    Accumulation = "Accumulation"
    Classtime = "Classtime"
    Dismissal = "Dismissal"
    AfterSchool = "After School"
    Score = "Score"


class CardTypeName:
    ActionCard = "Action Card"


default_game_definition = [
    {
        "stage_type": "GameStart",
        "phase_sets": 1,
        "phases":     [
            {
                "phase_type": PhaseTypeName.ChooseSeats,
                "turn_sets":  1,
                "automatic":  False
            }
        ]
    },
    {
        "stage_type": "Play",
        "phase_sets": 8,
        "phases":     [
            {
                "phase_type": PhaseTypeName.Accumulation,
                "turn_sets":  1,
                "automatic":  True
            },
            {
                "phase_type": PhaseTypeName.Classtime,
                "turn_sets":  2,
                "automatic":  False
            },
            {
                "phase_type": PhaseTypeName.Dismissal,
                "turn_sets":  1,
                "automatic":  False
            },
            {
                "phase_type": PhaseTypeName.AfterSchool,
                "turn_sets":  1,
                "automatic":  False
            }
        ]
    },
    {
        "stage_type": "Scoring",
        "phase_sets": 1,
        "phases":     [
            {
                "phase_type": PhaseTypeName.Score,
                "turn_sets":  1,
                "automatic":  True
            }
        ]
    }
]
