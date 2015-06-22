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
    self.speaker = speaker
    self.passive_stt_engine = passive_stt_engine
    self.active_stt_engine = active_stt_engine
    self._logger.info("Initializing PyAudio. ALSA/Jack error messages " +
                      "that pop up during this process are normal and " +
                      "can usually be safely ignored.")
    self._audio = pyaudio.PyAudio()
    self._logger.info("Initialization of PyAudio completed.")

  def __del__(self):
    self._audio.terminate()
