from flask import Flask, render_template, request, jsonify
from weather import main as get_weather

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        city = request.form['cityName']
        state = request.form['stateName']
        country = request.form['countryName']
        weather_data = get_weather(city, state, country)
        return render_template('index.html', weather_data = weather_data)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
