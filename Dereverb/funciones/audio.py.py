import librosa 
import numpy as np

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

  return x_trim 

#Normalizar según percentil 95%

def percentil_95(all_audios_):

  norm_val = np.quantile(np.abs(all_audios_),0.95)
  all_audios_norm = [x/norm_val for x in all_audios_]

  return x_norm
