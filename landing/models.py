from django.db import models


class Contact(models.Model):
    name = models.CharField("Foydalanuvchi ismi", max_length=120)
    email = models.EmailField()
    subject = models.CharField("So'rov mavzusi", max_length=250)
    message = models.TextField("Xabar")
    sent_at = models.DateTimeField("So'rov jonatilgan sana", auto_now_add=True)
    is_answered = models.BooleanField("Javob berildimi?", default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-sent_at']
        verbose_name = "Zayavka"
        verbose_name_plural = "Zayavkalar"
