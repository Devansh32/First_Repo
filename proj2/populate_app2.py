import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','proj2.settings')

import django

django.setup()


import random
from app2.models import User
from faker import Faker

fakegen=Faker()




def populate(N=5):
    for entry in range(N):


        fake_f=fakegen.first_name()
        fake_l=fakegen.last_name()
        fake_id=fakegen.email()


        # webpg=Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]
        user_data =User.objects.get_or_create(f_name=fake_f,l_name=fake_l,email=fake_id)
        # acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]


if __name__=='__main__':


    print("populating")
    populate(20)
    print("complete")
