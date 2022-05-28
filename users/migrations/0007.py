
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='present',
            field=models.BooleanField(default=False),
        ),
    ]
