from django import forms



class uploaderForm(forms.Form):

    file_score_info=forms.FileField(label="Archivo para carga")


