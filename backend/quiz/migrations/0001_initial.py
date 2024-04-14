# Generated by Django 3.2.4 on 2021-06-23 05:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1000)),
                ('option_a', models.CharField(max_length=500)),
                ('option_b', models.CharField(max_length=500)),
                ('option_c', models.CharField(max_length=500)),
                ('option_d', models.CharField(max_length=500)),
                ('marks', models.PositiveIntegerField(default=1)),
                ('image', models.ImageField(blank=True, help_text='If any', null=True, upload_to='question')),
                ('answer', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='A', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obtained_marks', models.IntegerField(blank=True, null=True)),
                ('total_marks', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('total_marks', models.PositiveIntegerField(blank=True, null=True)),
                ('total_questions', models.PositiveIntegerField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, max_length=400, null=True)),
                ('questions', models.ManyToManyField(to='quiz.Question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('users_test', models.ManyToManyField(blank=True, null=True, related_name='test_users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserAnswers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_answer', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=2)),
                ('answer', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=2, null=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.question')),
                ('result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='quiz.result')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.test')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='result',
            name='response',
            field=models.ManyToManyField(blank=True, null=True, related_name='user_response', to='quiz.UserAnswers'),
        ),
        migrations.AddField(
            model_name='result',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.test'),
        ),
        migrations.AddField(
            model_name='result',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
