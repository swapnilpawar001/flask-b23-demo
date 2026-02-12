from flask import Flask
import requests

application = Flask(__name__)
app = application

def get_instance_id():
    try:
        # IMDSv2: fetch token first
        tok = requests.put(
            "http://169.254.169.254/latest/api/token",
            headers={"X-aws-ec2-metadata-token-ttl-seconds": "21600"},
            timeout=2
        ).text
        return requests.get(
            "http://169.254.169.254/latest/meta-data/instance-id",
            headers={"X-aws-ec2-metadata-token": tok},
            timeout=2
        ).text
    except Exception:
        return "local"

@app.route("/")
def home():
    return f"<h1>Hello Batch 23 this is the demontsration of python deployment with flask service </h1><p>Instance: {get_instance_id()}</p>"

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=8080)