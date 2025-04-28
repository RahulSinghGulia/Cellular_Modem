import gradio as gr

# Block descriptions
block_descriptions = {
    "Source": "Generates the original data (e.g., voice, text, video). Example: Microphone for voice calls.",
    "Encoder": "Converts data into transmittable format (e.g., digital bits). Example: PCM encoding for audio.",
    "Encryption": "Secures data using algorithms (e.g., AES). Prevents eavesdropping.",
    "Modulator": "Maps data to carrier signals (e.g., QAM for 5G). Adapts to channel properties.",
    "Channel": "Physical medium (e.g., fiber, radio waves). Introduces noise/interference.",
    "Demodulator": "Extracts data from carrier signals. Handles noise correction.",
    "Decoder": "Reverses encoding (e.g., PCM to audio). May include error correction.",
    "Destination": "Final output (e.g., speaker, screen). Completes the communication loop."
}

def block_clicked(block_name):
    desc = block_descriptions.get(block_name, "No description available.")
    return f"""
    <div style='background: #f8f9fa; padding: 20px; border-radius: 10px;'>
        <h2 style='color: #2c3e50;'>{block_name}</h2>
        <p style='font-size: 16px;'>{desc}</p>
    </div>
    """

# Define all blocks in transmission order
all_blocks = [
    "Source", "Encoder", "Encryption", "Modulator",
    "Channel",
    "Demodulator", "Decoder", "Destination"
]

# Updated color scheme with green channel
block_colors = [
    "#FF6B6B", "#FF8E8E", "#FFB3B3", "#FFD8D8",  # Transmitter
    "#4CAF50",                                   # Channel (green)
    "#74C0FC", "#8FD3FF", "#A5D8FF"              # Receiver
]

with gr.Blocks(title="Communication System Explorer", theme=gr.themes.Soft()) as demo:
    # Header
    gr.Markdown("""
    <h1 style='text-align: center; color: #2c3e50; margin-bottom: 10px;'>
        📡 Communication System: Transmission and Reception
    </h1>
    <p style='text-align: center; color: #7f8c8d; margin-bottom: 30px;'>
        Click any block to learn its role in the communication chain
    </p>
    """)

    # Output panel
    output_panel = gr.HTML(
        value="<div style='text-align: center; color: #7f8c8d; padding: 20px;'>Select a block to view details</div>",
        label="Block Details"
    )

    # Single row for all blocks with increased spacing
    with gr.Row(variant="panel"):
        for i, block in enumerate(all_blocks):
            # Add larger arrows between sections with more spacing
            if block == "Channel":
                gr.Markdown("""
                <div style='display: flex; align-items: center; padding: 0 25px; font-size: 28px; color: #666;'>
                    ➤
                </div>
                """)
            
            btn = gr.Button(
                block,
                elem_classes="block-btn",
                variant="primary",
                min_width=120
            )
            btn.click(
                block_clicked,
                inputs=gr.State(block),
                outputs=output_panel
            )
            
            # Add larger arrows between transmitter/receiver blocks with more spacing
            if block in ["Source", "Encoder", "Encryption"]:
                gr.Markdown("""
                <div style='display: flex; align-items: center; padding: 0 15px; font-size: 24px; color: #666;'>
                    ➤
                </div>
                """)
            
            if block in ["Demodulator", "Decoder"]:
                gr.Markdown("""
                <div style='display: flex; align-items: center; padding: 0 15px; font-size: 24px; color: #666;'>
                    ➤
                </div>
                """)

    # CSS for styling with increased spacing
    demo.css = """
    .block-btn {
        font-weight: bold;
        padding: 25px 20px;
        margin: 0 5px;
        border-radius: 8px;
        transition: all 0.3s;
        min-width: 120px;
        white-space: nowrap;
        font-size: 16px;
    }
    .block-btn:hover {
        transform: scale(1.05);
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    #component-0 {
        max-width: 1400px;
        margin: 0 auto;
        padding: 30px;
    }
    .gr-row {
        gap: 10px !important;
    }
    """

    # Apply colors to each block
    for i, color in enumerate(block_colors):
        demo.css += f"""
        button:nth-of-type({i+1}) {{
            background: {color};
            border: 2px solid {color};
        }}
        button:nth-of-type({i+1}):hover {{
            border-color: #2c3e50;
        }}
        """

demo.launch()