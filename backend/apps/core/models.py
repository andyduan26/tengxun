from django.db import models


class VideoProject(models.Model):
    CATEGORY_CHOICES = [
        ("电视剧", "电视剧"),
        ("电影", "电影"),
        ("动漫", "动漫"),
        ("综艺", "综艺"),
        ("纪录片", "纪录片"),
        ("短剧", "短剧"),
    ]

    id = models.AutoField(primary_key=True)
    title = models.CharField("标题", max_length=120)
    description = models.TextField("描述/看点")
    cover_image_url = models.URLField("封面大图 URL", max_length=500)
    thumbnail_url = models.URLField("缩略图 URL", max_length=500)
    category = models.CharField("分类", max_length=20, choices=CATEGORY_CHOICES)
    is_vip = models.BooleanField("是否 VIP 权限", default=False)
    sort_weight = models.IntegerField("排序权重", default=0)
    created_at = models.DateTimeField("创建时间", auto_now_add=True)
    updated_at = models.DateTimeField("更新时间", auto_now=True)

    class Meta:
        verbose_name = "视频剧集"
        verbose_name_plural = "视频剧集"
        ordering = ["-sort_weight", "-created_at", "-id"]

    def __str__(self):
        return self.title
