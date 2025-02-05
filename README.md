video_slowMotion
A slow motion video generator that uses optical flow interpolation to create smooth slow-motion effects in videos. The application leverages OpenCV for video processing and Gradio to provide an interactive web interface.

Features
Optical Flow Interpolation: Generate intermediate frames using Farneback optical flow.
CUDA Acceleration: Automatically detects and uses CUDA for faster processing if available.
User-Friendly Interface: Simple Gradio web interface for video upload and slow-motion generation.
Progress Tracking: Uses tqdm to display a processing progress bar.
Requirements
Python 3.7+
OpenCV (both opencv-python and opencv-contrib-python)
NumPy
Gradio
tqdm
Installation
Clone the Repository:

bash
Copy
Edit
git clone https://github.com/yourusername/video_slowMotion.git
cd video_slowMotion
Install Dependencies:

It is recommended to use a virtual environment. Then run:

bash
Copy
Edit
pip install -r requirements.txt
Example requirements.txt content:

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
