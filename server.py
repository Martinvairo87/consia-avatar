from flask import Flask, request, send_file
import os
import uuid

app = Flask(__name__)

@app.route("/")
def health():
    return {"ok": True, "system": "CONSIA AVATAR ENGINE"}

@app.route("/avatar/talk", methods=["POST"])
def talk():
    data = request.json
    text = data.get("text", "Hola Martín, CONSIA activo")

    uid = str(uuid.uuid4())
    audio_path = f"temp/{uid}.wav"
    video_path = f"results/{uid}.mp4"

    # TEXT → VOZ (ElevenLabs)
    os.system(f"""
    curl -X POST "https://api.elevenlabs.io/v1/text-to-speech/YOUR_VOICE_ID" \
    -H "xi-api-key: YOUR_ELEVEN_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{{"text":"{text}","model_id":"eleven_multilingual_v2"}}' \
    --output {audio_path}
    """)

    # LIP SYNC (Wav2Lip)
    os.system(f"""
    python inference.py \
    --checkpoint_path wav2lip.pth \
    --face avatar.jpg \
    --audio {audio_path} \
    --outfile {video_path}
    """)

    return send_file(video_path, mimetype="video/mp4")

if __name__ == "__main__":
    os.makedirs("temp", exist_ok=True)
    os.makedirs("results", exist_ok=True)
    app.run(host="0.0.0.0", port=5000)
