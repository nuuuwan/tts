import sys

from tts import Speech

# test:
# python .\workflows\from_generic_file.py .\tests\input.docx
# .\tests\input.docx.mp3

if __name__ == "__main__":
    file_path = sys.argv[1]
    output_path = sys.argv[2]
    Speech.from_generic_file(file_path).write(output_path)
