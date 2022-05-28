
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='time_in',
            field=models.DateTimeField(default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='time_out',
            field=models.DateTimeField(default=datetime.datetime.now, null=True),
        ),
    ]
