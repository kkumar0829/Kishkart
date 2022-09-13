# Generated by Django 4.1 on 2022-09-13 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostSave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='cartdata',
            options={'verbose_name': 'Cart List'},
        ),
        migrations.AlterModelOptions(
            name='productprice',
            options={'verbose_name': 'Price List'},
        ),
        migrations.AlterField(
            model_name='productprice',
            name='price_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='lol', to='cart.cartdata'),
        ),
    ]
