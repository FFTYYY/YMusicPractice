import pyaudio
import wave
from tqdm import tqdm

def 录音到文件(文件名 , 录音时间 = 3 , 频率 = 9600):
	'''from official example http://people.csail.mit.edu/hubert/pyaudio'''
	CHUNK = 1024
	FORMAT = pyaudio.paInt16
	CHANNELS = 1
	RATE = 频率
	RECORD_SECONDS = 录音时间
	WAVE_OUTPUT_FILENAME = 文件名

	p = pyaudio.PyAudio()

	stream = p.open(format=FORMAT,
	                channels=CHANNELS,
	                rate=RATE,
	                input=True,
	                frames_per_buffer=CHUNK)

	frames = []

	for i in tqdm(range(0, int(RATE / CHUNK * RECORD_SECONDS)) , ncols=70 , desc = "录音中"):
	    data = stream.read(CHUNK)
	    frames.append(data)

	stream.stop_stream()
	stream.close()
	p.terminate()

	wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	wf.setnchannels(CHANNELS)
	wf.setsampwidth(p.get_sample_size(FORMAT))
	wf.setframerate(RATE)
	wf.writeframes(b''.join(frames))
	wf.close()
