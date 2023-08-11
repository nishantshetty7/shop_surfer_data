# Generated by Django 4.2.2 on 2023-08-11 18:01

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_cart_cartitem_cart_cart_items'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('user_id', models.IntegerField(unique=True)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('shipping_address', models.TextField()),
                ('payment_method', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(unique=True)),
                ('full_name', models.CharField(blank=True, max_length=150)),
                ('mobile_number', models.CharField(max_length=10)),
                ('pin_code', models.CharField(max_length=10)),
                ('address1', models.TextField()),
                ('address2', models.TextField()),
                ('city', models.CharField(blank=True, max_length=150)),
                ('state', models.CharField(blank=True, max_length=150)),
                ('is_default', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='shop.product')),
            ],
            options={
                'unique_together': {('order', 'product')},
            },
        ),
        migrations.AddField(
            model_name='order',
            name='order_items',
            field=models.ManyToManyField(related_name='order_items', through='shop.OrderItem', to='shop.product'),
        ),
    ]