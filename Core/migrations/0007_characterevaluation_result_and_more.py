# Generated by Django 5.1 on 2024-09-04 21:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0006_alter_characterevaluation_behavior_five_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='characterevaluation',
            name='result',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='characterevaluation',
            unique_together={('evaluator', 'employee')},
        ),
    ]
