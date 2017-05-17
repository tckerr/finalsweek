# +- DISCIPLINE CARD BOILERPLATE -------+
__locals = locals()
ActorApi = __locals.get('ActorApi')
StudentApi = __locals.get('StudentApi')
SeatApi = __locals.get('SeatApi')
PromptApi = __locals.get('PromptApi')
export = __locals.get('export')
# +- END DISCIPLINE CARD BOILERPLATE -------+

sorted_by_popularity = list(sorted(ActorApi.get_actors(), key=lambda x: x.popularity))
lowest_popularity = sorted_by_popularity[0]
if lowest_popularity.id == ActorApi.get_requestor().id:
    empty_seats = SeatApi.get_empty_seats()
    results = {}

    for actor in sorted_by_popularity:
        student = actor.student
        eligible_seats = []
        if actor.trouble <= 0:
            continue
        elif actor.trouble == 1:
            eligible_seats = filter(lambda s: s.row == student.seat.row, empty_seats)
        elif actor.trouble == 2:
            eligible_seats = filter(lambda s: s.column == student.seat.column, empty_seats)
        elif actor.trouble >= 3:
            eligible_seats = empty_seats
        eligible_seats = list(filter(lambda s: s.id not in results.keys(), eligible_seats))
        if eligible_seats:
            selected_seat = PromptApi.prompt_seat_choice(eligible_seats, "Target Seat for Student {} ({})".format(student.name, student.id))
            results[selected_seat] = actor.student

    for student, seat in results.items():
        StudentApi.move_to_empty_seat(seat, student)
