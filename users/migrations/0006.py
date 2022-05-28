

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='time_in',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='time_out',
            field=models.DateTimeField(null=True),
        ),
    ]
