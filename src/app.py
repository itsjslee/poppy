from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/modify_url', methods=['POST'])
def modify_url():
    url = request.form['url']
    if "youtube.com" in url and not url.endswith('.'):
        url = url.replace("youtube.com", "youtube.com.")
    return redirect(url)

if __name__ == '__main__':
    app.run(debug=True)
