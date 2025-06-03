import json

class InferenceEngine:
    def __init__(self, knowledge_base_path):
        # Load the knowledge base from the JSON file
        with open(knowledge_base_path, 'r') as f:
            self.knowledge_base = json.load(f)

    def get_recommendation(self, occasion, weather):
        # Search the knowledge base for a matching rule
        for rule in self.knowledge_base:
            if rule["occasion"].lower() == occasion.lower() and rule["weather"].lower() == weather.lower():
                return rule["recommendation"], rule["explanation"]
        return ["No outfit available for the selected criteria"], "No matching rules found."
