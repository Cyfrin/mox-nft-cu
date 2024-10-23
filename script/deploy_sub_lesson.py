from src.sub_lesson import call_anything, encoding, raw_call


def deploy_call_anything():
    return call_anything.deploy()


def deploy_encoding():
    return encoding.deploy()


def deploy_raw_call():
    return raw_call.deploy()


def moccasin_main():
    deploy_call_anything()
    deploy_encoding()
    deploy_raw_call()
