prize = [
    {
        'id': 1,
        'description': 'string'
    },
    {
        'id': 2,
        'description': 'string'
    }
]

participant = [
    {
        'id': 1,
        'name': 'string'
    },
    {
        'id': 2,
        'name': 'string'
    }
]

participants = [participant[0], participant[1]]

promo = [
    {
        'id': 1,
        'name': 'string',
        'description': 'string',
        'prizes': prize,
        'participants': participants
    },
    {
        'id': 2,
        'name': 'string',
        'description': 'string',
        'prizes': prize,
        'participants': participants
    }
]

result = [
    {
        'winner': participant,
        'prize': prize
    }
]
