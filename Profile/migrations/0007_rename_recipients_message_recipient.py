# Generated by Django 5.0.2 on 2024-02-21 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0006_remove_message_recipients_message_recipients'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='recipients',
            new_name='recipient',
        ),
    ]