from django import forms


class OrderingListForm(forms.Form):
    ordering_list = forms.CharField(max_length=50,label="Enter the order of columns in which you want to sort ?")

    def __unicode__(self):
        return self.ordering_list