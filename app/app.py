from flask import Flask,jsonify,render_template_string
import os
import datetime


app = Flask(__name__)

##minimal HTML
HTML_INDEX = """
<!doctype html>
<html>
<head>
    <title>Simple Flask App</title>
</head>
<body>
    <h1>Devops Rules 4ever✅</h1>
    <p>Host: {{ host }}</p>
    <p>Time: {{ time }}</p> 
    <p> Adding ArgoCD Project By Almog</p>
    
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(
        HTML_INDEX,
        host=os.getenv("HOSTNAME" , "local"),
        time=datetime.datetime.now()
    
    )
@app.route("/health")
def health():
    return jsonify({
        "status":"ok",
        "service":"simple-flaskapp",
        "time": datetime.datetime.now().isoformat()
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000)