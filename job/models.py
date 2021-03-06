from django.db import models
from django.utils import timezone
from random import randint

class Customer(models.Model):
    def my_random_key():
        return randint(10**4,10**7)

    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    address=models.TextField(max_length=100)
    landmark = models.CharField(max_length=100)
    id_proof=models.FileField(null=True,blank=True)
    email=models.EmailField(max_length=100,unique=True)
    password=models.CharField(max_length=100)
    forget_password=models.CharField(max_length=100,null=True,blank=True)
    otp_confirm_code=models.IntegerField(default= 0)
    mobile_number=models.IntegerField()
    profile_pic=models.FileField(default="http://180dc.org/wp-content/uploads/2016/08/default-profile.png")
    user_type=models.CharField(max_length=100,default="Customer")
    Reg_date=models.DateTimeField(default=timezone.now)
    confirmation_code=models.IntegerField(default=my_random_key)
    confirm=models.NullBooleanField(default=False)
    wish_to_be_worker=models.BooleanField(default=False)
    # def get_absolute_url(self):
    #     return reverse('index')

    def __str__(self):
        return str(self.first_name)

class Category(models.Model):
    category_name = models.CharField(max_length = 30, default="")

    # def get_absolute_url(self):
    #     return reverse('index')

    def __str__(self):
        return self.category_name

class Worker(models.Model):
    worker=models.ForeignKey(Customer,on_delete=models.CASCADE)
    category_id=models.ForeignKey(Category,on_delete=models.CASCADE)
    status=models.CharField(max_length=10,default="available")

    def __str__(self):
        return str(self.worker)

class Services_Request(models.Model):
    service_request = models.CharField(max_length = 200, default="")
    customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
    service_dateTime = models.DateTimeField(default=timezone.now)
    job_created=models.BooleanField(default=False)
    mark_as_read=models.BooleanField(default=False)
    # def get_absolute_url(self):
    #     return reverse('index')

    def __str__(self):
        return str(self.id)

class Feedback(models.Model):
    customer_id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    feedback_description=models.CharField(max_length=200)

    # def get_absolute_url(self):
    #     return reverse('index')

    def __str__(self):
        return self.feedback_description

class Estimation(models.Model):
    service_id=models.ForeignKey(Services_Request,on_delete=models.CASCADE)
    customer_id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    total_cost=models.FloatField(max_length=100,default=0.0)
    trasportation_charge=models.FloatField(max_length=100)
    visit_charge=models.FloatField(max_length=100)
    extra_cost=models.FloatField(max_length=100,default=0.0,blank=True,null=True)

    # def get_absolute_url(self):
    #     return reverse('index')

    def __str__(self):
        return str(self.id)

class Job(models.Model):
    worker_id=models.ForeignKey(Worker,on_delete=models.CASCADE)
    service_id=models.ForeignKey(Services_Request,on_delete=models.CASCADE)
    customer_id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    Estimate_id=models.ForeignKey(Estimation,on_delete=models.CASCADE)
    job_start_datetime=models.DateTimeField()
    job_end_datetime=models.DateTimeField(null=True,blank=True)
    location=models.CharField(max_length = 100,null=True,blank=True)
    job_description=models.CharField(max_length=200)
    job_status=models.CharField(max_length=20, default="pending")
    job_report=models.CharField(max_length=200,null=True,blank=True)
    customer_approvel=models.BooleanField(default=False)
    worker_approvel=models.CharField(max_length=10,default=0)
    report_customer_approvel=models.BooleanField(default=True)
    mark_as_read=models.BooleanField(default=False)
    report_admin_approvel=models.BooleanField(default=True)
    # def get_absolute_url(self):
    #     return reverse('index')

    def __str__(self):
        return self.job_description

class Invoice(models.Model):
    service_id=models.ForeignKey(Services_Request,on_delete=models.CASCADE)
    customer_id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    job_id=models.ForeignKey(Job,on_delete=models.CASCADE,default=None)
    job_datetime=models.DateField()
    total_cost=models.FloatField(max_length=100)
    trasportation_charge=models.FloatField(max_length=100)
    visit_charge=models.FloatField(max_length=100)
    extra_cost=models.FloatField(max_length=100)
    invoice_status=models.CharField(max_length=20, default="pending")

class Query(models.Model):
    customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
    query_dateTime = models.DateTimeField(default=timezone.now)
    query_description = models.CharField(max_length = 500)
    status = models.CharField(max_length = 20 ,default="pending")
    query_response=models.CharField(max_length = 500,default="",null=True,blank=True)

    def __str__(self):
        return self.query_description+ " " +self.status

class Notifications(models.Model):
    sender=models.ForeignKey(Customer,on_delete=models.CASCADE)
    reciever=models.CharField(max_length = 10,default=1)
    reciever_type=models.CharField(max_length = 10)
    target=models.CharField(max_length = 20)
    message=models.CharField(max_length = 100)
    mark_as_read=models.BooleanField(default=False)
    noti_date=models.DateTimeField(default=timezone.now)