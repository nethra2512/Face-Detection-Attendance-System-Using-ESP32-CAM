# Face-Detection-Attendance-System-Using-ESP32-CAM



This project demonstrates how to set up an ESP32-CAM module as a web server for capturing images at different resolutions and performing face detection. The captured images can be accessed via HTTP requests, and the face detection script (`det.py`) marks attendance based on recognized faces.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Usage](#usage)
- [Endpoints](#endpoints)


## Introduction

The ESP32-CAM module is a versatile device that integrates a camera and Wi-Fi capabilities. In this project, we utilize the ESP32-CAM to create a web server capable of capturing images at different resolutions (low, medium, and high) and serving them over HTTP. Additionally, we implement face detection using OpenCV and mark attendance based on recognized faces.

## Prerequisites

To use this code, you will need:

- Arduino IDE installed on your computer.
- ESP32 board support installed in the Arduino IDE.
- Required libraries: `WebServer.h`, `WiFi.h`, `esp32cam.h`, `OpenCV`.
- Python environment with `OpenCV` installed.

## Setup

1. Connect your ESP32-CAM module to your computer via USB.
2. Open the `esp32cam_webserver.ino` file in Arduino IDE.
3. Configure the Wi-Fi SSID and password in the code.
4. Upload the code to your ESP32-CAM module.
5. Ensure that the `connect.py` and `det.py` files are placed in the same directory.

## Usage

### Arduino IDE Code

1. Power on the ESP32-CAM module.
2. Connect your computer or mobile device to the same Wi-Fi network as the ESP32-CAM.
3. Open a web browser and navigate to the IP address of the ESP32-CAM.
4. Access the provided endpoints to capture images at different resolutions.

### Python Scripts (connect.py and det.py)

1. Ensure that the ESP32-CAM module is powered on and connected to the Wi-Fi network.
2. Run the `connect.py` script to establish a connection with the ESP32-CAM module.
3. Run the `det.py` script to perform face detection and mark attendance based on recognized faces.

## Endpoints

- `/cam-lo.jpg`: Capture image at low resolution.
- `/cam-hi.jpg`: Capture image at high resolution.
- `/cam-mid.jpg`: Capture image at medium resolution.

