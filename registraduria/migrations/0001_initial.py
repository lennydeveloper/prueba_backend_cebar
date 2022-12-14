# Generated by Django 3.2.5 on 2022-10-03 23:39

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('rol', models.PositiveSmallIntegerField(choices=[(1, 'ADMIN'), (2, 'LIDER')], default=2)),
                ('user_picture', models.BinaryField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Barrio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(db_column='nombre', max_length=50, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'barrio',
                'verbose_name_plural': 'barrios',
                'db_table': 'barrio',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(db_column='nombre', max_length=50, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'departamento',
                'verbose_name_plural': 'departamentos',
                'db_table': 'departamento',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(db_column='nombre', max_length=50, verbose_name='Nombre')),
                ('id_fk_departamento', models.ForeignKey(db_column='id_fk_departamento', on_delete=django.db.models.deletion.DO_NOTHING, to='registraduria.departamento')),
            ],
            options={
                'verbose_name': 'municipio',
                'verbose_name_plural': 'municipios',
                'db_table': 'municipio',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='PuestoVotacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(db_column='nombre', max_length=50, verbose_name='Nombre')),
                ('direccion', models.CharField(db_column='direccion', max_length=100, verbose_name='Direccion')),
                ('id_fk_municipio', models.ForeignKey(db_column='id_fk_municipio', on_delete=django.db.models.deletion.DO_NOTHING, to='registraduria.municipio')),
                ('id_fk_usuario', models.ForeignKey(db_column='id_fk_usuario', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'puesto votaci??n',
                'verbose_name_plural': 'puestos de votaci??n',
                'db_table': 'puesto_votacion',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Votante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(db_column='nombre', max_length=50, verbose_name='Nombre')),
                ('apellido', models.CharField(db_column='apellido', max_length=50, verbose_name='Apellido')),
                ('direccion', models.CharField(db_column='direccion', max_length=100, verbose_name='Direcci??n')),
                ('telefono', models.CharField(db_column='telefono', max_length=10, verbose_name='Tel??fono')),
                ('cedula', models.CharField(db_column='cedula', max_length=10, verbose_name='C??dula')),
                ('mesa', models.IntegerField(blank=True, db_column='mesa', null=True, verbose_name='Mesa')),
                ('id_fk_barrio', models.ForeignKey(db_column='id_fk_barrio', on_delete=django.db.models.deletion.DO_NOTHING, to='registraduria.barrio')),
                ('id_fk_puesto_votacion', models.ForeignKey(db_column='id_fk_puesto_votacion', on_delete=django.db.models.deletion.DO_NOTHING, to='registraduria.puestovotacion')),
                ('id_fk_usuario', models.ForeignKey(db_column='id_fk_usuario', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'votante',
                'verbose_name_plural': 'votantes',
                'db_table': 'votante',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Traza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('descripcion', models.CharField(blank=True, db_column='descripcion', max_length=200, null=True)),
                ('id_fk_usuario', models.ForeignKey(db_column='id_fk_usuario', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('id_fk_votante', models.ForeignKey(db_column='id_fk_votante', on_delete=django.db.models.deletion.DO_NOTHING, to='registraduria.votante')),
            ],
            options={
                'verbose_name': 'traza',
                'verbose_name_plural': 'trazas',
                'db_table': 'traza',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(db_column='nombre', max_length=50, verbose_name='Nombre')),
                ('id_fk_municipio', models.ForeignKey(db_column='id_fk_municipio', on_delete=django.db.models.deletion.DO_NOTHING, to='registraduria.municipio')),
            ],
            options={
                'verbose_name': 'comuna',
                'verbose_name_plural': 'comunas',
                'db_table': 'comuna',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='barrio',
            name='id_fk_comuna',
            field=models.ForeignKey(db_column='id_fk_comuna', on_delete=django.db.models.deletion.DO_NOTHING, to='registraduria.comuna'),
        ),
    ]
