# main.py

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def getData(url):
    key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImM0NGYxYWZkLThkNjItNDg1NC1hNjNjLTE1NTgwM2Q4M2U3NCIsImlhdCI6MTcwMzk3Mzk1NCwic3ViIjoiZGV2ZWxvcGVyL2I1ZTQzNTRiLWU2OWEtMTI3Ny05NGI3LWI2YTYyMzA3ODA2MCIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjE1Ny40NS4xODMuMjAyIiwiMTguMjE1LjE0My4yNDgiXSwidHlwZSI6ImNsaWVudCJ9XX0.mDB-_Kb7vSoBLF-ANNmwoBs02qyUYs751ZTJgKyKR2TSQD71T9v0XWCGwr2pUvCSXmaIItl5edmEQxBJGPYxBw"  # Replace with your Clash of Clans API key
    headers = {
        "Accept": "application/json",
        "authorization": f"Bearer {key}"
    }
    response = requests.get(url, headers=headers)
    return response.json()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/clan", methods=["POST"])
def clan():
    try:
        tag = request.form["clan_tag"]
        url = f"https://api.clashofclans.com/v1/clans/{tag}?members=1"  # Include at least one filtering parameter
        jsonData = getData(url)
        return render_template("clan.html", clan_info=jsonData)
    except Exception as e:
        return f"An error occurred: {str(e)}"
                                     
