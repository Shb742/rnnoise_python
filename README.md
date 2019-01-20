# A python wrapper for rnnoise
python wrapper for the [rnnoise](https://github.com/xiph/rnnoise) library.

# Prerequisites
* Have [rnnoise](https://github.com/xiph/rnnoise) installed
* python (2/3)
* numpy

# Example usage
**It operates on RAW 16-bit (machine endian) mono
PCM data sampled at 48 kHz.**

**Each frame of data must be in binary, and must be 480 int16s (i.e 2 bytes per sample.) This translates to 960 bytes per audio frame.**

```
arecord -v -f S16_LE -c1 -r48000 -t raw | python3 rnn_test.py
```
```python
import rnnoise,sys
denoiser = rnnoise.RNNoise()
stream = sys.stdin.buffer
input_data = stream.read(480*2)
va_prob,denoised_data = denoiser.process_frame(input_data)
```

