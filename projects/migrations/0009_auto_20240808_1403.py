from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
        ('projects', '0008_alter_project_options_review_owner_and_more'),  # Replace with the previous migration
    ]

    operations = [
        migrations.RenameField(
            model_name='Review',
            old_name='vote',
            new_name='value',
        ),
    ]