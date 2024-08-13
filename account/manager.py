from django.contrib.auth.base_user import BaseUserManager



class UserManager(BaseUserManager):
    use_in_migrations = True
    def create_user(self, phone_no, email, password=None,**extra_fields):
        if not email:
            raise ValueError("User Must have Email")
        if not phone_no:
            raise ValueError("Phone Number is required")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.phone_no = phone_no
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_superuser(self, phone_no, email,password=None,**extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(phone_no,email,password,**extra_fields)
