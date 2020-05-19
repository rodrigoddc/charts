from django.db import models


class DataSample(models.Model):
    JANUARY = 'jan'
    FEBRUARY = 'feb'
    MARCH = 'mar'
    APRIL = 'apr'
    MAY = 'may'
    JUNE = 'jun'
    JULY = 'jul'
    AUGUST = 'aug'
    SEPTEMBER = 'sep'
    OCTOBER = 'oct'
    NOVEMBER = 'nov'
    DECEMBER = 'dec'

    LABELS = {
        (JANUARY, 'Janary'),
        (FEBRUARY, 'February'),
        (MARCH, 'March'),
        (APRIL, 'April'),
        (MAY, 'May'),
        (JUNE, 'June'),
        (JULY, 'July'),
        (AUGUST, 'August'),
        (SEPTEMBER, 'September'),
        (OCTOBER, 'October'),
        (NOVEMBER, 'November'),
        (DECEMBER, 'December'),
    }

    month = models.CharField(max_length=3, choices=LABELS)
    price = models.DecimalField(max_length=10, max_digits=10, decimal_places=2)

    def __str__(self):
        return self.month