# -*- coding: utf-8 -*-
import os
import json
import logging

from flask import Flask
from flask import render_template

from settings import BASE_DIR, VOWELS, LOG_LEVEL


app = Flask(__name__)
logger = logging.getLogger(__name__)
logger.setLevel(LOG_LEVEL)


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/test1/")
def test1():
    """ Test 1

        1. If the state name begins with a vowel, print “Voo” after the state name.
        2. If the state name ends with a vowel, print “Doo” after the state name.
        3. If the state name begins and ends with a vowel, print “VooDoo”  BEFORE the state name.
    """
    states_data_file = os.path.join(BASE_DIR, 'data', 'states.json')
    result_1, result_2, result_3 = [], [], []
    with open(states_data_file, 'r') as f:
        states_json = json.loads(f.read())

        # part 1
        for st_key, st_value in states_json.items():
            logger.info("{} - {}".format(st_key, st_value))
            if st_value[0].lower() in VOWELS:
                result_1.append("{} <b>Voo</b>".format(st_value))

        # part 2
        for st_key, st_value in states_json.items():
            logger.info("{} - {}".format(st_key, st_value))
            if st_value[-1].lower() in VOWELS:
                result_2.append("{} <b>Doo</b>".format(st_value))

        # part 3
        for st_key, st_value in states_json.items():
            logger.info("{} - {}".format(st_key, st_value))
            if (st_value[0].lower() in VOWELS) and (st_value[-1].lower() in VOWELS):
                result_3.append("<b>VooDoo</b> {}".format(st_value))

    logger.info("Result 1: {}".format(result_1))
    logger.info("Result 2: {}".format(result_2))
    logger.info("Result 3: {}".format(result_3))

    return render_template('test1.html', result_1=result_1, result_2=result_2, result_3=result_3)


@app.route("/test2/")
def test2():
    """ Test 2

        1. If the number of vowels is greater than the number of consonants in the state name,
            print “Apple” after the state name.
        2. If the number of vowels is fewer than the number of consonants in the state name,
            print “Pie” after the state name.
        3. If the number of vowels is equal to the number of consonants in the state name,
            print “Apple Pie” BEFORE the state name.
        4. If the state name contains a space, print the state name and the word in ALL CAPS.
    """
    states_data_file = os.path.join(BASE_DIR, 'data', 'states.json')
    result = []
    with open(states_data_file, 'r') as f:
        states_json = json.loads(f.read())

        # part 1
        for st_key, st_value in states_json.items():
            vovs, cons = 0, 0
            for s in st_value:
                if s in VOWELS:
                    vovs += 1
                else:
                    cons += 1
            if vovs > cons:
                res = "{} <b>Apple</b>".format(st_value)
            elif vovs < cons:
                res = "{} <b>Pie</b>".format(st_value)
            elif vovs == cons:
                res = "<b>Apple Pie</b> {}".format(st_value)
            else:
                pass

            if ' ' in st_value:
                res = res.upper()
            result.append(res)

    print(result)
    return render_template('test2.html', result=result)


@app.route("/test3/")
def test3():
    """ Test 3
    There are 381 large cities in the USA: http://en.wikipedia.org/wiki/List_of_Metropolitan_Statistical_Areas

    Using live data from the web, create a web page that prints a list of the names of the five cities
    in the United States with the highest temperatures “right now”, along with each of the five cities’
    current temperature.

    Please include a button that will recalculate and update the results when clicked.
    """

    result = {}
    weather_data_file = os.path.join(BASE_DIR, 'data', 'weather.json')
    with open(weather_data_file, 'r') as f:
        result = json.loads(f.read())

    return render_template('test3.html', result=result)


if __name__ == "__main__":
    app.run(port=8000)
