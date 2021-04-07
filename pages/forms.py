from django import forms
MARKS = [
    ('1', '1'), ('1.5', '1.5'), ('2', '2'), ('2.5', '2.5'), ('3', '3'), ('3.5', '3.5'), ('4', '4'),('4.5', '4.5'), ('5', '5')
]

class ReviewForm(forms.Form):
    name = forms.CharField(label='Фамилия и Имя', max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control'}),
                           required=True
                           )
    text = forms.CharField(label='Отзыв',
                           max_length=1000,
                           widget=forms.Textarea(attrs={'class': 'form-control'}),
                           required=True
                           )
    mark = forms.MultipleChoiceField(label='Оценка', required=False,
        widget=forms.Select,
        choices=MARKS,)