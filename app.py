import psutil
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory().percent
    Message = None
    if cpu_percent > 80 or memory_percent > 80:
        Message = "High CPU or Memory Utilization detected. Please scale up"
    return f"CPU Utilizatioin: {cpu_percent} and Memory Utilization: {memory_percent}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
