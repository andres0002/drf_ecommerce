# Generated by Django 5.2.1 on 2025-06-08 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0003_expenses_category_historicalexpenses_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalmermas',
            name='lost_modey',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Dinero perdido'),
        ),
        migrations.AlterField(
            model_name='mermas',
            name='lost_modey',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Dinero perdido'),
        ),
    ]
