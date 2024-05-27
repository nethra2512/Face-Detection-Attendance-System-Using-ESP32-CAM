
from flask import Flask
import subprocess

app = Flask(__name__)


@app.route('/')
def index():
    return '''
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Attendance Checker</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #aed9e0; /* Pastel blue background */
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            flex-direction: column;
            position: relative;
        }

        .animated-text {
            color: #333;
            font-size: 20px;
            text-align: center;
            animation: slide-in 2s ease infinite;
            position: absolute;
            top: 20px; /* Adjusted top position */
        }

        @keyframes slide-in {
            0% {
                transform: translateY(-50px);
                opacity: 0;
            }
            100% {
                transform: translateY(0);
                opacity: 1;
            }
        }

        #container {
            max-width: 800px;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
        }

        h1 {
            color: #333;
            margin-bottom: 20px;
            text-align: center;
        }

        button {
            background-color: #fff;
            border: 2px solid #333;
            border-radius: 5px;
            color: #333;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.3s, color 0.3s;
            margin-top: 20px;
        }

        button:hover {
            background-color: #333;
            color: #fff;
        }

        #csvData {
            margin-top: 20px;
            text-align: center;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            border-spacing: 0;
            margin-top: 20px;
            border: 2px solid #333; /* Dark grey border */
        }

        th, td {
            border: 1px solid #333; /* Dark grey border */
            padding: 10px;
        }

        th {
            background-color: #f2f2f2;
            color: #333;
            font-weight: bold;
        }
    </style>
    <script>
        function runScript() {
            fetch('/run-script').then(response => {
                if (!response.ok) {
                    throw new Error('Failed to run script');
                }
                return response.text();
            }).then(result => {
                console.log(result);
            }).catch(error => {
                console.error(error);
            });
        }
        function loadCSV() {
            // Redirect to the "attendance.html" page
            window.location.href = 'http://localhost:8000/attendance.html';
        }
    </script>
</head>
<body>
    <div class="animated-text">Check your attendance below</div>
    <div id="container">
        <h1>Attendance Checker</h1>
        <button onclick="runScript()">Take Attendance</button>
        <button onclick="loadCSV()">View Attendance</button>
        <div id="csvData"></div>
    </div>
    
</body>
</html>
    '''


@app.route('/run-script')
def run_script():
    result = subprocess.run(['python', 'det.py'], capture_output=True, text=True)
    return result.stdout

if __name__ == '__main__':
    app.run(debug=True)

