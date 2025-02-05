import cv2
import numpy as np
from tqdm import tqdm

def generate_slow_motion(input_video_path, output_video_path, slow_factor=2):
    # Check CUDA availability
    cuda_available = cv2.cuda.getCudaEnabledDeviceCount() > 0
    use_cuda = False
    
    if cuda_available:
        try:
            # Try to initialize CUDA Farneback
            cuda_farneback = cv2.cuda.FarnebackOpticalFlow_create(
                numLevels=3, pyrScale=0.5, fastPyramids=False,
                winSize=15, numIters=3, polyN=5, polySigma=1.2, flags=0
            )
            use_cuda = True
        except AttributeError:
            print("CUDA optical flow not available - falling back to CPU")
            use_cuda = False

    cap = cv2.VideoCapture(input_video_path)
    if not cap.isOpened():
        raise ValueError("Could not open video file")

    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video_path, fourcc, fps // slow_factor, (width, height))

    ret, prev_frame = cap.read()
    if not ret:
        raise ValueError("Could not read video frames")

    # Initialize previous frame
    prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
    if use_cuda:
        prev_gpu = cv2.cuda_GpuMat()
        prev_gpu.upload(prev_gray)

    pbar = tqdm(total=total_frames-1, desc="Processing Frames", unit="frame")

    while True:
        ret, next_frame = cap.read()
        if not ret:
            break

        next_gray = cv2.cvtColor(next_frame, cv2.COLOR_BGR2GRAY)

        # Calculate optical flow
        if use_cuda:
            next_gpu = cv2.cuda_GpuMat()
            next_gpu.upload(next_gray)
            flow_gpu = cuda_farneback.calc(prev_gpu, next_gpu, None)
            flow = flow_gpu.download()
        else:
            flow = cv2.calcOpticalFlowFarneback(
                prev_gray, next_gray, None, 0.5, 3, 15, 3, 5, 1.2, 0
            )

        # Generate interpolated frames
        for i in range(1, slow_factor):
            alpha = i / slow_factor
            x_coords, y_coords = np.meshgrid(np.arange(width), np.arange(height), indexing='xy')
            
            map_x = (x_coords + flow[..., 0] * alpha).astype(np.float32)
            map_y = (y_coords + flow[..., 1] * alpha).astype(np.float32)
            
            interpolated_frame = cv2.remap(prev_frame, map_x, map_y, cv2.INTER_LINEAR)
            out.write(interpolated_frame)

        out.write(next_frame)
        
        # Update previous frame
        prev_gray = next_gray
        if use_cuda:
            prev_gpu.upload(next_gray)
        pbar.update(1)

    pbar.close()
    cap.release()
    out.release()
    return output_video_path