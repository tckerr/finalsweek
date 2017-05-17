# +- OPERATION_MODIFIER BOILERPLATE -------+
__locals = locals()
ActorApi = __locals.get('ActorApi')
StudentApi = __locals.get('StudentApi')
SeatApi = __locals.get('SeatApi')
operation = __locals.get('operation')
export = __locals.get('export')
# +- END OPERATION_MODIFIER BOILERPLATE -------+

operation.value += 1
export("operation", operation)
