import pyaudio

import logging
import tempfile
import wave
import audioop
import alteration
import jasperpath

class IO:
  
  def __init__(self, speaker, passive_stt_engine, active_stt_engine):
    self._logger = logging.getLogger(__name__)
