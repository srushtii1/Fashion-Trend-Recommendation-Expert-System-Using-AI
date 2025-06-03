from flask import Flask, request, render_template
from inference_engine import InferenceEngine

app = Flask(__name__)

# Initialize the inference engine with the path to the knowledge base
engine = InferenceEngine("knowledge_base.json")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    occasion = request.form['occasion']
    weather = request.form['weather']
    print(f"Debug: Received inputs - Occasion: {occasion}, Weather: {weather}")  # Debugging line
    recommendation, explanation = engine.get_recommendation(occasion, weather)
    return render_template('result.html', recommendation=recommendation, explanation=explanation)

if __name__ == "__main__":
    app.run(debug=True)
