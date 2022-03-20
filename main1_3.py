import pgm
import algorithm as alg
import cv2
import numpy as np
from PIL import Image

detail, cross = pgm.read_pgmb('./src/PGM/Cross.pgm') # magic number from detail is 'P5\r' must be strip \r out.
width = detail[1][0]
height = detail[1][1]

# img = cv2.imread('./src/PGM/Cross.pgm', 0) # return array
rotate = alg.rotate(cross, width, height, 30, 255)
fft = np.fft.fft2(rotate)
fft_shiftC = np.fft.fftshift(fft)
amp_c = alg.amplitude(fft_shiftC,200,200)
amp_c_norm = alg.normalize_color(amp_c)

ori = Image.open('./src/PGM/Cross.pgm')
rotated = ori.rotate(30)
ori = rotated.save('./src/PGM/Cross30.pgm')
detail2, cross30 = pgm.read_pgmb('./src/PGM/Cross30.pgm')
fft2 = np.fft.fft2(cross30)
fft2_shiftC = np.fft.fftshift(fft2)
amp2_c = alg.amplitude(fft2_shiftC,200,200)
amp2_c_norm = alg.normalize_color(amp2_c)

pgm.write_txt_pgma('./src/readPGM/Cross.txt', cross, detail)
pgm.write_txt_pgma('./src/readPGM/CrossRotate.txt', rotate, detail)

pgm.write_pgm('./src/readPGM/CrossRotate.pgm', rotate, detail)
pgm.write_pgm('./src/readPGM/AmplitudeCrossRotateCentralNormalize.pgm', amp_c_norm, detail)
pgm.write_pgm('./src/readPGM/AmplitudeCross30CentralNormalize.pgm', amp2_c_norm, detail2)

