# Generated by Django 3.2.3 on 2021-07-06 12:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('engname', models.CharField(max_length=255)),
                ('chiname', models.CharField(blank=True, max_length=255, null=True)),
                ('idnumber', models.CharField(blank=True, max_length=25, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('tel', models.IntegerField(blank=True, null=True)),
                ('tel2', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=10)),
                ('language', models.CharField(max_length=20)),
                ('receipt', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=10)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('allergy', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='patient', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
