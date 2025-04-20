from flask import Flask, render_template_string, redirect
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def root():
    return redirect('/htop')

@app.route('/htop')
def htop():
    # Get system username
    username = os.getenv('USER', os.getenv('CODESPACE_NAME', 'unknown'))
    
    # Get full name (using system username as fallback)
    full_name = "Guneet Singh"  # Replace with your full name
    
    # Get server time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %z')
    
    # Get top output - adjusted for Linux environment in Codespace
    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1'], text=True)
    except subprocess.CalledProcessError as e:
        # Fallback for macOS if not in Codespace
        try:
            top_output = subprocess.check_output(['top', '-l', '1', '-n', '0'], text=True)
        except:
            top_output = f"Error fetching top data: {str(e)}"

    # HTML template
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>System Information</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 20px;
                line-height: 1.6;
                background-color: #f5f5f5;
            }
            .container {
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
                background-color: white;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            .info {
                margin-bottom: 20px;
                padding: 20px;
                background-color: #f8f9fa;
                border-radius: 4px;
            }
            .info p {
                margin: 10px 0;
            }
            pre {
                background-color: #2d2d2d;
                color: #ffffff;
                padding: 15px;
                border-radius: 5px;
                overflow-x: auto;
                font-family: 'Courier New', monospace;
            }
            h3 {
                color: #333;
                border-bottom: 2px solid #eee;
                padding-bottom: 10px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="info">
                <p><strong>Name:</strong> {{ full_name }}</p>
                <p><strong>Username:</strong> {{ username }}</p>
                <p><strong>Server Time (IST):</strong> {{ server_time }}</p>
            </div>
            <div class="top-output">
                <h3>TOP output:</h3>
                <pre>{{ top_output }}</pre>
            </div>
        </div>
    </body>
    </html>
    """
    
    return render_template_string(
        html_template,
        full_name=full_name,
        username=username,
        server_time=server_time,
        top_output=top_output
    )

if __name__ == '__main__':
    # Enable debug mode for development
    app.run(host='0.0.0.0', port=5000, debug=True) 