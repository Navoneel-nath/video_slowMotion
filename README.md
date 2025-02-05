# video_slowMotion

A slow motion video generator that creates smooth slow-motion effects by leveraging optical flow interpolation. This Python tool uses OpenCV for video processing and Gradio for an interactive web interface, with optional CUDA acceleration for enhanced performance.

## Features

- **Optical Flow Interpolation:** Uses Farneback optical flow to generate intermediate frames for smooth slow motion.
- **CUDA Acceleration:** Automatically detects and utilizes CUDA if available, speeding up the optical flow computation.
- **Interactive Interface:** A simple Gradio web interface to easily upload and process videos.
- **Progress Indicator:** Displays a live progress bar during video processing using tqdm.

## Requirements

- Python 3.7 or later
- [OpenCV](https://opencv.org/) (both `opencv-python` and `opencv-contrib-python`)
- [NumPy](https://numpy.org/)
- [Gradio](https://gradio.app/)
- [tqdm](https://github.com/tqdm/tqdm)

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/video_slowMotion.git
   cd video_slowMotion


txt
Copy
Edit
opencv-python
opencv-contrib-python
numpy
gradio
tqdm
Usage
Run the Application:

bash
Copy
Edit
python app.py
Interact via Browser:

Once the script is running, open the provided URL in your browser. Upload your video, adjust the slow motion factor (e.g., 2 for inserting one interpolated frame between each original frame), and click the button to generate your slow motion video.

Project Structure
processor.py: Contains the function to generate slow motion videos using optical flow.
app.py: Sets up the Gradio interface and integrates the video processing function.
Contributing
Contributions are welcome! Please feel free to open issues or submit pull requests if you have any suggestions or improvements.

License
This project is licensed under the MIT License.
