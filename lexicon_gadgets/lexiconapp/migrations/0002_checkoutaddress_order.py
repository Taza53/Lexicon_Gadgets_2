# Generated by Django 4.1.2 on 2022-11-24 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lexiconapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkoutaddress',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lexiconapp.order'),
        ),
    ]
