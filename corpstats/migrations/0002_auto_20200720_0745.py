# Generated by Django 2.2.12 on 2020-07-20 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corpstats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corpmember',
            name='location_id',
            field=models.BigIntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='corpmember',
            name='location_name',
            field=models.CharField(blank=True, default=None, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='corpmember',
            name='logoff_date',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='corpmember',
            name='logon_date',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='corpmember',
            name='ship_type_id',
            field=models.PositiveIntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='corpmember',
            name='ship_type_name',
            field=models.CharField(default=None, max_length=42, null=True),
        ),
        migrations.AlterField(
            model_name='corpmember',
            name='start_date',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
