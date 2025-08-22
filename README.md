# Voice Cloning TTS Project

A voice cloning system using Coqui TTS XTTS v2 for zero-shot voice cloning. This project processes JSON files with multilingual text entries to generate speech using a reference voice sample.

## Installation

1. **Create and activate virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux/macOS
   # .venv\\Scripts\\activate    # Windows
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify installation:**
   ```bash
   python -c "from TTS.api import TTS; print('Installation verified!')"
   ```

## Usage

### Prerequisites
- Provide a reference voice audio file as `data/reference/ref_voice.wav`
- See `data/reference/README.md` for audio requirements and ethical guidelines

### Command Line Interface

**View help:**
```bash
python voice_cloning_script.py --help
```

### JSON Batch Processing
Process multiple multilingual sentences from a JSON file:
```bash
python voice_cloning_script.py \
  --speaker-wav data/reference/ref_voice.wav \
  --json data/inputs/sentences.json \
  --out-dir outputs
```

**JSON Format:**
```json
[
  {"id": "utt1", "text": "Hello from the cloned voice.", "language": "en"},
  {"id": "utt2", "text": "Bonjour tout le monde !", "language": "fr"}
]
```

### Supported Languages

- English (`en`) - Default
- French (`fr`)
- Spanish (`es`) 
- German (`de`)
- Italian (`it`)
- Portuguese (`pt`)
- Polish (`pl`)
- Turkish (`tr`)
- Dutch (`nl`)
- Czech (`cs`)
- Arabic (`ar`)
- Chinese (`zh-cn`)
- Hungarian (`hu`)
- Korean (`ko`)
- Japanese (`ja`)
- Hindi (`hi`)

## Technical Details

- **Model**: `tts_models/multilingual/multi-dataset/xtts_v2`
- **Framework**: Coqui TTS with PyTorch CPU backend
- **Output Format**: 22kHz WAV files
- **Input Requirements**: 5-30 second reference audio samples

## Evaluation Criteria

When testing the generated voices, consider:

1. **Similarity**: How closely does the generated voice resemble the reference voice?
2. **Naturalness**: Does the speech sound natural without artifacts?
3. **Clarity**: How easily can listeners understand the synthesized speech?

## Best Practices

- Use clean, high-quality reference audio (5-30 seconds)
- Keep text sentences short to reduce artifacts  
- Test with different languages to explore multilingual capabilities
- Always use voice cloning ethically with proper consent

## Dependencies

- Python 3.9-3.12
- Coqui TTS (`coqui-tts`)
- PyTorch CPU (`torch==2.7.1+cpu`)
- TorchAudio
- Additional dependencies listed in `requirements.txt`

## Ethical Use

**Important**: This technology should only be used ethically:
- Obtain explicit consent before cloning someone's voice
- Respect privacy and intellectual property rights
- Consider potential misuse and societal implications
- Use responsibly for legitimate purposes only

## Troubleshooting

- Ensure reference voice file exists and is accessible
- Check that input CSV/JSON files are properly formatted
- Verify virtual environment is activated
- Check available disk space for output files
- For best results, use clear, noise-free reference audio

----

Note: The included `data/reference/ref_voice.wav` is sourced from President Ronald Reagan's "Address to the Nation on the [Soviet Attack on a Korean Airliner](https://en.wikipedia.org/wiki/Korean_Air_Lines_Flight_007)" (September 5, 1983). This file was taken from the website of the Scripps Library Multimedia Archive of the University of Virginia's Miller Center of Public Affairs. The Miller Center multimedia files are taken from the presidential libraries of the presidents they depict. The files are therefore within the public domain, both as works of US Government employees conducted during their work, and as a part of the National Archive.
