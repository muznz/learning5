from flask import Flask, render_template, request
from flask_s3 import FlaskS3

#if app.config["ENV"] == "production":
    #app.config.from_object("config.ProductionConfig")
#else:
    #app.config.from_object("config.DevelopmentConfig")

s3 = FlaskS3()

def start_app():
    app = Flask(__name__)
    app.config["ENV"] = "development"
    app.config.from_object("config.DevelopmentConfig")
    #following line would have been needed if wanting production configuration
    #app.config.from_object("ProductionConfig(Config)")
    s3.init_app(app)
    return app

app = start_app()

#Following lines not needed but have put in to help understand program
print(app.config["SECRET_KEY"])
print(app.config["ENV"])
print(app.config["FLASKS3_BUCKET_NAME"])
print(app.config["FLASKS3_BUCKET_DOMAIN"])
print(app.config["FLASKS3_REGION"])
print(app.config["FLASKS3_ACTIVE"])
print(app.config["FLASKS3_DEBUG"])


@app.route('/', methods=['GET', 'POST'])
def form():
    return render_template('form.html')

@app.route('/greeting', methods=['GET', 'POST'])
def greeting():
    return render_template('greeting.html', say='a', blah='var', to='b')

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    return render_template('greeting.html', say=request.form['say'], to=request.form['to'] )

if __name__ == "__main__":
    app.run()