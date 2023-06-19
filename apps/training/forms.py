from django import forms



class uploaderForm(forms.Form):

    file_score_info=forms.FileField(label="Archivo para carga")

class scrapperForm(forms.Form):

    url_page=forms.CharField(label="Pagina a Scrapear",initial='https://grow.google/intl/es/courses-and-tools/?category=career&topic=cloud-computing',disabled=True)

