# Generated by Django 4.0.5 on 2022-09-02 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_noticia_contenido'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='noticias'),
        ),
    ]
