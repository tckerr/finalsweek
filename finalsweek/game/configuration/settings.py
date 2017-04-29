from game.configuration.definitions import PhaseTypeName, StageTypeName, LogLevel, LogType

logging = {
    "as_file": True,
    "print_output": True,
    "log_level": LogLevel.Verbose,
    "disabled": {
        LogType.NoOp,
        LogType.DocumentConversion
    }
}

generation = {
    "seed":   "fVTtJui5Ym",
    "id_len": 16
}

base_settings = {
    "hand_size":      6,
    "total_cards":    1000,
    "seat_rows":      5,
    "seat_columns":   4,
    "total_students": 16
}

default_game_definition = [
    {
        "stage_type": StageTypeName.GameStart,
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
        "stage_type": StageTypeName.Play,
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
        "stage_type": StageTypeName.Scoring,
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

