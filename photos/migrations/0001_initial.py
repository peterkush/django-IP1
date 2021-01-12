
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cate', models.CharField(choices=[('Flowers', 'Flowers'), ('Articles', 'Articles'), ('Animals', 'Animals'), ('People', 'People')], max_length=255)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locs', models.CharField(choices=[('Nairobi', 'Nairobi'), ('Turkey', 'Turkey'), ('Nakuru', 'Nakuru'), ('Paris', 'Paris'), ('China', 'China'), ('Mombasa', 'Mombasa')], max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Location',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('image', models.ImageField(upload_to='images/')),
                ('description', models.TextField()),
                ('image_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.Category')),
                ('image_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.Location')),
            ],
        ),
    ]
