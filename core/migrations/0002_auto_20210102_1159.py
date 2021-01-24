# Generated by Django 3.1.4 on 2021-01-02 03:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='category_type',
            field=models.CharField(choices=[('Photoshop', 'Photoshop'), ('Lightroom', 'Lightroom')], default='Photoshop', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='WishList',
        ),
    ]