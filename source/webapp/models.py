from django.db import models


class Poll(models.Model):
    text = models.TextField(max_length=400, verbose_name='text of poll')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Time created')

    def __str__(self):
        return self.text


class Choice(models.Model):
    poll = models.ForeignKey('webapp.Poll', related_name='choice',
                             on_delete=models.CASCADE, verbose_name='poll')
    text = models.TextField(max_length=400, verbose_name='text')

    def __str__(self):
        return self.text


class Answer(models.Model):
    choice = models.ForeignKey('webapp.Choice', related_name='Answer', on_delete=models.CASCADE, verbose_name='choice')
    poll = models.ForeignKey('webapp.Poll', related_name='Answer',
                             on_delete=models.CASCADE, verbose_name='poll')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Time created')

