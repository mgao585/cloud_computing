from flask import Flask, request 
import random
import json
import os
app = Flask(__name__)

@app.route('/meal_rec')
def meal_pick():
    meals = [
    {'Meal': 'Meal A',
     'Price': '$1'},
    {'Meal': 'Meal B',
     'Price': '$2'},
    {'Meal': 'Meal C',
     'Price': '$3'},
    {'Meal': 'Meal D',
     'Price': '$4'},
    {'Meal': 'Meal E',
     'Price': '$5'},
    {'Meal': 'Meal F',
     'Price': '$6'},
    {'Meal': 'Meal G',
     'Price': '$7'},
    {'Meal': 'Meal H',
     'Price': '$8'},
    {'Meal': 'Meal I',
     'Price': '$9'},
    {'Meal': 'Meal J',
     'Price': '$10'},]
    meal_picked = random.choice(meals)
    return json.dumps(meal_picked)

if __name__ == '__main__':
    app.run(host="0.0.0.0")