# Generated by Django 4.1.2 on 2022-10-25 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newssite', '0010_rename_author_category_rename_author_new_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Author',
        ),
        migrations.RenameField(
            model_name='new',
            old_name='category',
            new_name='author',
        ),
    ]