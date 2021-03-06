from django.conf.urls import url
from . import views
#for use of job:view_name
app_name='job'

urlpatterns = [
    url(r'^index/', views.index , name="index"),
    url(r'^$', views.LogInView.as_view() , name="login"),
    url(r'^(?P<email>[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4})/(?P<confirmation_code>[0-9]+)$', views.LogInView.as_view() , name="LogIn"),
    url(r'^login/', views.LogInView.as_view() , name="login"),
    url(r'^services/', views.customer_services , name="services"),
    url(r'^jobs/', views.customer_jobs , name="jobs"),
    url(r'^createservices/', views.ServiceRequestView.as_view() , name="createservices"),
    url(r'^signup/', views.SignUp.as_view() , name="signup"),
    url(r'^logout/', views.logout , name="logout"),
    url(r'^my_invoices/', views.my_invoices , name="my_invoices"),
    url(r'^(?P<job_id>[0-9]+)/start_job/$', views.start_job , name="start_job"),
    url(r'^(?P<not_id>[0-9]+)/admin_read/$', views.admin_read , name="admin_read"),
    url(r'^(?P<not_id>[0-9]+)/customer_read/$', views.customer_read , name="customer_read"),
    url(r'^(?P<not_id>[0-9]+)/worker_read/$', views.worker_read , name="worker_read"),
    url(r'^(?P<inv_id>[0-9]+)/customerinvoices/$', views.customer_invoice , name="customerinvoices"),
    url(r'^feedback/', views.FeedbackView.as_view() , name="feedback"),
    url(r'^invoice/', views.invoice_all , name="invoice"),
    url(r'^profile/', views.profile , name="profile"),
    url(r'^(?P<job_id>[0-9]+)/invoices/$', views.invoice_single , name="invoices"),
    url(r'^(?P<job_id>[0-9]+)/viewjob/$', views.view_job , name="viewjob"),
    url(r'^service/$', views.services , name="service"),
    url(r'^all_jobs/$', views.all_jobs , name="all_jobs"),
    url(r'^(?P<job_id>[0-9]+)/all_jobs/$', views.worker_single_job, name="all_jobs"),
    url(r'^(?P<cust_id>[0-9]+)/add_worker/$', views.accept_worker, name="add_worker"),
    url(r'^(?P<cust_id>[0-9]+)/reject_worker/$', views.reject_worker, name="reject_worker"),
    url(r'^(?P<job_id>[0-9]+)/accept_job/$', views.accept_job, name="accept_job"),
    url(r'^(?P<job_id>[0-9]+)/reject_job/$', views.reject_job, name="reject_job"),
    url(r'^jobs_approvel/$', views.worker_job_approvel , name="jobs_approvel"),
    url(r'^(?P<job_id>[0-9]+)/accept/$', views.worker_accept_job, name="accept"),
    url(r'^(?P<job_id>[0-9]+)/reject/$', views.worker_reject_job, name="reject"),
    url(r'^updated_job/$', views.updated_job_approvel, name="updated_job"),
    url(r'^(?P<job_id>[0-9]+)/admin_report_submit/$', views.admin_report_submit, name="admin_report_submit"),
    url(r'^(?P<job_id>[0-9]+)/submit_job/$', views.submit_job.as_view(), name="submit_job"),
    url(r'^(?P<job_id>[0-9]+)/report_job/$', views.report_job.as_view(), name="report_job"),
    url(r'^queries/$', views.queries , name="queries"),
    url(r'^approvel/$', views.job_approvel , name="approvel"),
    url(r'^my_job/$', views.worker_jobs , name="my_job"),
    url(r'^tobeworker/$', views.to_be_worker , name="tobeworker"),
    url(r'^wishes_worker/$', views.wishes_worker , name="wishes_worker"),
    url(r'^custquery/', views.CustQuery.as_view() , name="custquery"),
    url(r'^query/$', views.QueryView , name="query"),
    url(r'^admin_job_report/$', views.admin_job_report , name="admin_job_report"),
    url(r'^worker/$',views.WorkerView,name="worker"),
    url(r'^customer/$',views.CustomerView,name="customer"),
    url(r'^(?P<cust_id>[0-9]+)/customer_data/$',views.customer_data,name="customer_data"),
    url(r'^(?P<work_id>[0-9]+)/worker_data/$',views.worker_data,name="worker_data"),
    url(r'^(?P<ser_id>[0-9]+)/newjob/$',views.NewJob.as_view(),name="newjob"),
    url(r'^(?P<que_id>[0-9]+)/responsequery/$',views.ResponseQuery.as_view(),name="responsequery"),
    url(r'^(?P<ser_id>[0-9]+)/estimate/$',views.Estimate.as_view(),name="estimate"),
    url(r'^job/$',views.JobView,name="job"),
    url(r'^forget_password/', views.Forget_passwordView.as_view(), name="forget_password"),
    url(r'^otp/', views.OtpView.as_view(), name="otp"),
    url(r'^reset_password/', views.Reset_passwordView.as_view(), name="reset_password"),
    url(r'^notifications/$',views.view_notifications,name="notifications"),
    url(r'^(?P<noti_id>[0-9]+)/delete_noti/$', views.delete_notifications, name="delete_noti"),
]
