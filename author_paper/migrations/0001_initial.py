# Generated by Django 2.1 on 2018-08-05 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('given_name', models.CharField(max_length=45)),
                ('surname', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=191)),
                ('url', models.CharField(max_length=191)),
            ],
        ),
        migrations.CreateModel(
            name='Author_Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='author_paper.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.CharField(max_length=23, primary_key=True, serialize=False)),
                ('title', models.TextField(blank=True, null=True)),
                ('cover_date', models.DateTimeField(auto_now_add=True)),
                ('url', models.CharField(max_length=191, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=191)),
            ],
        ),
        migrations.AddField(
            model_name='author_paper',
            name='paper_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='author_paper.Paper'),
        ),
        migrations.AddField(
            model_name='author',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='author_paper.University'),
        ),
    ]