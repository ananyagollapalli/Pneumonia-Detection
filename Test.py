from keras_preprocessing import image
from keras.models import load_model
from keras.applications.vgg16 import preprocess_input
import numpy as np
from keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import confusion_matrix, classification_report



def prediction(path):
	model=load_model('our_model.h5') #Loading our model
	img=image.load_img(path,target_size=(224,224))
	imagee=image.img_to_array(img) #Converting the X-Ray into pixels
	imagee=np.expand_dims(imagee, axis=0)
	img_data=preprocess_input(imagee)
	prediction=model.predict(img_data)
	if prediction[0][0]>prediction[0][1]: #Printing the prediction of model.
		return "1001"
	else:
		print('Person is affected with Pneumonia.')

