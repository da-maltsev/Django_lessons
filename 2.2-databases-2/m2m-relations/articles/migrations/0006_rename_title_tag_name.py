# Generated by Django 4.0.6 on 2022-07-04 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_alter_articlescope_article_alter_articlescope_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='title',
            new_name='name',
        ),
    ]