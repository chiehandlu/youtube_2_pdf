import os
from download_video import download_video, generate_srt
from translate_srt import translate_srt_file
from video_to_images import video_to_images
from convert_png_to_pdf import convert_png_to_pdf

def process_youtube_url(url, progress_callback=None):
    try:
        # Download video
        if progress_callback:
            progress_callback(0.1, "Downloading video...")
        file_name = download_video(url)
        
        # Generate subtitles
        if progress_callback:
            progress_callback(0.3, "Generating subtitles...")
        generate_srt(file_name)
        
        # Translate subtitles
        if progress_callback:
            progress_callback(0.5, "Translating subtitles...")
        en_srt_name = file_name.replace("mp4", "srt")
        translate_srt_file(en_srt_name)
        
        # Convert video to images
        if progress_callback:
            progress_callback(0.7, "Converting video to images...")
        base_name = os.path.splitext(file_name)[0]
        video_to_images(file_name)
        
        # Convert images to PDF
        if progress_callback:
            progress_callback(0.9, "Generating PDF...")
        pdf_path = convert_png_to_pdf(base_name, base_name)
        
        if progress_callback:
            progress_callback(1.0, "Done!")
        
        return pdf_path
    
    except Exception as e:
        if progress_callback:
            progress_callback(1.0, f"Error: {str(e)}")
        return None
