import pgm
import algorithm as alg
import cv2
import numpy as np
import cmath
import matplotlib.pyplot as plt

detail, cross = pgm.read_pgmb('./src/PGM/Cross.pgm') # magic number from detail is 'P5\r' must be strip \r out.
width = detail[1][0]
height = detail[1][1]

pad_cross = alg.padding(cross, width, height, 256)
size = ["P5",[256,256],255] #detail of cross after padding

fft = np.fft.fft2(pad_cross)
fft_shiftC = np.fft.fftshift(fft)
amp = alg.amplitude(fft,256,256)
amp_c = alg.amplitude(fft_shiftC,256,256)
amp_norm = alg.normalize_color(amp)
amp_c_norm = alg.normalize_color(amp_c)
phase = alg.phase(fft,256,256)
phase_norm = alg.normalize_color(phase)
phase_shiftC = alg.phase(fft_shiftC,256,256)
phase_c_norm = alg.normalize_color(phase_shiftC)

infft_p = np.fft.ifft2(phase)
plt.imshow(np.abs(infft_p), "gray"), plt.title("Inverse fourier phase")
plt.show()
infft_a = np.fft.ifft2(amp)
plt.imshow(np.abs(infft_a), "gray"), plt.title("Inverse fourier amplitude")
plt.show()

pgm.write_txt_pgma('./src/readPGM/Cross.txt', cross, detail)


