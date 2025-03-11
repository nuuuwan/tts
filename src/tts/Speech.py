import os
import shutil
import tempfile
from functools import cached_property

from docx import Document  # Add this import
from gtts import gTTS
from pydub import AudioSegment
from utils import File, Hash, Log

log = Log("TTS")


class Speech:

    def __init__(self, content_lines: list[str]):
        self.content_lines = content_lines

    @staticmethod
    def from_txt_file(file_path: str):
        assert file_path.endswith(".txt")
        lines = File(file_path).read_lines()
        return Speech(lines)

    @staticmethod
    def from_docx_file(file_path: str):
        assert file_path.endswith(".docx")
        doc = Document(file_path)
        lines = [para.text for para in doc.paragraphs if para.text]
        return Speech(lines)

    @staticmethod
    def from_generic_file(file_path: str):
        if file_path.endswith(".txt"):
            return Speech.from_txt_file(file_path)
        if file_path.endswith(".docx"):
            return Speech.from_docx_file(file_path)
        raise ValueError(f"Unsupported file type: {file_path}")

    def __len__(self):
        return len(self.content_lines)

    @cached_property
    def content(self):
        return "\n".join(self.content_lines)

    @cached_property
    def md5(self):
        return Hash.md5(self.content)

    @cached_property
    def temp_file_path(self) -> str:
        temp_dir = os.path.join(tempfile.gettempdir(), "tts")
        os.makedirs(temp_dir, exist_ok=True)
        return os.path.join(temp_dir, f"tts-{self.md5}.mp3")

    def write_single(self):
        assert len(self) == 1
        if os.path.exists(self.temp_file_path):
            return self.temp_file_path
        tts = gTTS(self.content_lines[0])
        tts.save(self.temp_file_path)
        log.debug(f"Wrote {self.temp_file_path}")
        return self.temp_file_path

    def write(self, output_path: str):
        assert output_path.endswith(".mp3")

        if len(self) == 1:
            return self.write_single()

        if not os.path.exists(self.temp_file_path):

            child_audio_list = []
            for line in self.content_lines:
                child_temp_file_path = Speech([line]).write_single()
                child_audio = AudioSegment.from_file(child_temp_file_path)
                child_audio_list.append(child_audio)

            audio = sum(child_audio_list)
            audio.export(self.temp_file_path, format="mp3")

        shutil.copy(self.temp_file_path, output_path)
        log.info(f"Wrote {output_path}")
        return output_path
