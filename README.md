# HandyPointer

A computer vision application that enables control of the mouse cursor and basic interactions (clicking, scrolling) through hand gestures captured via webcam.

## Features

- **Cursor Control**: Move your index finger to control the mouse pointer
- **Click Detection**: Bring your index finger and thumb together to perform a click
- **Scroll Functionality**: Hold your index and middle fingers together and move up/down to scroll
- **Smooth Movement**: Implements cursor smoothing for more precise control
- **Real-time Visualization**: See hand landmark tracking directly in the application window

## Requirements

- Python 3.8+
- Webcam
- Libraries:
  - opencv-python
  - mediapipe
  - pyautogui
  - numpy

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/aayushker/HandyPointer.git
   cd HandyPointer
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   python main.py
   ```

2. Position your hand in front of the webcam
3. Control the cursor with the following gestures:
   - Move your index finger to control the cursor position
   - Bring your index finger and thumb close together to click
   - Hold your index and middle fingers together and move up/down to scroll
4. Press 'Esc' to exit the application

## How It Works

HandyPointer uses MediaPipe's hand tracking solution to detect hand landmarks in real-time. The application tracks specific landmarks on your hand:
- Landmark 8 (index fingertip) for cursor positioning
- Landmarks 4 (thumb tip) and 8 (index fingertip) for click detection
- Landmarks 8 (index fingertip) and 12 (middle fingertip) for scroll detection

## Customization

You can adjust various parameters in [main.py](main.py) to fine-tune the application:
- `smooth_factor`: Higher values create smoother but slower cursor movement
- `click_threshold`: Adjust the distance threshold for click detection
- `scroll_threshold`: Change sensitivity of scrolling

