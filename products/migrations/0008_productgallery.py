# Generated by Django 4.0.4 on 2022-05-06 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_reviewrating'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(max_length=255, upload_to='media')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products')),
            ],
        ),
    ]