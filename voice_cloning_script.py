#!/usr/bin/env python3

import argparse
import json
import sys
from pathlib import Path
from TTS.api import TTS

MODEL = "tts_models/multilingual/multi-dataset/xtts_v2"

def load_rows_from_json(json_path, default_language):
    """Load text rows from JSON file with id, text, and optional language fields."""
    rows = []
    try:
        data = json.loads(Path(json_path).read_text(encoding="utf-8"))
        for i, row in enumerate(data):
            row_id = row.get("id") or f"utt_{i+1}"
            text = (row.get("text") or "").strip()
            language = row.get("language") or default_language or "en"
            if text:
                rows.append({"id": row_id, "text": text, "language": language})
    except FileNotFoundError:
        print(f"Error: JSON file '{json_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        sys.exit(1)
    return rows

def main():
    parser = argparse.ArgumentParser(
        description="Voice cloning TTS using Coqui TTS XTTS v2 - JSON batch processing",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Example:
  JSON batch processing:
    python voice_cloning_script.py --speaker-wav data/reference/ref_voice.wav --json data/inputs/sentences.json
        """
    )
    
    parser.add_argument(
        "--speaker-wav", 
        required=True, 
        help="Path to reference voice audio file (.wav format recommended)"
    )
    parser.add_argument(
        "--json", 
        required=True,
        help="Path to JSON file with array of objects containing id, text, and optional language fields"
    )
    parser.add_argument(
        "--out-dir", 
        default="outputs", 
        help="Output directory for generated audio files (default: outputs)"
    )
    parser.add_argument(
        "--language", 
        default="en", 
        help="Default language code (default: en). Supported: en, fr, es, de, it, pt, pl, tr, nl, cs, ar, zh-cn, hu, ko, ja, hi"
    )
    
    args = parser.parse_args()
    
    # Validate JSON file argument
    if not args.json:
        parser.error("--json parameter is required")
    
    # Check if speaker wav file exists
    if not Path(getattr(args, 'speaker_wav') or getattr(args, 'speaker-wav')).exists():
        print(f"Error: Reference voice file '{getattr(args, 'speaker_wav') or getattr(args, 'speaker-wav')}' not found.")
        sys.exit(1)
    
    # Initialize TTS model
    print(f"Loading TTS model: {MODEL}")
    try:
        tts = TTS(MODEL)
    except Exception as e:
        print(f"Error loading TTS model: {e}")
        sys.exit(1)
    
    # Create output directory
    out_dir = Path(getattr(args, 'out_dir') or getattr(args, 'out-dir'))
    out_dir.mkdir(parents=True, exist_ok=True)
    
    # JSON batch processing
    rows = load_rows_from_json(args.json, args.language)
    print(f"Loaded {len(rows)} entries from JSON file")
    
    if not rows:
        print("No valid text entries found to process.")
        sys.exit(1)
    
    # Generate speech for each row
    print(f"Processing {len(rows)} entries...")
    successful = 0
    for i, row in enumerate(rows, 1):
        output_path = out_dir / f"{row['id']}.wav"
        print(f"[{i}/{len(rows)}] Generating: {row['id']} ({row['language']}) - '{row['text'][:50]}{'...' if len(row['text']) > 50 else ''}'")
        
        try:
            tts.tts_to_file(
                text=row["text"],
                speaker_wav=getattr(args, 'speaker_wav') or getattr(args, 'speaker-wav'),
                language=row["language"],
                file_path=str(output_path),
            )
            print(f"  ✓ Generated: {output_path}")
            successful += 1
        except Exception as e:
            print(f"  ✗ Error generating {row['id']}: {e}")
    
    print(f"\nCompleted: {successful}/{len(rows)} files generated successfully")
    if successful < len(rows):
        print(f"Failed: {len(rows) - successful} files")

if __name__ == "__main__":
    main()