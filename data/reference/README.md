# Reference Voice Audio

## Requirements for Reference Voice (ref_voice.wav)

To use this voice cloning system, you need to provide a reference voice audio file. Place your reference audio file in this directory as `ref_voice.wav`.

### Audio Requirements:
- **Format**: WAV file (recommended) or MP3
- **Duration**: 5-30 seconds for optimal results
- **Quality**: Clear, high-quality recording without background noise
- **Content**: Natural speech, preferably containing various phonemes
- **Channels**: Mono preferred (stereo will work but mono is better)
- **Sample Rate**: 22kHz or higher recommended

### Tips for Best Results:
1. Use a clean, noise-free recording environment
2. Record natural, conversational speech (not reading in a robotic manner)  
3. Include varied intonation and emotions in the sample
4. Avoid very short clips (under 5 seconds) or very long ones (over 30 seconds)
5. Ensure the speaker's voice is the only voice in the recording

### Ethical Considerations:
- **IMPORTANT**: Only clone voices with explicit consent from the speaker
- Respect privacy and intellectual property rights
- Use voice cloning technology responsibly and ethically
- Consider the potential implications of synthetic speech generation

### Example Usage:
Once you have placed your `ref_voice.wav` file in this directory, you can test the system with:

```bash
# JSON batch processing test
python voice_cloning_script.py \
  --speaker_wav data/reference/ref_voice.wav \
  --json data/inputs/sentences.json
```

**Note**: Without a reference voice file, the voice cloning script will not work. You must provide your own reference audio.