from django.db import models

# Create your models here.
class approvals(models.Model):
    gender_choices=(
        ('Male','Male'),
        ('Female','Female')
    )
    married_choices=(
        ('Yes','Yes'),
        ('No','No')
    )
    graduated_choices=(
        ('graduated','graduated'),
        ('not_graduated','not_graduated')
    )
    selfemployed_choices=(
        ('yes','yes'),
        ('no','no')
    )
    property_choices=(
        ('rural','rural'),
        ('semiurban','semiurban'),
        ('urban','urban')
    )
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    dependants=models.IntegerField(default=0)
    applicantincome=models.IntegerField(default=0)
    coapplicantincome=models.IntegerField(default=0)
    loanamt=models.IntegerField(default=0)
    credithistory=models.IntegerField(default=0)
    gender=models.CharField(max_length=15,choices=gender_choices)
    married=models.CharField(max_length=15,choices=married_choices)
    graduatededucation=models.CharField(max_length=15,choices=graduated_choices)
    selfemployed=models.CharField(max_length=15,choices=selfemployed_choices)
    area=models.CharField(max_length=15,choices=property_choices)

    def __str__(self):
        return '{} {}'.format(self.firstname,self.lastname)
    
    class Meta:
        verbose_name_plural = "approvals"
    