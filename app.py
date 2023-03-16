import base64
import datetime
from io import BytesIO
from flask import Flask, jsonify, request, render_template
from flask_mysqldb import MySQL
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('agg')

app = Flask(__name__)

# configure the database connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'products_db'

mysql = MySQL(app)

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

# create a dictionary to map product ID with sub-category ID
product_dict = {
    1: 4,
    2: 44,
    3: 24,
    4: 12,
    5: 27,
    6: 14,
    7: 9,
    8: 13,
    9: 28,
    10: 30
}

# create a dictionary to map sub-category ID with a list of interest points on each date
subcat_interest = {}
for subcat_id in subcat_dict:
    subcat_interest[subcat_id] = {}

# insert the given data into the database
@app.route('/insert-data', methods=['POST'])
def insert_data():
    data = request.json
    cursor = mysql.connection.cursor()
    for row in data:
        date = datetime.strptime(row['Date'], '%d/%m/%Y')
        product_id = row['Product_ID']
        subcat_id = product_dict[product_id]
        interest_point = row['Interest_Point']
        if date not in subcat_interest[subcat_id]:
            subcat_interest[subcat_id][date] = interest_point
        else:
            subcat_interest[subcat_id][date] += interest_point
        cursor.execute('INSERT INTO sub_category_interest (Subcategory_ID, Date, Interest_Point) VALUES (%s, %s, %s)', (subcat_id, date, interest_point))
        mysql.connection.commit()
    cursor.close()
    return jsonify({'message': 'Data inserted successfully.'})

# render the bar chart for sub-category interest points
@app.route('/subcat-interest-chart')
def subcat_interest_chart():
    fig, ax = plt.subplots()
    x_values = list(subcat_interest.keys())
    y_values = [sum(subcat_interest[subcat_id].values()) for subcat_id in x_values]
    ax.bar(x_values, y_values, color='b')
    ax.set_xticks(list(subcat_interest.keys()))
    ax.set_xticklabels([subcat_dict[subcat_id] for subcat_id in subcat_interest.keys()], rotation=90)
    ax.set_xlabel('Sub-Category')
    ax.set_ylabel('Total Interest Points')
    plt.tight_layout()
    chart_url = get_chart_url(fig)
    return render_template('subcat_interest_chart.html', chart_url=chart_url)

def get_chart_url(fig):
    buffer = BytesIO()
    fig.savefig(buffer, format='png')
    buffer.seek(0)
    chart_url = base64.b64encode(buffer.getvalue()).decode()
    return chart_url
