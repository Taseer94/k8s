from flask import Flask
import psycopg2

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/connect')
def connect():
    try:
        connection = psycopg2.connect(user = "admin",
                                    password = "admin123",
                                    host = "db",
                                    port = "5432",
                                    database = "postgresdb")
    except (Exception, psycopg2.Error) as error:
        return error
    finally:
        return "Congrats! Connection was successfull"   


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')