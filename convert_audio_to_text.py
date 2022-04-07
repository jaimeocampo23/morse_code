import pyttsx3
import numpy as np   
import tensorflow as tf
def convert_audio_to_text(Pro):
    rec = ''
    # TrainedM=tf.keras.models.load_model('Face_Model.h5')
    TrainedM=tf.keras.models.load_model('Morse_Model.h5')
    for i in range(Pro.shape[0]):
        Respu=TrainedM.predict(np.asmatrix(Pro[i, :]))
        if (np.argmax(Respu) == 0):
            rec += 'A'  
        elif(np.argmax(Respu) == 1):
            rec += 'B' 
        elif(np.argmax(Respu) == 2):
            rec += 'C' 
        elif(np.argmax(Respu) == 3):
            rec += 'D' 
        elif(np.argmax(Respu) == 4):
            rec += 'E' 
        elif(np.argmax(Respu) == 5):
            rec += 'F' 
        elif(np.argmax(Respu) == 6):
            rec += 'G' 
        elif(np.argmax(Respu) == 7):
            rec += 'H' 
        elif(np.argmax(Respu) == 8):
            rec += 'I' 
        elif(np.argmax(Respu) == 9):
            rec += 'J' 
        elif(np.argmax(Respu) == 10):
            rec += 'K' 
        elif(np.argmax(Respu) == 11):
            rec += 'L' 
        elif(np.argmax(Respu) == 12):
            rec += 'M' 
        elif(np.argmax(Respu) == 13):
            rec += 'N' 
        elif(np.argmax(Respu) == 14):
            rec += 'O' 
        elif(np.argmax(Respu) == 15):
            rec += 'P' 
        elif(np.argmax(Respu) == 16):
            rec += 'Q' 
        elif(np.argmax(Respu) == 17):
            rec += 'R' 
        elif(np.argmax(Respu) == 18):
            rec += 'S' 
        elif(np.argmax(Respu) == 19):
            rec += 'T' 
        elif(np.argmax(Respu) == 20):
            rec += 'U' 
        elif(np.argmax(Respu) == 21):
            rec += 'V' 
        elif(np.argmax(Respu) == 22):
            rec += 'W'         
        elif(np.argmax(Respu) == 23):
            rec += 'X' 
        elif(np.argmax(Respu) == 24):
            rec += 'Y' 
        elif(np.argmax(Respu) == 25):
            rec += 'Z' 
        else:
            rec += ' '
            
    print('MENSAJE RECIBIDO: ', rec)
    engine = pyttsx3.init()
    engine.say(rec)
    engine.runAndWait()