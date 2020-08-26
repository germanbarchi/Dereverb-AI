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


def import_cs (nom_audio,corte):  

  x,fs= librosa.core.load(nom_audio,sr=16000)
  largo_audio=len(x)

  if largo_audio<corte:
    
    padding= corte-largo_audio
    x_trim=np.pad(x,(0,padding),'constant',constant_values=0)   
    
  else: 
    x_trim=x[:corte]

  norm_val = np.quantile(np.abs(x_trim),0.95)
  x_norm = x_trim/norm_val

  return x_norm

def convolve(x,reverb_path,largo):
  
  reverb,fs= librosa.core.load(reverb_path,sr=16000)
  convol=scipy.signal.convolve(x,reverb,mode='full', method='fft')
  convol_trim=convol[:largo]

  return convol_trim

def split (nom_audio,largo,solapamiento):

  lista=[]
  x_cut,fs= librosa.core.load(nom_audio,sr=16000) 
  leng=len(x_cut)
  dif=largo-solapamiento
  i=0
  sup=largo
  while sup<leng:
    y=x_cut[i*dif:sup]
    lista.append(y)
    i=i+1
    sup=(i*dif)+largo
  lista=np.array(lista)
  
  return lista_array


