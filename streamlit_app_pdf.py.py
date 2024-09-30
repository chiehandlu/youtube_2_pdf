import streamlit as st
import you_dt
import os

def main():
    st.title("YouTube Video to PDF Converter")

    # YouTube URL input
    youtube_url = st.text_input("Enter YouTube URL")

    if st.button("Convert"):
        if youtube_url:
            progress_bar = st.progress(0)
            status_text = st.empty()

            def update_progress(progress, status):
                progress_bar.progress(progress)
                status_text.text(status)

            pdf_path = you_dt.process_youtube_url(youtube_url, update_progress)
            
            if pdf_path and os.path.exists(pdf_path):
                st.success("Conversion complete!")
                with open(pdf_path, "rb") as pdf_file:
                    pdf_bytes = pdf_file.read()
                st.download_button(
                    label="Download PDF",
                    data=pdf_bytes,
                    file_name="youtube_video.pdf",
                    mime="application/pdf"
                )
                # Clean up: remove the PDF file after offering download
                os.remove(pdf_path)
            else:
                st.error("An error occurred during conversion.")
        else:
            st.error("Please enter a YouTube URL")

if __name__ == "__main__":
    main()
