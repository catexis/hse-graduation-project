# Generated by Django 2.0.4 on 2018-05-02 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vergleich', '0002_scrapperbenchcpu'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScrapperBenchHDD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=1000)),
                ('url', models.URLField(blank=True, max_length=1000)),
                ('score', models.FloatField(blank=True)),
                ('rank', models.IntegerField(blank=True)),
                ('in_stock', models.BooleanField(default=False)),
                ('price', models.FloatField(blank=True)),
            ],
        ),
    ]
