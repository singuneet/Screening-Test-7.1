from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    print("Route /htop accessed")  # Debug statement
    # Full name
    full_name = "Your Full Name"  # Replace with your actual full name
    # System username
    username = os.getlogin()
    # Server time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S IST')
    # Top output
    top_output = subprocess.getoutput('top -b -n 1')
    return f"""
    <h1>System Information</h1>
    <p><b>Name:</b> {full_name}</p>
    <p><b>Username:</b> {username}</p>
    <p><b>Server Time (IST):</b> {server_time}</p>
    <pre><b>Top Output:</b>\n{top_output}</pre>
    """

if __name__ == '__main__':
    print("Starting Flask server on port 5000")
    app.run(host='0.0.0.0', port=5000, debug=True)