from flask import Flask, render_template, request
from stories import story

app = Flask(__name__)

@app.route('/')
def home():
    """Show the form to fill in words for the story."""
    return render_template('form.html', prompts=story.prompts)

@app.route('/story')
def show_story():
    """Show the generated story."""
    answers = {prompt: request.args[prompt] for prompt in story.prompts}
    text = story.generate(answers)
    return render_template('story.html', text=text)

if __name__ == "__main__":
    app.run(debug=True)
