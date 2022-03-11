from flask import Flask, jsonify, request
from data import promo, prize, participant, result

app = Flask(__name__)


@app.route('/promo', methods=['GET', 'POST'])
def promo_f():
    if request.method == 'GET':
        return jsonify(promo)
    elif request.method == 'POST':
        new_promo = request.json
        if new_promo['name'] is None:
            return 'please add name'
        else:
            new_id = int(promo[-1]["id"] + 1)
            new_promo["id"] = new_id
            promo.append(new_promo)
            return str(new_id)


@app.route('/promo/<int:promo_id>', methods=['GET', 'PUT', 'DELETE'])
def promo_id_f(promo_id):
    if request.method == 'GET':
        try:
            answer = jsonify(next(x for x in promo if x['id'] == promo_id))
            return answer
        except:
            return 'promo is empty'

    elif request.method == 'PUT':
        put_promo = request.json

        edit_promo = next(x for x in promo if x['id'] == promo_id)
        edit_promo['name'] = put_promo['name']
        edit_promo['description'] = put_promo['description']

        if put_promo['name'] is None or put_promo['name'] == ' ':
            return 'name is empty'
        else:
            promo.remove(next(x for x in promo if x['id'] == promo_id))
            promo.append(edit_promo)
            return "200 OK"
    elif request.method == 'DELETE':
        promo.remove(next(x for x in promo if x['id'] == promo_id))
        return "200 OK"


# /promo/{id}/participant
@app.route('/promo/<int:promo_id>/participant', methods=['POST'])
def add_participant(promo_id):
    new_part = request.json
    new_id = int(promo["id" == promo_id]["participants"][-1]["id"] + 1)
    new_part["id"] = new_id
    promo['id' == promo_id]['participants'].append(new_part)
    return str(new_id)


# /promo/{promoId}/participant/{participantId}
@app.route('/promo/<int:promo_id>/participant/<int:part_id>', methods=['DELETE'])
def del_part(promo_id, part_id):
    result_promo = next(x for x in promo if x['id'] == promo_id)
    result_promo = result_promo['participants']
    result_promo.remove(next(x for x in result_promo if x['id'] == part_id))
    promo['id' == promo_id].pop('participants')
    promo['id' == promo_id]['participants'] = result_promo
    return "200 OK"


# /promo/{id}/prize
@app.route('/promo/<int:promo_id>/prize', methods=['POST'])
def post_prize(promo_id):
    new_prize = request.json
    new_prize_id = int(promo["id" == promo_id]["prizes"][-1]["id"] + 1)
    new_prize["id"] = new_prize_id
    promo['id' == promo_id]['prizes'].append(new_prize)
    return str(new_prize_id)


# /promo/{promoId}/prize/{prizeId}
@app.route('/promo/<int:promo_id>/prize/<int:prize_id>', methods=['DELETE'])
def del_prize(promo_id, prize_id):
    result_promo = next(x for x in promo if x['id'] == promo_id)
    result_promo = result_promo['prizes']
    result_promo.remove(next(x for x in result_promo if x['id'] == prize_id))
    promo['id' == promo_id].pop('prizes')
    promo['id' == promo_id]['prizes'] = result_promo
    return "200 OK"


# /promo/{id}/raffle
@app.route('/promo/<int:promo_id>/raffle', methods=['POST'])
def raffle(promo_id):
    result_promo = next(x for x in promo if x['id'] == promo_id)
    if len(result_promo['participants']) == len(result_promo['prizes']):
        winners = result_promo['participants']
        prizes_list = result_promo['prizes']
        result = []
        for i in range(len(result_promo['participants'])):
            new_dict = dict(winner=winners[i], prize=prizes_list[i])
            result.append(new_dict)
        return jsonify(result)
    else:
        return "Conflict", 409


if __name__ == '__main__':
    app.run()
