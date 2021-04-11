from django import forms
from .models import Comments, Post


class NewPostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['description', 'tags']


class NewCommentForm(forms.ModelForm):

	class Meta:
		model = Comments
		fields = ['comment']
