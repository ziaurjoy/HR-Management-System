# Generated by Django 4.1.2 on 2022-10-22 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Districts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_english', models.CharField(default=None, max_length=120)),
                ('name_bangla', models.CharField(default=None, max_length=25)),
                ('url', models.CharField(default=None, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Divisions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_english', models.CharField(default=None, max_length=25, null=True)),
                ('name_bangla', models.CharField(default=None, max_length=25, null=True)),
                ('url', models.CharField(default=None, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Upazila',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_english', models.CharField(max_length=120)),
                ('name_bangla', models.CharField(default=None, max_length=25)),
                ('url', models.CharField(default=None, max_length=50)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thana_district', to='address_app.districts')),
            ],
        ),
        migrations.AddField(
            model_name='districts',
            name='division',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='distric_division', to='address_app.divisions'),
        ),
    ]
