
from django.db import models
    
class customer(models.Model):
        first_name=models.CharField(max_length=20)
        last_name=models.CharField(max_length=20)
        adhar_no=models.CharField(max_length=12,unique=True)
        id1=models.IntegerField(unique=True)

        def save(self):
                if not self.id1:
                        prev_customer = customer.objects.order_by('id1').first()

                        if prev_customer:
                            self.id1 = prev_customer.id1 + 1
            
           
                        else:
                             self.id1 = 8000
                super(customer,self).save()

        
        def __str__(self):
            return f"{self.first_name} {self.last_name}"