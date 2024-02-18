from flask import Flask, render_template

app = Flask(__name__)

# / will render a template that displays "INDEX" in h1 tags
@app.route('/')
def index():
    return render_template('index.html', content="INDEX")

# /display-name will render a template that displays my name in h1 tags
@app.route('/display-name')
def display_name():
    return render_template('name.html', content='Kathy Bailey Hines')

# /display-food ill render a template that displays my favorite food & image in h1 tags 
@app.route('/display-food')
def display_food():
    return render_template('food.html', content='Favorite Food: Paella', image_path='/static/paella.jpg')

# /display-vacation will render a template that displays my favorite vacation destination & image in h1 tags including an image of that destination.
@app.route('/display-vacation')
def display_vacation():
    return render_template('vacation.html', content='Favorite Vacation Destination: Ocean', image_path='/static/wave.jpg')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
