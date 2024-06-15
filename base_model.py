from datetime import datetime
import uuid

class BaseModel:
    """The base model class for your freight application."""

    def __init__(self, *args, **kwargs):
        """
        Initializes a base model instance.

        Args:
            *args: Variable-length argument list (unused in this case).
            **kwargs: Keyword argument dictionary containing model attributes.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            self.created_at = datetime.utcnow() if kwargs.get("created_at", None) is None else datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = datetime.utcnow() if kwargs.get("updated_at", None) is None else datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
            if not getattr(self, "id", None):
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def __str__(self):
        """
        Returns a string representation of the base model instance.
        """
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the `updated_at` attribute with the current datetime and saves the instance to storage.

        This assumes the existence of a storage module (not included here) that handles
        database interaction and persists model data.

        Raises:
            NotImplementedError: If the storage module is not implemented.
        """
        self.updated_at = datetime.utcnow()
        try:
            from storage import storage
            storage.new(self)
            storage.save()
        except ImportError:
            raise NotImplementedError("storage module not implemented")

    def to_dict(self):
        """
        Returns a dictionary representation of the base model instance.

        Excludes sensitive attributes like password from the dictionary.
        """
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = new_dict["created_at"].strftime("%Y-%m-%dT%H:%M:%S.%f")
        new_dict["updated_at"] = new_dict["updated_at"].strftime("%Y-%m-%dT%H:%M:%S.%f")
        new_dict["__class__"] = self.__class__.__name__
        del new_dict["_sa_instance_state"]  # Remove SQLAlchemy internal state
        if "password" in new_dict:
            del new_dict["password"]  # Exclude password for security
        return new_dict

    def delete(self):
        """
        Deletes the current instance from the storage.

        This assumes the existence of a storage module that handles
        database interaction and record deletion.

        Raises:
            NotImplementedError: If the storage module is not implemented.
        """
        try:
            from storage import storage
            storage.delete(self)
        except ImportError:
            raise NotImplementedError("storage module not implemented")
