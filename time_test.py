import time
import rnnoise
import random
a = rnnoise.RNNoise()
def time_rnnoise(rounds=1000):
	timer = 0.0
	st = time.time()
	for i in range(rounds):
		inp = bytearray([random.randint(0,255) for _ in range(960)])
	timer = (time.time() - st)
	st = time.time()
	for i in range(rounds):
		inp = bytearray([random.randint(0,255) for _ in range(960)])
		va,out = a.process_frame(inp)
	time_taken_per_frame = ((time.time()-st)-timer) /rounds
	print("time taken for one frame - " + str(time_taken_per_frame ))
	print("time in a frame - " +str(480.0/48000.0)) 
	print(str((480.0/48000.0)/time_taken_per_frame )+"X faster than real")

time_rnnoise()