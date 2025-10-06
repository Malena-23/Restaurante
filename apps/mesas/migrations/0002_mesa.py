import django.db.models.deletion
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('mesas', '0001_initial'),
    ] 
    
    operations = [
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('capacidad', models.IntegerField(default=4)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mesas', to='mesas.mesasestado')),
            ],
        ),
    ]