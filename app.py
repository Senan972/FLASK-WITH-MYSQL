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
}


@app.route('/')
def index():
    # query the database for interest points data
    cnx = mysql.connector.connect(**mysql_config)
    cursor = cnx.cursor()
    query = "SELECT subcat_id, date, interest_points FROM interest_points_table"
    cursor.execute(query)
    data = cursor.fetchall()
    cnx.close()

    # create a dictionary to store the interest points for each sub-category and date
    interest_points_dict = {}
    for subcat_id in subcat_dict:
        interest_points_dict[subcat_id] = {}
    
    # process the data and populate the interest_points_dict
    for row in data:
        subcat_id = row[0]
        date = row[1]
        interest_points = row[2]
        if date not in interest_points_dict[subcat_id]:
            interest_points_dict[subcat_id][date] = interest_points
        else:
            interest_points_dict[subcat_id][date] += interest_points
    
    # create a bar chart for each sub-category
    fig, axs = plt.subplots(len(subcat_dict), 1, figsize=(10, 20), sharex=True, sharey=True)
    plt.subplots_adjust(hspace=0.4)
    for i, subcat_id in enumerate(subcat_dict):
        if subcat_id in interest_points_dict:
            dates = sorted(interest_points_dict[subcat_id].keys())
            interest_points = [interest_points_dict[subcat_id][date] for date in dates]
            x_ticks = np.arange(len(dates))
            axs[i].bar(x_ticks, interest_points, align='center', alpha=0.5)
            axs[i].set_xticks(x_ticks)
            axs[i].set_xticklabels(dates)
            axs[i].set_ylabel('Interest Points')
            axs[i].set_title(subcat_dict[subcat_id])
    
    # save the chart image as a byte stream
    buf = BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    chart = base64.b64encode(buf.read()).decode('utf-8')
    plt.close(fig)
    
    return render_template('index.html', chart=chart)

if __name__ == '__main__':
    app.run(debug=True)
