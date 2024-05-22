from django.db import models
#import genai
import google.generativeai as genai
import os

#genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
#model = genai.GenerativeModel('gemini-pro')
model = genai.GenerativeModel('models/gemini-pro')
#model = genai.GenerativeModel(model_name="gemini-pro", generation_config=generation_config, safety_settings=safety_settings)

def generate_description_from_title_gemini(title):
    #response = genai.stream_generate_content(
    response = genai.generate_content(
        model="models/gemini-pro",
        prompt=title
    )

class GeminiTextElement(models.Model): 
    title = models.CharField(max_length=255)  
    content = models.TextField(blank=True)  
    
    def __str__(self):  
        return self.title  
    
    def save(self, *args, **kwargs):  
        if not self.content:  
            self.content = generate_description_from_title_gemini(self.title)  
            super().save(*args, **kwargs)  