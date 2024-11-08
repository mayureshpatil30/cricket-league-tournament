from django import forms
from main.models import Team, Matches
from django.forms import ModelForm


class MatchFixture(forms.Form):
    teams = forms.ModelMultipleChoiceField(queryset=Team.objects.all(),
                                           required=True,
                                           widget=forms.CheckboxSelectMultiple())
    
    
class MatchUpdate(ModelForm):
    class Meta:
        model = Matches
        fields = ['winner_team']
     
    def __init__(self, *args, **kwargs):
        super(MatchUpdate, self).__init__(*args, **kwargs)
        self.fields['winner_team'] = forms.ChoiceField(choices=[])
    
    class Meta:
        model = Matches
        fields = ['looser_team']
     
    def __init__(self, *args, **kwargs):
        super(MatchUpdate, self).__init__(*args, **kwargs)
        self.fields['looser_team'] = forms.ChoiceField(choices=[])
