# Generated by Django 5.2 on 2025-04-16 04:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0011_alter_brand_rating'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductRecommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(default=0.0, help_text='The recommendation score for the product.')),
                ('recommendation_type', models.CharField(choices=[('preferred', 'Preferred'), ('liked', 'Liked'), ('new', 'New'), ('popular', 'Popular')], default='preferred', help_text='Type of recommendation.', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='The timestamp when the recommendation was created.')),
                ('product', models.ForeignKey(help_text='The product being recommended.', on_delete=django.db.models.deletion.CASCADE, related_name='recommended_to', to='core.product')),
                ('user', models.ForeignKey(help_text='The user who receives the recommendation.', on_delete=django.db.models.deletion.CASCADE, related_name='recommendations', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Product Recommendation',
                'verbose_name_plural': 'Product Recommendations',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='UserBehaviorLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(choices=[('view', 'View'), ('like', 'Like'), ('purchase', 'Purchase')], max_length=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='behavior_logs', to='core.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='behavior_logs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
