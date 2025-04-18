import os
import unittest

from tts import Speech


class TestCase(unittest.TestCase):
    def test_raw(self):
        content_lines = [
            "Hello!",
            "My name is TTS",
            "I am a Text to Speech engine",
            "Bye",
        ]
        tts = Speech(content_lines)
        output_path = os.path.join("tests", "output-raw.mp3")
        tts.write(output_path)

    def test_txt(self):
        input_path = os.path.join("tests", "input.txt")
        tts = Speech.from_generic_file(input_path)
        output_path = os.path.join("tests", "output-txt.mp3")
        tts.write(output_path)

    def test_md(self):
        input_path = os.path.join("tests", "input.md")
        tts = Speech.from_generic_file(input_path)
        output_path = os.path.join("tests", "output-md.mp3")
        tts.write(output_path)

    def test_docx(self):
        input_path = os.path.join("tests", "input.docx")
        tts = Speech.from_generic_file(input_path)
        output_path = os.path.join("tests", "output-docx.mp3")
        tts.write(output_path)
