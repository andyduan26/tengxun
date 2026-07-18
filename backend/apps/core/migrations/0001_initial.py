from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="VideoProject",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=120, verbose_name="标题")),
                ("description", models.TextField(verbose_name="描述/看点")),
                ("cover_image_url", models.URLField(max_length=500, verbose_name="封面大图 URL")),
                ("thumbnail_url", models.URLField(max_length=500, verbose_name="缩略图 URL")),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("电视剧", "电视剧"),
                            ("电影", "电影"),
                            ("动漫", "动漫"),
                            ("综艺", "综艺"),
                            ("纪录片", "纪录片"),
                            ("短剧", "短剧"),
                        ],
                        max_length=20,
                        verbose_name="分类",
                    ),
                ),
                ("is_vip", models.BooleanField(default=False, verbose_name="是否 VIP 权限")),
                ("sort_weight", models.IntegerField(default=0, verbose_name="排序权重")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="创建时间")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="更新时间")),
            ],
            options={
                "verbose_name": "视频剧集",
                "verbose_name_plural": "视频剧集",
                "ordering": ["-sort_weight", "-created_at", "-id"],
            },
        ),
    ]
