
# 📝 Meeting Minutes Generator

The **Meeting Minutes Generator** is an intelligent documentation assistant that automatically transcribes meeting audio and generates **professional meeting minutes**.  
It combines **OpenAI’s Whisper API** for transcription 🎙️ and a **Llama-based summarization model** for crafting polished summaries.  

The generated minutes include:
- 📅 **Meeting summary** with attendees, location, and date  
- 🔍 **Discussion points** and **key takeaways**  
- ✅ **Action items** with assigned owners  
- 📄 **Downloadable PDF** report for easy sharing and record-keeping  

---

## 🚀 Features
- 🎧 Upload and transcribe any meeting audio file  
- 🤖 Automatically summarize discussions and extract key decisions  
- 📋 Generate structured and formatted meeting minutes  
- 💾 Download results as a clean, professional PDF  
- 🌐 Built with **Streamlit** for an easy-to-use web interface  

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/siddhynayak/Meeting-Documentation-Assistant.git
cd Meeting-Minutes-Generator
````

### 2️⃣ Install the dependencies

```bash
pip install -r requirements.txt
```

> ⚠️ Make sure you have Python 3.8 or above installed.

---

### 3️⃣ Add your API keys

Create a `.env` file in the project root directory and add:

```bash
GOOGLEGEMINI_API_KEY=your_openai_api_key
HF_TOKEN=your_huggingface_token
```

---

## ▶️ Run the Application

To start the Streamlit app, run:

```bash
streamlit run main.py
```

Then open the local URL displayed in your terminal (usually [http://localhost:8501](http://localhost:8501)).



---

## 📦 Dependencies

Key libraries used:

* `openai-whisper`
* `transformers`
* `streamlit`
* `reportlab`
* `python-dotenv`
* `pydub`
* `torch`

Install all using:

```bash
pip install -r requirements.txt
```

---

## 🧠 Model Details

* **Speech-to-Text**: [OpenAI Whisper](https://github.com/openai/whisper)
* **Summarization Model**: [Llama 3 / T5 / BART] (customizable via Hugging Face API)
* **Output Format**: PDF (via ReportLab)

---

## 📄 License

This project is licensed under the **MIT License** — free to use and modify.

---

## 💡 Example Output

**Generated Minutes Example (Markdown):**

```
### Meeting Summary
- **Date:** October 5, 2025
- **Attendees:** John, Sarah, Priya
- **Location:** Zoom

### Key Points Discussed
- Product roadmap updates
- Budget allocations for Q4
- Upcoming client deliverables

### Action Items
- John to finalize budget by Oct 10
- Priya to update roadmap slides
- Sarah to send client deliverable schedule
```



