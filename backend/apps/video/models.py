from django.db import models


class VideoProject(models.Model):
    CATEGORY_CHOICES = [
        ("电视剧", "电视剧"),
        ("综艺", "综艺"),
        ("电影", "电影"),
        ("动漫", "动漫"),
        ("少儿", "少儿"),
        ("纪录片", "纪录片"),
    ]

    id = models.AutoField(primary_key=True)
    title = models.CharField("视频/剧集标题", max_length=120)
    subtitle = models.CharField("主视觉看点或金句", max_length=200)
    category = models.CharField("主分类", max_length=20, choices=CATEGORY_CHOICES)
    tags = models.CharField("细分标签", max_length=200, help_text="用空格隔开，例如：东方玄幻 东方仙侠 逆袭")
    cover_image = models.URLField("横版封面大图 URL", max_length=500)
    badge_text = models.CharField("视频卡片角标", max_length=20, blank=True)
    status_text = models.CharField("剧集更新状态", max_length=50)
    is_banner = models.BooleanField("是否顶部轮播", default=False)
    sort_weight = models.IntegerField("排序权重", default=0)
    created_at = models.DateTimeField("创建时间", auto_now_add=True)
    updated_at = models.DateTimeField("更新时间", auto_now=True)

    class Meta:
        verbose_name = "影视项目"
        verbose_name_plural = "影视项目"
        ordering = ["-sort_weight", "-created_at", "-id"]

    def __str__(self):
        return self.title
