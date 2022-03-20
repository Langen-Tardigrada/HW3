import pgm
import algorithm as alg
import cv2
import numpy as np

detail, cross = pgm.read_pgmb('./src/PGM/Cross.pgm') # magic number from detail is 'P5\r' must be strip \r out.
width = detail[1][0]
height = detail[1][1]

pad_cross = alg.padding(cross, width, height, 256)
size = ["P5",[256,256],255] #detail of cross after padding

# img = cv2.imread('./src/PGM/Cross.pgm', 0) # return array
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

pgm.write_txt_pgma('./src/readPGM/Cross.txt', cross, detail)
pgm.write_txt_pgma('./src/readPGM/CrossPadding.txt', pad_cross, size)
pgm.write_txt_pgma('./src/readPGM/AmplitudeCross.txt', amp, size)
pgm.write_txt_pgma('./src/readPGM/AmplitudeCrossCentral.txt', amp_c, size)
pgm.write_txt_pgma('./src/readPGM/AmplitudeCrossNorm.txt', amp_norm, size)
pgm.write_txt_pgma('./src/readPGM/AmplitudeCrossCentralNorm.txt', amp_c_norm, size)
pgm.write_txt_pgma('./src/readPGM/PhaseCrossNorm.txt', phase_norm, size)
pgm.write_txt_pgma('./src/readPGM/PhaseCrossCentralNorm.txt', phase_c_norm, size)

pgm.write_pgm('./src/readPGM/AmplitudeCrossNorm.pgm', amp_norm, size)
pgm.write_pgm('./src/readPGM/AmplitudeCrossCentralNorm.pgm', amp_c_norm, size)
pgm.write_pgm('./src/readPGM/PhaseCrossNorm.pgm', phase_norm, size)
pgm.write_pgm('./src/readPGM/PhaseCrossCentralNorm.pgm', phase_c_norm, size)

