class Validator:
    def __init__(self, payload, rules):
        self.rules = rules
        self.payload = self.clean_payload(payload)
        self.errors = {}

    def apply(self):
        missing_fields = self.required_and_not_sent()
        if missing_fields:
            self.errors = missing_fields

        for key in self.payload.keys():
            if key in self.rules.keys():
                rules = self.rules[key].split('|')
                validation = self.caller(rules, self.payload[key])
                if validation['fails']:
                    self.errors[key] = validation['message']

        if len(self.errors) > 0:
            return self.errors
        else:
            return False

    def caller(self, rules, value):
        if rules[0] == 'string':
            rule_validator = StringValidator(value, rules)
            return rule_validator.validate()

    def required_and_not_sent(self):
        not_sent = {}
        for key in self.rules:
            if 'required' in self.rules[key].split('|'):
                if key not in self.payload:
                    not_sent[key] = 'This field is required'

        return not_sent

    def clean_payload(self, payload):
        clean = {}
        for key in payload:
            if key in self.rules:
                clean[key] = payload[key]

        return clean


class StringValidator:
    def __init__(self, value, rules):
        self.value = value
        self.rules = rules
        self.clean_rules()

    def validate(self):
        if len(self.value) < 1:
            return {
                'fails': True,
                'message': 'Empty string'
            }

        if type(self.value) != str:
            return {
                'fails': True,
                'message': 'No a string'
            }

        if len(self.rules) == 0:
            return {
                'fails': False,
                'message': ''
            }
        else:
            for rule in self.rules:
                description = rule.split(':')
                if description[0] == 'max':
                    rms = RuleMaxString(description, self.value)
                    return rms.validate()

                if description[0] == 'min':
                    rms = RuleMinString(description, self.value)
                    return rms.validate()

                if description[0] == 'type':
                    rms = RuleTypeString(description, self.value)
                    return rms.validate()

    def clean_rules(self):
        if 'required' in self.rules: self.rules.remove('required')
        if 'string' in self.rules: self.rules.remove('string')

class RuleMaxString:
    def __init__(self, description, value):
        self.limit = int(description[1])
        self.value = value
        self.response = {
            'fails': False,
            'message': ''
        }

    def validate(self):
        if len(self.value) > self.limit:
            self.response = {
                'fails': True,
                'message': 'Value needs to be under limit'
            }

        return self.response


class RuleMinString:
    def __init__(self, description, value):
        self.limit = int(description[1])
        self.value = value
        self.response = {
            'fails': False,
            'message': ''
        }

    def validate(self):
        if len(self.value) < self.limit:
            self.response = {
                'fails': True,
                'message': 'Value needs to be bigger'
            }

        return self.response


class RuleTypeString:
    def __init__(self, description, value):
        self.limit = int(description[1])
        self.value = value
        self.response = {
            'fails': False,
            'message': ''
        }

    def validate(self):
        if len(self.value) > self.limit:
            return 'Value needs to be the required type'
        else:
            return 'Value has correct type'
