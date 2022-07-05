# Generated by Django 3.2.5 on 2022-07-05 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registraduria', '0004_auto_20220705_0034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='votante',
            name='id_fk_lider',
        ),
        migrations.AddField(
            model_name='votante',
            name='id_fk_usuario',
            field=models.ForeignKey(db_column='id_fk_usuario', default=2, on_delete=django.db.models.deletion.PROTECT, to='registraduria.user'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Lider',
        ),
    ]