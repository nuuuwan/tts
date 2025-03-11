import sys

from tts import Speech

# test:
#   python .\workflows\from_generic_file.py .\tests\input.docx

if __name__ == "__main__":
    file_path = sys.argv[1]
    output_path = file_path + ".mp3"
    Speech.from_generic_file(file_path).write(output_path)
