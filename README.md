# YouTube到PDF轉換器

這個Streamlit網頁應用程式允許用戶將YouTube視頻轉換為PDF文檔。應用程式會下載視頻、生成字幕、翻譯字幕、將視頻轉換為圖片，最後將這些圖片編譯成PDF。

## 功能特點

- 簡單的網頁界面，用於輸入YouTube URL
- 進度條顯示轉換狀態
- 自動下載轉換後的PDF

## 安裝

1. 克隆此倉庫：
   ```
   git clone https://github.com/yourusername/youtube-to-pdf-converter.git
   cd youtube-to-pdf-converter
   ```

2. 安裝所需的依賴：
   ```
   pip install -r requirements.txt
   ```

## 使用方法

1. 運行Streamlit應用：
   ```
   streamlit run streamlit_app_pdf.py
   ```

2. 打開瀏覽器，訪問終端中顯示的URL（通常是 `http://localhost:8501`）。

3. 在輸入框中輸入YouTube URL。

4. 點擊"轉換"按鈕。

5. 等待轉換過程完成。你可以通過進度條監控進度。

6. 轉換完成後，點擊"下載PDF"按鈕來保存生成的PDF。

## 系統要求

- Python 3.7+
- Streamlit
- yt-dlp
- moviepy
- Pillow
- pysrt
- requests
- whisper-ctranslate2
- tqdm

## 文件結構

- `streamlit_app_pdf.py`: 主要的Streamlit應用
- `you_dt.py`: 核心處理邏輯
- `download_video.py`: 下載YouTube視頻的功能
- `video_to_images.py`: 將視頻轉換為圖片的功能
- `convert_png_to_pdf.py`: 將圖片轉換為PDF的功能
- `translate_srt.py`: 翻譯字幕的功能

## 注意事項

本應用程式僅用於教育目的。使用此工具時，請尊重YouTube的服務條款和版權法。

## 貢獻

本項目是基於 [xdite/Video2PDF](https://github.com/xdite/Video2PDF.git) 的工作進行的。我們感謝原作者 xdite 的貢獻和創意。

歡迎提出問題、建議和功能請求。如果你想貢獻代碼，請查看 [issues 頁面](https://github.com/yourusername/youtube-to-pdf-converter/issues)。

## 授權

本項目採用 [MIT](https://choosealicense.com/licenses/mit/) 授權。