# Generated by Django 2.2.16 on 2022-11-29 06:26


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20221128_1957'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenreTitle',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='genretitle', to='reviews.Genre', verbose_name='Жанр')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='genretitle', to='reviews.Title', verbose_name='Произведение')),
            ],
        ),
    ]