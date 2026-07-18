from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("video", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="videoproject",
            name="video_file",
            field=models.FileField(blank=True, upload_to="videos/", verbose_name="视频文件"),
        ),
    ]
