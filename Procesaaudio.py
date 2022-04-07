# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 21:02:47 2020

@author: jaime calderon
"""


from scipy.io import wavfile
from winsound import *


import matplotlib.pyplot as plt
import numpy as np
import pyaudio
import wave
import convert_audio_to_text


plt.close('all')

Format = pyaudio.paInt16
Channel = 1
Rate = 44100
Chuck = 1024
Tiempo = 10
Nombre = 'grabacion1.wav'

Audio = pyaudio.PyAudio()
Sonido = Audio.open(format=Format, channels=Channel, rate=Rate,
                    input=True, output=True, frames_per_buffer=Chuck)

print('Inicia la grabacion ')
input('Presiona Tecla:')
datos = []
FF = []
for i in range(0, int(Rate/Chuck*Tiempo)):
    datos.append(Sonido.read(Chuck))
    FF.append(np.frombuffer(Sonido.read(Chuck), dtype=np.int16))

AA = np.hstack(FF)

print('Termina la grabacion')
Sonido.stop_stream()
Sonido.close()
Audio.terminate()

wF = wave.open(Nombre, 'wb')
wF.setnchannels(Channel)
wF.setsampwidth(Audio.get_sample_size(Format))
wF.setframerate(Rate)
wF.writeframes(b''.join(datos))
wF.close()


PlaySound(r"grabacion1.wav", SND_FILENAME | SND_ASYNC)


# =========================== ACONDICIONAMIENTO DE SEÑAL=======================================

senalN = AA / np.max(np.abs(AA))

Bin1 = np.where(np.abs(senalN) >= 0.5, 1, 0)
senal1 = []
for i in range(0, len(Bin1)-439, 1):
    senal1.append(np.mean(Bin1[i: i+440]))


Bin2 = np.where(np.array(senal1) >= 0.1, 1, 0)
senal2 = []
for i in range(0, len(Bin2)-439, 1):
    if (Bin2[i] == 1):
        senal2.append(senalN[i])


senal3 = []
for i in range(0, len(Bin2)-439, 1):
    senal3.append(np.mean(Bin2[i: i+440]))


# plt.figure(1)
# plt.plot(senal3)
# plt.show()

# np.savetxt('prueba1.dat',senal3)

# # # ------------------------  RECORTE DE CARACTERISTICAS ---------------------------

# senal3 = np.loadtxt('Prueba1.dat')
c = 0
corte = []
while c < len(senal3):
    if senal3[c-1] == 0 and senal3[c] > 0:
        corte.append(c)
        c = len(senal3)
    c += 1

c = len(senal3)
while c > 0:
    if senal3[c-1] > 0 and senal3[c] == 0:
        corte.append(c)
        c = 0
    c -= 1
New = senal3[corte[0]:corte[1]]

cont = 3
ini = [0]
for k in range(6000, len(New)):
    if np.sum(New[k-6000:k]) == 0 and New[k] > 0:
        ini.append(k)
        cont += 1

Pro = np.zeros((len(ini), 43154))
for u in range(len(ini)):

    if u == len(ini)-1:
        Pro[u, 0:len(New[ini[u]:-1])] = New[ini[u]:-1]
    else:
        Pro[u, 0:len(New[ini[u]:ini[u+1]])] = New[ini[u]:ini[u+1]]


plt.figure(2)
plt.plot(Pro[0, :])
plt.show()
# # # ----------------------------- KERAS -----------------------------------------

convert_audio_to_text(Pro)
