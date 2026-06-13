from flask import Flask, jsonify, request
from prompt_generator import NeonGenerationPromptGenerator

app = Flask(__name__)
generator = NeonGenerationPromptGenerator()

@app.route('/api/generate-prompt', methods=['GET'])
def generate_prompt():
    prompt = generator.generate_prompt()
    return jsonify({
        "success": True,
        "prompt": prompt,
        "skill": "neon-generation-prompt",
        "version": "1.0.0"
    })

@app.route('/api/test', methods=['GET'])
def test():
    return jsonify({
        "success": True,
        "message": "Neon Generation Prompt API is working!"
    })

if __name__ == '__main__':
    print("Starting Neon Generation Prompt API...")
    app.run(port=5000, debug=True)
