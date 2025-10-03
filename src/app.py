#!/usr/bin/env python3
"""
iot-device-app - Agrarian Application
"""

from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "name": "iot-device-app",
        "version": "1.0.0",
        "status": "running",
        "description": "Agrarian iot-device-app application"
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
