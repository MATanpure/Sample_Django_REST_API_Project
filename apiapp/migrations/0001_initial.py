# Generated by Django 2.2.7 on 2021-02-12 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('real_name', models.CharField(max_length=50)),
                ('tz', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'MEMBER_INFO_TABLE',
            },
        ),
        migrations.CreateModel(
            name='ActivityPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.CharField(max_length=50)),
                ('end_time', models.CharField(max_length=50)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_periods', to='apiapp.Member')),
            ],
            options={
                'db_table': 'ACTIVITY_PERIOD_INFO_TABLE',
            },
        ),
    ]
