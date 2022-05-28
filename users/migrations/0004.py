import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='time_in',
            field=models.TimeField(default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='time_out',
            field=models.TimeField(default=datetime.datetime.now, null=True),
        ),
    ]
