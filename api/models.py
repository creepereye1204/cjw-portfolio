from django.db import models
from django.utils import timezone


class SkillSet(models.Model):
    skill_name = models.CharField(max_length=15, primary_key=True)
    badge_file = models.ImageField(upload_to="badge/", null=True, blank=True)

    def __str__(self):
        return self.skill_name


class ProjectInfo(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=30, null=True, blank=True)
    start_at = models.DateField(default=timezone.now)
    end_at = models.DateField(null=True, blank=True)
    describe = models.CharField(max_length=50, null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    readme_file = models.FileField(upload_to="readme/", null=True, blank=True)

    def __str__(self):
        return self.project_name


class SkillMapping(models.Model):
    skill_name = models.ForeignKey("SkillSet", related_name="skill_mappings", on_delete=models.CASCADE)
    project_id = models.ForeignKey("ProjectInfo", related_name="skill_mappings", on_delete=models.CASCADE)

    class Meta:
        unique_together = (("project_id", "skill_name"),)
        verbose_name = "Skill Mapping"
        verbose_name_plural = "Skill Mappings"

    def __str__(self):
        return f"{self.project_id} - {self.skill_name}"


class ContentMetadata(models.Model):
    project_id = models.ForeignKey(
        "ProjectInfo", primary_key=True, related_name="content_metadata", on_delete=models.CASCADE, unique=False
    )
    content = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.content
