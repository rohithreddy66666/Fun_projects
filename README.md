# YouTube Video Summarizer

This Streamlit app allows you to summarize the transcript of a YouTube video using AI models. It utilizes Pytube to retreive the audio file and  Whisper for audio transcription and Transformers library for text summarization.

## Usage

1. Enter the URL of the YouTube video in the provided text input box.
2. Click on the "Generate Transcript" button to download the audio from the video and transcribe it.
3. Once the transcription is generated, you can click on the "Generate Summary" button to create a summary of the transcription.
4. The summarized text will be displayed in the app.

## Prerequisites

- Python 3.x
- Streamlit
- PyTube
- OpenAI Whisper
- Transformers

## Setup

1. Install the required dependencies using the following commands:

```bash
pip install pyngrok streamlit pytube openai-whisper transformers

## Ngrok Setup
ngrok authtoken your_ngrok_token

## Running the app
Run the Streamlit app

![Screenshot (343)](https://github.com/rohithreddy66666/Fun_projects/assets/29374423/65d0d7f8-6c41-4f30-82e8-aa5d89d6d17c)

