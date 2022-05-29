from platform import python_branch
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import *
from .models import *
from backend.settings import MEDIA_URL
from PIL import Image
import numpy as np
from glob import glob
import cv2
import tensorflow as tf
from keras.utils import plot_model
from keras.models import Model, Sequential
import keras.layers as lay
import os
import matplotlib.pyplot as plt
import pickle
from keras.utils import to_categorical
from keras_preprocessing.sequence import pad_sequences
from gtts import gTTS
import base64
import io
from PIL import *
  
# This module is imported so that we can 
# play the converted audio

# Create your views here.


def convert_image_view(request):

    if request.method == 'POST':
        form = ConvertForm(request.POST, request.FILES)
        print(request.FILES['convert_Main_Img'])

        if form.is_valid():
            form.save()
            image = Convert.objects.all().order_by("-id")[0].convert_Main_Img
            eimage = Image.open(image)
            # eimage.show()
            # print(eimage)
            # try:
            #     print(cv2.imread(str(MEDIA_URL) + str(eimage)))
            # except Exception as e:
            #     print(e)
            models_folder = settings.BASE_DIR / 'backend' / 'vacobs'
            filename = 'vacob.pickle'
            file_path = os.path.join(models_folder, os.path.basename(filename))
            with open(file_path, 'rb') as handle:
             vacob = pickle.load(handle)

             max=40
            from keras.applications import ResNet50
            incept_model = ResNet50(include_top=True)
            last = incept_model.layers[-2].output
            resnet = Model(inputs = incept_model.input,outputs = last)
            resnet.trainable=False
            resnet.summary()
            image_model = Sequential()
            image_model.add(lay.Dense(128, input_shape=(2048,), activation='relu'))
            image_model.add(lay.RepeatVector(max))
            language_model = Sequential()
            language_model.add(lay.Embedding(input_dim=len(vacob)+1, output_dim=128, input_length=max))
            language_model.add(lay.LSTM(256, return_sequences=True))
            language_model.add(lay.TimeDistributed(lay.Dense(128)))
            conca = lay.Concatenate()([image_model.output, language_model.output])
            x = lay.LSTM(128, return_sequences=True)(conca)
            x = lay.LSTM(512, return_sequences=False)(x)
            out = lay.Dense(len(vacob)+1,activation='softmax')(x)
            model = Model(inputs=[image_model.input, language_model.input], outputs = out)

            # model.load_weights("../input/model_weights.h5")
            model.compile(loss='categorical_crossentropy', optimizer='RMSprop', metrics=['accuracy'])
            filenameb = 'best_model_acc.h5'
            file_pathb = os.path.join(models_folder, os.path.basename(filenameb))
            model.load_weights(file_pathb)
            inv_vacob = {v:k for k, v in vacob.items()}

            h=7000

            models_folder = settings.BASE_DIR / 'media' / 'images'
            # filenamec = 'duck.jpg'
            filenamec = str(Convert.objects.all().order_by("-id")[0].convert_Main_Img)
            file_pathc = os.path.join(models_folder, os.path.basename(filenamec))

            test=cv2.imread(file_pathc)
            test = cv2.cvtColor(test, cv2.COLOR_BGR2RGB)
            test = cv2.resize(test, (224,224))
            test = test.reshape(1,224,224,3)
            predt = resnet.predict(test).reshape(1,2048)

            word=['<sos>']
            word_encoded=[]
            stement=''
            for i in range(20):
                word_encoded=[]
                for w in word:
                    word_encoded.append(vacob[w])


                encoded = [word_encoded]
                encoded = pad_sequences(encoded, padding='post', truncating='post', maxlen=max)

                prediction = np.argmax(model.predict([predt, encoded]))

                sampled_word = inv_vacob[prediction]
                if sampled_word == '<eos>':
                   break

                word.append(sampled_word)
                stement+=' '+sampled_word

            plt.imshow(test.reshape(224,224,3))
            print(stement)
            # Language in which you want to convert
            language = 'en'
  
# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
            myobj = gTTS(text=stement, lang=language, slow=True)
  
# Saving the converted audio in a mp3 file named
# welcome 
            myobj.save("media/res.mp3")


            return redirect('output')
    else:
        form = ConvertForm()
    return render(request, 'index.html', {'form': form})


def output(request):
    return render(request, 'output.html')

def home(request):
    return render(request, 'home.html')
