from django.shortcuts import render
from .forms import ImageForm
from .models import POST
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import cv2
import joblib
from tumordetection_version_OnE import settings

def result_views(request, *args, **kwargs):
    context={}
    form=ImageForm(data=request.POST,files=request.FILES)
    context['form']=ImageForm()
    if request.method == "POST":
        ensemble=joblib.load('hybrid_model.sav')
        if form.is_valid():
            form.save()
            obj=form.instance
            img2=obj.MRI_IMAGE
            #print(obj. get_profile_image_filename)
            path="C:/Users/User/Desktop/Raunak Ali/AI PROJECT-TUMOR DETECTION/PROJECT CODE  WISE/tumordetection_version_OnE/media_cdn/"+ str(obj.MRI_IMAGE)
            dec = {0:'No Tumor Detected', 1:'Positive Tumor Detected!'}
            #img=np.array(path)
            img = cv2.imread(path)
            print(img)
            img1 = cv2.resize(img,(200,200))
            print(img1.shape)
            img1=img1[:,:,0]
            print(img1.shape)
            img1 = img1.reshape(1,-1)/255
            print(img1.shape)
            answer=ensemble.predict(img1)
            print(answer)
            p=dec[answer[0]]
            return render(request,"Output.html",{"obj":obj,"Answer":p})
        else:
            form=ImageForm()
            img=Image.objects.all()
            return render(request, "Output.html", context)
    return render(request, "Uploading.html", context)



# Create your views here.
