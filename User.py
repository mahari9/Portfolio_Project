from datetime import datetime
import uuid
from passlib.hash import bcrypt  # Secure password hashing

class User(BaseModel):
    username = str
    email = str
    phone_number = str
    password = str
    is_carrier = bool
    business_license = str  # Optional, only for carriers
    truck_plate_number = str  # Optional, only for carriers

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.id:
            self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def set_password(self, password):
        self.password = bcrypt.hash(password)  # Hash password securely

    def verify_password(self, password):
        return bcrypt.verify(password, self.password)  # Securely compare passwords

    def to_dict(self):
        user_dict = super().to_dict()
        user_dict.pop('password', None)  # Exclude password from serialized data
        return user_dict
