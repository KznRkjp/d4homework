# Generated by Django 2.2.6 on 2019-11-20 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0004_remove_book_publisher'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='p_library.Publisher'),
        ),
    ]