# Generated by Django 3.0.3 on 2020-03-06 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database_manager', '0002_auto_20200305_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='relative_attendance_for_one_lecture',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='relative_attendance_for_one_practical',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='relative_attendance_for_one_tutorial',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='CumulativeAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('was_present_last_class', models.BooleanField()),
                ('total_lectures', models.IntegerField()),
                ('total_tutorials', models.IntegerField()),
                ('total_practicals', models.IntegerField()),
                ('total_lectures_present', models.IntegerField()),
                ('total_tutorials_present', models.IntegerField()),
                ('total_practicals_present', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database_manager.Course')),
                ('last_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database_manager.Class')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database_manager.Student')),
            ],
            options={
                'verbose_name_plural': 'Cumulative Attendance',
            },
        ),
        migrations.AddConstraint(
            model_name='cumulativeattendance',
            constraint=models.UniqueConstraint(fields=('student', 'course'), name='Unique Student Registration in Course'),
        ),
    ]