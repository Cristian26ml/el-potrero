from django.db import models


class Media(models.Model):
    TIPO_CHOICES = (
        ("foto", "Foto"),
        ("video", "Video"),
    )
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    archivo = models.FileField(upload_to="galeria/", blank=True, null=True)
    url_original = models.URLField(
        "Enlace de Google Drive", blank=True, null=True)
    fecha_subida = models.DateTimeField(auto_now_add=True)

    @property
    def url_directo(self):
        if self.url_original and "drive.google.com" in self.url_original:
            try:
                file_id = self.url_original.split("/d/")[1].split("/")[0]
                if self.tipo == "foto":
                    return f"https://drive.google.com/thumbnail?id={file_id}&sz=w800"
                elif self.tipo == "video":
                    return f"https://drive.google.com/file/d/{file_id}/preview"
            except Exception:
                return self.url_original
        elif self.archivo:
            return self.archivo.url
        return None

    def __str__(self):
        return f"{self.tipo} - {self.fecha_subida}"
