from flask import Flask
import psycopg2
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

def get_db_conn():
    conn = psycopg2.connect(
        host="postgres",
        dbname="mydb",
        user="postgres",
        password="postgres"
    )
    return conn

@app.route("/")
def index():
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS msg (id SERIAL PRIMARY KEY, content TEXT);")
    cur.execute("INSERT INTO msg(content) VALUES('hello from gitops micro service') RETURNING id;")
    res = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return f"API返回成功，记录id:{res[0]}"

@app.route("/health")
def health():
    return "ok",200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
