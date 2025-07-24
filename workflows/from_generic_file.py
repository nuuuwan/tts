import sys

from tts import Speech

# test:
# python .\workflows\from_generic_file.py .\tests\input.docx
# .\tests\input.docx.mp3

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: tts <input_file_path> <output_file_path>")
        sys.exit(1)
    file_path = sys.argv[1]
    output_path = sys.argv[2]
    Speech.from_generic_file(file_path).write(output_path)
