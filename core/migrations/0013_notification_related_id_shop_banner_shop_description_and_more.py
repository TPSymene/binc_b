# Generated by Django 5.2 on 2025-04-19 12:30

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_product_original_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='related_id',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Related ID'),
        ),
        migrations.AddField(
            model_name='shop',
            name='banner',
            field=models.ImageField(blank=True, null=True, upload_to='shop_banners/', verbose_name='Shop Banner'),
        ),
        migrations.AddField(
            model_name='shop',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Shop Description'),
        ),
        migrations.AddField(
            model_name='shop',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Shop Email'),
        ),
        migrations.AddField(
            model_name='shop',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Shop Phone'),
        ),
        migrations.AddField(
            model_name='shop',
            name='social_media',
            field=models.JSONField(blank=True, default=dict, null=True, verbose_name='Social Media Links'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='notification_type',
            field=models.CharField(choices=[('promotion', 'Promotion'), ('order', 'Order Update'), ('general', 'General'), ('inventory', 'Inventory Alert')], default='general', max_length=20),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Customer Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Phone Number')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Address')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('processing', 'Processing'), ('shipped', 'Shipped'), ('delivered', 'Delivered'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='pending', max_length=20, verbose_name='Order Status')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total Amount')),
                ('shipping_address', models.TextField(verbose_name='Shipping Address')),
                ('payment_method', models.CharField(choices=[('credit_card', 'Credit Card'), ('paypal', 'PayPal'), ('cash_on_delivery', 'Cash on Delivery')], default='credit_card', max_length=20, verbose_name='Payment Method')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='core.customer')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='core.shop')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Quantity')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='core.order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orderitem', to='core.product')),
            ],
        ),
    ]
