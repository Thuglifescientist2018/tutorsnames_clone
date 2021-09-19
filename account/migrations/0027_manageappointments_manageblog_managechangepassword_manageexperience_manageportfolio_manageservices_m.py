# Generated by Django 3.2.6 on 2021-09-06 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0026_alter_fonts_site_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManageAppointments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_booking_info_text', models.TextField(blank=True, null=True)),
                ('saturday', models.BooleanField(blank=True, null=True)),
                ('saturday_start_time', models.CharField(blank=True, max_length=255, null=True)),
                ('saturday_end_time', models.CharField(blank=True, max_length=255, null=True)),
                ('sunday', models.BooleanField(blank=True, null=True)),
                ('sunday_start_time', models.CharField(blank=True, max_length=255, null=True)),
                ('sunday_end_time', models.CharField(blank=True, max_length=255, null=True)),
                ('monday', models.BooleanField(blank=True, null=True)),
                ('monday_start_time', models.CharField(blank=True, max_length=255, null=True)),
                ('monday_end_time', models.CharField(blank=True, max_length=255, null=True)),
                ('tuesday', models.BooleanField(blank=True, null=True)),
                ('tuesday_start_time', models.CharField(blank=True, max_length=255, null=True)),
                ('tuesday_end_time', models.CharField(blank=True, max_length=255, null=True)),
                ('wednesday', models.BooleanField(blank=True, null=True)),
                ('wednesday_start_time', models.CharField(blank=True, max_length=255, null=True)),
                ('wednesday_end_time', models.CharField(blank=True, max_length=255, null=True)),
                ('thursday', models.BooleanField(blank=True, null=True)),
                ('thursday_start_time', models.CharField(blank=True, max_length=255, null=True)),
                ('thursday_end_time', models.CharField(blank=True, max_length=255, null=True)),
                ('friday', models.BooleanField(blank=True, null=True)),
                ('friday_start_time', models.CharField(blank=True, max_length=255, null=True)),
                ('friday_end_time', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ManageBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255, null=True)),
                ('category', models.CharField(choices=[('select', 'Select')], max_length=255, null=True)),
                ('title', models.CharField(max_length=255, null=True)),
                ('slug', models.SlugField(null=True)),
                ('tags', models.CharField(blank=True, max_length=255, null=True)),
                ('post_description', models.TextField(blank=True, null=True)),
                ('upload_image', models.ImageField(upload_to='images/account/blog/')),
            ],
        ),
        migrations.CreateModel(
            name='ManageChangePassword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('old_password', models.CharField(max_length=255, null=True)),
                ('new_password', models.CharField(max_length=255, null=True)),
                ('confirm_new_password', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ManageExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience_name', models.CharField(max_length=255, null=True)),
                ('order', models.IntegerField(blank=True, null=True)),
                ('sub_experience', models.CharField(choices=[('Select_skills', 'Select Experience')], max_length=255, null=True)),
                ('sub_experience_name', models.CharField(max_length=255, null=True)),
                ('company_or_institute_name', models.CharField(max_length=255, null=True)),
                ('enter_date', models.DateField(null=True)),
                ('details', models.TextField(null=True)),
                ('sub_order', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ManagePortfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255, null=True)),
                ('category', models.CharField(choices=[('select', 'Select')], max_length=255, null=True)),
                ('title', models.CharField(max_length=255, null=True)),
                ('details', models.TextField(null=True)),
                ('project_link', models.URLField(null=True)),
                ('upload_image', models.ImageField(upload_to='images/account/portfolio/')),
            ],
        ),
        migrations.CreateModel(
            name='ManageServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=255, null=True)),
                ('service_image', models.ImageField(upload_to='images/account/services/')),
                ('service_details', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ManageSkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=255, null=True)),
                ('order', models.IntegerField(blank=True, null=True)),
                ('service_details', models.TextField(blank=True, null=True)),
                ('skills', models.CharField(choices=[('Select_skills', 'Select Skill')], max_length=255, null=True)),
                ('sub_skill_name', models.CharField(max_length=255, null=True)),
                ('sub_skill_level', models.CharField(choices=[('ten_percent', '10%'), ('twenty_percent', '20%'), ('thirty_percent', '30%'), ('fourty_percent', '40%'), ('fifty_percent', '50%'), ('sixty_percent', '60%'), ('seventy_percent', '70%'), ('eighty_percent', '80%'), ('ninety_percent', '90%'), ('hundred_percent', '100%')], max_length=255, null=True)),
                ('sub_order', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ManageTestimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=255, null=True)),
                ('upload_client_avatar', models.ImageField(upload_to='images/account/testimonial/')),
                ('feedback', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ManageUploadCV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_pdf_file', models.FileField(upload_to='account/pdfs/cvs/')),
            ],
        ),
    ]