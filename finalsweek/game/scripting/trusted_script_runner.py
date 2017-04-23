class TrustedScriptRunner(object):
    @staticmethod
    def exec(script, _locals, _globals):
        exec(script, _locals, _globals)


