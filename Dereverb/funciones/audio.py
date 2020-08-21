import librosa 
import numpy as np
import scipy 

def audio_import(nom_audio,largo):
  display=nom_audio
  x,fs= librosa.core.load(nom_audio,sr=16000)
  inicio=24000
  corte=inicio+largo
  largo_audio=len(x)
  if largo_audio<corte:
    
    padding= corte-largo_audio
    x_trim=np.pad(x[inicio:],(0,padding),'constant',constant_values=0)   
    
  else: 
    x_trim=x[inicio:corte]

  #Normalizar según percentil 95%

  norm_val = np.quantile(np.abs(x_trim),0.95)
  x_norm = x_trim/norm_val

  return x_norm,norm_val

def convolve(x,reverb,largo):
  
  convol=scipy.signal.convolve(x,reverb,mode='full', method='fft')
  convol_trim=convol[:largo]

  return convol_trim

def func (x):

  return x

  %%

