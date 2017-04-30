from game.configuration.definitions import PhaseTypeName, StageTypeName, LogLevel, LogType


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    TRACE = '\033[38;5;243m'


logging = {
    "as_file":           True,
    "print_output":      True,
    "log_level":         LogLevel.Verbose,
    "disabled":          {
        LogType.NoOp
    },
    "log_type_prefixes": {
        LogType.IndexError:         "!!",
        LogType.Operational:        " $",
        LogType.TestRunner:         "#",
        LogType.GameLogic:          "++",
        LogType.Ai:                 ">>",
        LogType.DocumentConversion: "!!",
        LogType.General:            "",
        LogType.Gameflow:           "+-",
    },
    "log_type_colors":   {
        LogType.IndexError:         bcolors.FAIL,
        LogType.Operational:        bcolors.TRACE,
        LogType.TestRunner:         bcolors.BOLD,
        LogType.GameLogic:          "",
        LogType.Ai:                 bcolors.OKGREEN,
        LogType.DocumentConversion: bcolors.FAIL,
        LogType.General:            "",
        LogType.Gameflow:           bcolors.WARNING,
    }
}

generation = {
    "seed":   "fVTtJuAsDi5Ym2",
    "id_len": 16
}

base_settings = {
    "hand_size":                  6,
    "action_card_deck_size":      1000,
    "discipline_card_deck_size":  100,
    "afterschool_card_deck_size": 100,
    "seat_rows":                  5,
    "seat_columns":               4,
    "total_students":             16,
    "grades_per_row":             2,
    "trouble_per_row":            -1
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
        "phase_sets": 4,
        "phases":     [
            {
                "phase_type": PhaseTypeName.Accumulation,
                "turn_sets":  0,
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
