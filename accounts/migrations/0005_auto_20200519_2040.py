# Generated by Django 3.0.5 on 2020-05-19 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200515_2342'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='education',
            options={'verbose_name': 'Education', 'verbose_name_plural': 'Educations'},
        ),
        migrations.AlterField(
            model_name='profile',
            name='professional_status',
            field=models.CharField(blank=True, choices=[('Developer', 'Developer'), ('Junior Developer', 'Junior Developer'), ('Senior Developer', 'Senior Developer'), ('Intern', 'Intern'), ('Manager', 'Manager'), ('Student Or Learning', 'Student or Learning'), ('Instructor or Teacher', 'Instructor or Teacher'), ('Other', 'Other')], default='Other', max_length=21, null=True),
        ),
    ]