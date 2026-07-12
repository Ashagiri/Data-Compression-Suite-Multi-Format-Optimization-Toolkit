import streamlit as st
import io
import os

# Try to import from core, add fallback handling to prevent execution crashes
try:
    from core.huffman_engine import (
        build_frequency_table, 
        build_huffman_tree, 
        build_codes, 
        compress_text, 
        pad_encoded_text, 
        get_byte_array
    )
    from core.image_engine import compress_image
    from core.pdf_engine import compress_pdf
except ModuleNotFoundError:
    st.error("🚨 Configuration Error: Could not find the 'core' folder or engine scripts. Please verify your file structure.")

# Page Configuration
st.set_page_config(
    page_title="Data Compression Suite", 
    page_icon="🗜️", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling for Academic Polish
st.markdown("""
    <style>
    .main-title { font-size: 2.6rem; font-weight: 700; color: #1E3A8A; margin-bottom: 0.2rem; }
    .sub-title { font-size: 1.1rem; color: #4B5563; margin-bottom: 2rem; }
    .metric-card { background-color: #F3F4F6; padding: 1rem; border-radius: 0.5rem; border-left: 5px solid #3B82F6; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🗜️ Data Compression & Optimization Suite</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">An interactive framework analyzing bandwidth reduction paradigms across text, multimedia, and application containers.</div>', unsafe_allow_html=True)

# Main UI Tabs
tab1, tab2, tab3 = st.tabs(["🔤 Text (Huffman Coding)", "🖼️ Image (Quantization Passes)", "📄 PDF (Stream Deflation)"])

# ==========================================
# --- TAB 1: TEXT COMPRESSION (HUFFMAN) ---
# ==========================================
with tab1:
    st.header("Custom Huffman Serialization Engine")
    st.info("💡 **Theory:** This section processes discrete alphabets losslessly. By calculating relative character frequencies, frequent symbols receive shorter bitwise pathways than rare characters.")
    
    default_text = "Data communication forms the structural backbone of distributed modern networks."
    user_text = st.text_area("Input Stream for Bitwise Serialization:", value=default_text, height=120)
    
    if st.button("Execute Huffman Pipelines", type="primary", key="btn_text"):
        if not user_text:
            st.warning("Please input text to compress.")
        else:
            try:
                # Execution
                freq = build_frequency_table(user_text)
                root = build_huffman_tree(freq)
                codes = build_codes(root)
                encoded = compress_text(user_text, codes)
                padded = pad_encoded_text(encoded)
                bin_data = bytes(get_byte_array(padded))
                
                # Math calculations
                orig_bits = len(user_text) * 8
                comp_bits = len(encoded)
                efficiency = 100 - (comp_bits / orig_bits * 100)
                
                # Layout metrics
                st.subheader("⚡ Data Engineering Metrics")
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Uncompressed Base Stream", f"{orig_bits} bits")
                with col2:
                    st.metric("Padded Binary Payload", f"{comp_bits} bits")
                with col3:
                    st.metric("Bandwidth Optimization", f"{efficiency:.2f}% Saved")
                
                # Download and Charts
                st.write("---")
                col_left, col_right = st.columns([1, 2])
                with col_left:
                    st.success("Bitstream compiled successfully!")
                    st.download_button(
                        label="💾 Download Compressed (.bin)",
                        data=bin_data,
                        file_name="serialized_payload.bin",
                        mime="application/octet-stream"
                    )
                with col_right:
                    st.write("**Entropy Distribution Map (Character Frequencies)**")
                    st.bar_chart(freq)
            except NameError:
                st.error("Engine failure: Check that huffman_engine.py is completed and saved.")

# ==========================================
# --- TAB 2: IMAGE COMPRESSION (LOSSY) ---
# ==========================================
with tab2:
    st.header("Adaptive Quantization Framework")
    st.info("💡 **Theory:** Implements lossy visual optimizations. The framework isolates frequency coefficients and performs visual pruning alongside native Huffman serialization passes.")
    
    uploaded_img = st.file_uploader("Source Image Matrix Upload:", type=["png", "jpg", "jpeg"])
    quality = st.slider("Quantization Matrix Quality Scale (Lower = More Aggressive Compression)", 10, 100, 70)
    
    if uploaded_img:
        if st.button("Optimize Matrix Streams", type="primary", key="btn_img"):
            try:
                img_bytes = uploaded_img.read()
                compressed_bytes = compress_image(img_bytes, quality)
                
                orig_kb = len(img_bytes) / 1024
                comp_kb = len(compressed_bytes) / 1024
                savings = 100 - (comp_kb / orig_kb * 100)
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Raw Raster Allocation", f"{orig_kb:.2f} KB")
                with col2:
                    st.metric("Quantized Payload Size", f"{comp_kb:.2f} KB")
                with col3:
                    st.metric("Storage Volume Reductions", f"{savings:.2f}% Saved")
                
                st.write("---")
                st.download_button(
                    label="💾 Download Optimized Image (.jpg)",
                    data=compressed_bytes,
                    file_name="quantized_output.jpg",
                    mime="image/jpeg"
                )
            except NameError:
                st.error("Engine failure: Check that image_engine.py is completed and saved.")

# ==========================================
# --- TAB 3: PDF STREAM DEFLATION ---
# ==========================================
with tab3:
    st.header("Application Layer Deflate Optimization")
    st.info("💡 **Theory:** Performs structural parsing on vector containers. It losslessly strips duplicate metadata and shrinks structural objects using deflate routines.")
    
    uploaded_pdf = st.file_uploader("Document Stream Upload:", type=["pdf"])
    
    if uploaded_pdf:
        if st.button("Compress Container Components", type="primary", key="btn_pdf"):
            try:
                pdf_bytes = uploaded_pdf.read()
                compressed_pdf_bytes = compress_pdf(pdf_bytes)
                
                orig_kb = len(pdf_bytes) / 1024
                comp_kb = len(compressed_pdf_bytes) / 1024
                savings = 100 - (comp_kb / orig_kb * 100)
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Raw PDF Allocation", f"{orig_kb:.2f} KB")
                with col2:
                    st.metric("Deflated Stream Size", f"{comp_kb:.2f} KB")
                with col3:
                    st.metric("Transmission Economy", f"{savings:.2f}% Saved")
                
                st.write("---")
                st.download_button(
                    label="💾 Download Optimized Document (.pdf)",
                    data=compressed_pdf_bytes,
                    file_name="deflated_output.pdf",
                    mime="application/pdf"
                )
            except NameError:
                st.error("Engine failure: Check that pdf_engine.py is completed and saved.")