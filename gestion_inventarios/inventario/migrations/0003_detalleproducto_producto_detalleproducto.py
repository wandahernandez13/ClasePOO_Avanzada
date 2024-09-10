# Generated by Django 5.1 on 2024-09-10 19:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_etiqueta_producto_etiquetas'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especificaciones', models.TextField()),
                ('fecha_vencimiento', models.DateField(blank=True, null=True)),
                ('producto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='inventario.producto')),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='detalleProducto',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='producto_detalle', to='inventario.detalleproducto'),
        ),
    ]
