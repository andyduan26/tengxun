from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="VideoProject",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=120, verbose_name="视频/剧集标题")),
                ("subtitle", models.CharField(max_length=200, verbose_name="主视觉看点或金句")),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("电视剧", "电视剧"),
                            ("综艺", "综艺"),
                            ("电影", "电影"),
                            ("动漫", "动漫"),
                            ("少儿", "少儿"),
                            ("纪录片", "纪录片"),
                        ],
                        max_length=20,
                        verbose_name="主分类",
                    ),
                ),
                (
                    "tags",
                    models.CharField(
                        help_text="用空格隔开，例如：东方玄幻 东方仙侠 逆袭",
                        max_length=200,
                        verbose_name="细分标签",
                    ),
                ),
                ("cover_image", models.URLField(max_length=500, verbose_name="横版封面大图 URL")),
                ("badge_text", models.CharField(blank=True, max_length=20, verbose_name="视频卡片角标")),
                ("status_text", models.CharField(max_length=50, verbose_name="剧集更新状态")),
                ("is_banner", models.BooleanField(default=False, verbose_name="是否顶部轮播")),
                ("sort_weight", models.IntegerField(default=0, verbose_name="排序权重")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="创建时间")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="更新时间")),
            ],
            options={
                "verbose_name": "影视项目",
                "verbose_name_plural": "影视项目",
                "ordering": ["-sort_weight", "-created_at", "-id"],
            },
        ),
    ]
