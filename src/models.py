from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
RELATIONSHIP_STATUS = (
    ("Single", "Single"),
    ("Commited", "Commited"),
    ("Divorcee", "Divorcee"),
    ("Married", "Married"),
    ("Widow", "Widow"),
    ("Engaged", "Engaged"),
    ("Other", "Other")
)
LOCATION = (
    ("Noida", "Noida"),
    ("Delhi", "Delhi"),
    ('Mumbai', 'Mumbai'),
    ('Banglore', 'Banglore'),
    ('Gurgaon', 'Gurgaon'),
    ('Chennai', 'Chennai'),
    ('Kerala', 'Kerala'),
    ('Gujrat', 'Gujrat'),
    ('Ahmedabad', 'Ahmedabad')
)
PROFESSION = (
    ("IT Support", "IT Support"),
    ("Software Developer", "Software Developer"),
    ('Model', 'Model'),
    ('Director', 'Director'),
    ('Fitness Trainer', 'Fitness Trainer'),
    ('Doctor', 'Doctor'),
    ('Actor', 'Actor'),
    ('Nutritionist', 'Nutritionist'),
    ('Human Resource', 'Human Resource')
)
QUALIFICATION = (
    ('Matriculate', 'Matriculate'),
    ('Intermediate', 'Intermediate'),
    ("Bachelor's", "Bachelor's"),
    ("Matser's", "Matser's"),
    ("Doctrate", "Doctrate"),
)

COLLEGES = (("IIT", "IIT"),
            ("IIIT", "IIT"),
            ("NIT", "NIT"),
            ("IISC", "IISC"),
            ("BITS PILANI", "BITS PILANI"),
            ("AIIMS", "AIIMS"),
            ("IIM", "IIM")
            )

UNIVERSITY = (
    ("DU", "DU"),
    ("JNU", "JNU"),
    ("BHU", "BHU"),
    ("CCSU", "CCSU"),
    ("IPU", "IPU"),
    ("AKTU", "AKTU"),
)

PREFRENCE_FIRST_DATE = (
    ("Tea", "Tea"),
    ("Coffee", "Coffee"),
    ("Soft Drinks", "Soft Drinks"),
    ("Beer", "Beer"),
    ("Wine", "Wine"),
    ("Whisky", "Whisky")
)

BOOL_CHOICES = (('Yes', 'Yes'), ('No', 'NO'))

GENDER = (('Male', 'Male'), ('Female', 'Female'), ('Custom', 'Custom'))


class RegisterUser(models.Model):
    email = models.EmailField(default='test@maclo.com')
    phone_number = models.CharField(default='00000', max_length=12)
    first_name = models.CharField(default='maclo', max_length=100)
    last_name = models.CharField(default='app', max_length=100)
    gender = models.CharField(choices=GENDER, default='Male', max_length=20, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    job_profile = models.CharField(max_length=100, null=True, blank=True)
    company_name = models.CharField(max_length=200, null=True, blank=True)
    qualification = models.CharField(
        default="Bachelor's", choices=QUALIFICATION, max_length=100, null=True, blank=True)
    relationship_status = models.CharField(
        default='Single', choices=RELATIONSHIP_STATUS, max_length=100, null=True, blank=True)
    interests = models.CharField(default='Reading Books', max_length=500)
    fav_quote = models.CharField(default='MY Fav QUOTE', max_length=1000)
    religion = models.CharField(default='atheist', max_length=100, null=True, blank=True)
    body_type = models.CharField(default='slim', max_length=100)
    created_by = models.DateTimeField(auto_now_add=True)
    verified = models.CharField(default='NO', choices=BOOL_CHOICES, max_length=10)
    fb_signup = models.CharField(default='No', choices=BOOL_CHOICES, max_length=10)
    insta_connect = models.CharField(default='NO', choices=BOOL_CHOICES, max_length=10)
    pic_1 = models.ImageField(null=True, blank=True)
    pic_2 = models.ImageField(null=True, blank=True)
    pic_3 = models.ImageField(null=True, blank=True)
    pic_4 = models.ImageField(null=True, blank=True)
    pic_5 = models.ImageField(null=True, blank=True)
    pic_6 = models.ImageField(null=True, blank=True)
    pic_7 = models.ImageField(null=True, blank=True)
    pic_8 = models.ImageField(null=True, blank=True)
    pic_9 = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.phone_number


class UserDetail(models.Model):
    bio = models.CharField(default='sdjhkfsjh', max_length=600)
    phone_number = models.ForeignKey(RegisterUser, on_delete=models.CASCADE, null=True, blank=True)
    living_in = models.CharField(
        default='Delhi', choices=LOCATION, max_length=100)
    profession = models.CharField(
        default="Model", choices=PROFESSION, max_length=100)
    college_name = models.CharField(
        default='IIT', choices=COLLEGES, max_length=100)
    university = models.CharField(
        default='DU', choices=UNIVERSITY, max_length=200)
    personality = models.CharField(default=None, max_length=500)

    preference_first_date = models.CharField(
        default='Tea', choices=PREFRENCE_FIRST_DATE, max_length=150)
    fav_music = models.CharField(default=None, max_length=500)
    travelled_place = models.CharField(default=None, max_length=500)
    once_in_life = models.CharField(default=None, max_length=500)
    exercise = models.CharField(default='NO', choices=BOOL_CHOICES, max_length=10)
    looking_for = models.CharField(default="relationship", max_length=500)
    fav_food = models.CharField(default=None, max_length=500)
    fav_pet = models.CharField(default=None, max_length=100)
    smoke = models.CharField(default='No', choices=BOOL_CHOICES, max_length=10)
    drink = models.CharField(default='No', choices=BOOL_CHOICES, max_length=10)


class UserInstagramPic(models.Model):
    phone_number = models.ForeignKey(RegisterUser, default=1, on_delete=models.CASCADE)
    username = models.CharField(default='username', max_length=100)
    password = models.CharField(default='password', max_length=100)
    insta_pic_1 = models.ImageField(null=True, blank=True)
    insta_pic_2 = models.ImageField(null=True, blank=True)
    insta_pic_3 = models.ImageField(null=True, blank=True)
    insta_pic_4 = models.ImageField(null=True, blank=True)
    insta_pic_5 = models.ImageField(null=True, blank=True)
    insta_pic_6 = models.ImageField(null=True, blank=True)
    insta_pic_7 = models.ImageField(null=True, blank=True)
    insta_pic_8 = models.ImageField(null=True, blank=True)
    insta_pic_9 = models.ImageField(null=True, blank=True)
    insta_pic_10 = models.ImageField(null=True, blank=True)


class UserSettings(models.Model):
    phone_number = models.ForeignKey(RegisterUser, on_delete=models.CASCADE, null=True, blank=True)
    location = models.CharField(default='Delhi', choices=LOCATION, max_length=100)
    max_distance = models.IntegerField(default=10)
    age_range = models.IntegerField(default='18', validators=[MinValueValidator(18), MaxValueValidator(130)])
    show_me_on_app = models.CharField(choices=BOOL_CHOICES, max_length=100)


class MatchedUser(models.Model):
    liked_by = models.ManyToManyField(RegisterUser, default=1, related_name='liked_by')
    super_liked_by = models.ManyToManyField(RegisterUser, default=1, related_name='superliked_by')
    liked_by_me = models.ManyToManyField(RegisterUser, default=1, related_name='liked_by_me')
    super_liked_by_me = models.ManyToManyField(RegisterUser, default=1, related_name='superliked_by_me')

    def __str__(self):
        return str(self.id)


class RequestMeeting(models.Model):
    phone_number = models.ForeignKey(RegisterUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class ScheduleMeeting(models.Model):
    phone_number = models.ForeignKey(RegisterUser, on_delete=models.CASCADE)
    meeting_date = models.DateField()
    meeting_time = models.TimeField()
    venue = models.TextField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class InAppNotification(models.Model):
    from_user_id = models.ForeignKey(UserDetail, on_delete=models.CASCADE, related_name='from_user')
    from_user_name = models.CharField(default='From User', max_length=250)
    to_user_id = models.ForeignKey(UserDetail, on_delete=models.CASCADE, related_name='to_user')
    to_user_name = models.CharField(default='To user name', max_length=200)
    notification_type = models.CharField(default='Notification type', max_length=200)
    notification_title = models.CharField(default='Notification Title', max_length=200)
    notification_body = models.TextField()


class Feedback(models.Model):
    phone_number = models.ForeignKey(RegisterUser, on_delete=models.CASCADE)
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class ContactUs(models.Model):
    phone_number = models.BigIntegerField(default='+9199999')
    email = models.EmailField(default='support@maclo.com', max_length=100)


class AboutUs(models.Model):
    about_us = models.TextField()
