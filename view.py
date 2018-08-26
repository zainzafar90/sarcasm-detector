from flask import render_template
from flask import jsonify
from flask import request

import app
import sarcasm
# import api.sentiment


# VIEWS


def index():
    return render_template('index.html')


def by_query_sarcasm():
    query = request.args.get('query')
    sarcasmScore = sarcasm.SarcasmDetector().getSarcasmScore(query)

    return render_template(
        'query.html',
        sarcasmScore=sarcasmScore
    )
