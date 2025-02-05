import gradio as gr
import processor
import tempfile
import os

def process_video(input_video, slow_factor=2):
    # Create temporary input file
    with tempfile.NamedTemporaryFile(suffix=".mp4", delete=False) as input_temp:
        # Read content from uploaded file path
        with open(input_video, "rb") as f:
            input_temp.write(f.read())
        input_path = input_temp.name
    
    output_path = os.path.join(tempfile.gettempdir(), "slowmo_output.mp4")
    
    try:
        # Process video
        result_path = processor.generate_slow_motion(input_path, output_path, slow_factor)
        
        # Return processed video
        return result_path
    except Exception as e:
        raise gr.Error(f"Error processing video: {str(e)}")
    finally:
        # Clean up temporary files
        if os.path.exists(input_path):
            os.remove(input_path)
        if os.path.exists(output_path):
            os.remove(output_path)

# Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# Slow Motion Video Generator")
    
    with gr.Row():
        with gr.Column():
            video_input = gr.File(label="Upload Video", type="filepath")
            slow_factor = gr.Slider(2, 8, value=2, step=1, label="Slow Motion Factor")
            submit_btn = gr.Button("Generate Slow Motion")
        
        with gr.Column():
            video_output = gr.Video(label="Processed Video")

    submit_btn.click(
        fn=process_video,
        inputs=[video_input, slow_factor],
        outputs=video_output,
    )

if __name__ == "__main__":
    demo.launch(share=True)  # Added share=True for public link