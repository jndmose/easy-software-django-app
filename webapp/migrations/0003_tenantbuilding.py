# Generated by Django 3.0.6 on 2021-04-22 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_tenant'),
    ]

    operations = [
        migrations.CreateModel(
            name='TenantBuilding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkin_date', models.DateField(blank=True, null=True)),
                ('contract_amount', models.FloatField()),
                ('status', models.CharField(choices=[('active', 'active'), ('inactive', 'inactive')], default='active', max_length=128)),
                ('building', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.Building')),
                ('tenant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.Tenant')),
            ],
        ),
    ]
