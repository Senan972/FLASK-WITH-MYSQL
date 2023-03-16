from flask import Flask, render_template
import mysql.connector
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import os
from io import BytesIO
import base64

app = Flask(__name__)

# MySQL configuration
mysql_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'interest_points'
}

# create a dictionary to map sub-category ID with sub-category name
subcat_dict = {
1: 'Fishery',
    2: 'Meat',
    3: 'Medical Accessories',
    4: 'Fruits',
    5: 'Vegetables',
    6: 'Packed Fruits and Vegetables',
    7: 'Medical Consumables',
    8: 'Medical Ointments & Sprays',
    9: 'Chocolates',
    10: 'Biscuits',
    11: 'Croissant',
    12: 'Ice-Cream',
    13: 'Milk',
    14: 'Baby Diapers',
    15: 'Baby Milk Formula',
    16: 'Baby Feeding Accessories',
    17: 'Adult Pads',
    18: 'Sensual Care',
    19: 'Personal Care',
    20: 'Hygiene',
    21: 'Household Care',
    22: 'Fragrances',
    23: 'Perfumes',
    24: 'Air Fragrances',
    25: 'Surface Cleaners',
    26: 'Dish Washers',
    27: 'Laundry',
    28: 'Facial Care',
    29: 'Body Care',
    30: 'Oral Care',
    31: 'Baby Oral Care',
    32: 'Baby Body Care',
    33: 'Soap & Body Wash',
    34: 'Baby Bath supplies',
    35: 'Foodgrains',
    36: 'Rice',
    37: 'Pulses',
    38: 'Salt',
    39: 'Sugar',
    40: 'Chips and other snacks',
    41: 'Frozen Meat',
    42: 'Frozen Poultry',
    43: 'Fresh Poultry',
    44: 'Canned Poultry',
    45: 'Canned Meat',
    46: 'Canned Fish',
    47: 'Canned Fruits',
    48: 'Canned Veggies',
    49: 'Frozen Veggies',
    50: 'Frozen Fruits'
}

@app.route('/')
def index():
    plt.switch_backend('agg')

    # Query the database for interest points data
    cnx = mysql.connector.connect(**mysql_config)
    cursor = cnx.cursor()
    query = "SELECT subcat_id, date, interest_points FROM interest_points_table"
    cursor.execute(query)
    data = cursor.fetchall()
    cnx.close()

    # Create a dictionary to store the interest points for each sub-category and date
    interest_points_dict = {}
    for subcat_id in subcat_dict:
        interest_points_dict[subcat_id] = {}

    # Process the data and populate the interest_points_dict
    for row in data:
        subcat_id = row[0]
        date = row[1]
        interest_points = row[2]
        if date not in interest_points_dict[subcat_id]:
            interest_points_dict[subcat_id][date] = interest_points
        else:
            interest_points_dict[subcat_id][date] += interest_points

    # Create a bar chart for each sub-category
    figs = []
    charts = []
    for i, subcat_id in enumerate(subcat_dict):
        if subcat_id in interest_points_dict:
            dates = sorted(interest_points_dict[subcat_id].keys())
            interest_points = [interest_points_dict[subcat_id][date] for date in dates]
            x_ticks = np.arange(len(dates))

            fig, ax = plt.subplots(1, 1, figsize=(10, 6))
            ax.bar(x_ticks, interest_points, align='center', alpha=0.5)
            ax.set_xticks(x_ticks)
            ax.set_xticklabels(dates, rotation=90)
            ax.set_ylabel('Interest Points')
            ax.set_title(subcat_dict[subcat_id])

            # Save the chart image as a byte stream
            buf = BytesIO()
            fig.savefig(buf, format='png')
            buf.seek(0)
            chart = base64.b64encode(buf.read()).decode('utf-8')
            figs.append(chart)
            plt.close(fig)

            # Add the chart to the list of charts
            charts.append(chart)

    # Render the HTML page with all the charts
    return render_template('index.html', charts=charts, subcat_dict=subcat_dict)


if __name__ == '__main__':
    app.run(debug=True)
