# Generated by Django 5.0.2 on 2024-05-21 10:43

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0028_alter_post_post_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="body",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
