class IdDict(dict):
    cls = dict


class DocumentBase(object):
    _field_definitions = None
    _mongo_fields = ("_id",)

    def __init__(self, base_data, parent=None):
        self._assert_validation(base_data)
        self._set_fields(base_data)
        self._parent = parent

    def _set_fields(self, base_data):
        for key, data in base_data.items():
            self._set_field(data, key)

    def _set_field(self, data, key):
        property_class = self._field_definitions.get(key)

        if self._set_to_default(data, key, property_class):
            self.set_field_to_property_unmodified(data, key)

        elif property_class is None:
            raise Exception("Missing prop_class for: '{}'".format(key))

        elif self._property_is_cls_obj_list(data, property_class):
            property_value = []
            for item in data:
                item_value = self._cast_or_none(property_class, item)
                if item_value is not None:
                    property_value.append(item_value)
            setattr(self, key, property_value)

        elif self._is_id_dict(property_class):
            self._set_id_dict_value(data, key, property_class)

        else:
            property_value = self._cast_or_none(property_class, data)
            setattr(self, key, property_value)

    @staticmethod
    def _is_id_dict(property_class):
        return issubclass(property_class, IdDict)

    def _set_id_dict_value(self, data, key, property_class):
        property_value = {}
        item_prop_cls = property_class.cls
        for k, item in data.items():
            property_value[k] = self._cast_or_none(item_prop_cls, item)
        setattr(self, key, property_value)

    @staticmethod
    def _property_is_cls_obj_list(data, property_class):
        return property_class is not list and issubclass(data.__class__, list)

    def _set_to_default(self, data, key, property_class):
        return key in self._mongo_fields or property_class is data.__class__

    def set_field_to_property_unmodified(self, data, key):
        setattr(self, key, data)

    def _cast_or_none(self, cls, data):
        if data is None:
            return None
        try:
            args = [data]
            if issubclass(cls, DocumentBase):
                args.append(self)
            return cls(*args)
        except TypeError as e:
            # TODO: some concept of nullables
            pass  # print("Warning: could not convert {}: {}".format(cls.__name__ if cls else "NONE?", e))

    def _assert_validation(self, base_data):
        if self._field_definitions is None:
            raise Exception("Classes that derive from DocumentBase must implement '_field_definitions'")
        for key in self._field_definitions.keys():
            if key not in base_data:
                message = "Key '{}'' missing from data".format(key)
                raise Exception(message)

    @property
    def data(self):
        return {key: self._to_data(getattr(self, key)) for key in self._field_definitions.keys()}

    def _to_data(self, obj):
        obj_class = obj.__class__
        if issubclass(obj_class, DocumentBase):
            return obj.data
        elif issubclass(obj.__class__, dict):
            if obj:
                obj_cls = list(obj.values())[0].__class__
                if issubclass(obj_cls, DocumentBase):
                    return {k: self._to_data(v) for k, v in obj.items()}
        elif issubclass(obj_class, list):
            results = []
            for item in obj:
                result = self._to_data(item)
                if result is not None:
                    results.append(result)
            return results
        return obj

    def _find(self, cls_name):
        obj = self
        while obj is not None:
            obj = obj._parent
            if obj.__class__.__name__ is cls_name:
                return obj
