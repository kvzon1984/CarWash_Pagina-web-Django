from django.forms import ValidationError
from django.db import models


class MaxsizeFileValidator:
    def __init__(self, max_file_size=5):
        self.max_file_size = max_file_size

    def __call__(self,value):
        size = value.size
        max_size = self.max_file_size * 1048576

        if size > max_size:
            raise ValidationError(f"El tamano maximo del archivo dedbe ser de {self.max_file_size} MB")
            
        return value



class MaxLengthValidator:
    def __init__(self,max_length_text_file =120):
        self.max_length_text_file = max_length_text_file

    def __call__(self,lenght_value):
        lenght = lenght_value.lenght
        max_lenght = self.max_length_text_file

        if lenght > max_lenght:
            raise ValidationError(f"El largo maximo para escribir son de {self.max_length_text_file} caracteres")
        
        return lenght_value