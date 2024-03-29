import csv
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')

@app.route('/api/mydata', methods=['GET'])
def api_mydata():
    data = get_data()
    return jsonify(data)


@app.route('/city/<name>')
def city(name):
    # with open('/Users/wyc/Desktop/assignment1-1/static/us-cities.csv', 'r') as f:
    with open('static/us-cities.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['city'] == name:
                return render_template('city.html', **row)
        return "City not found", 404

def get_data():
    data = []
    # 替换为你的CSV文件路径
    # with open('/Users/wyc/Desktop/assignment1-1/static/amazon-reviews.csv', 'r') as f:
    with open('static/amazon-reviews.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data




if __name__ == '__main__':
    app.run()
