
gunicorn main:app -w 1 --log-finle -

# AND MAIN py is From you main.py file
# and app is from THIS app = Flask(__name__)

# AND NOW DEPLOY TO GLITCH USING GITHUB