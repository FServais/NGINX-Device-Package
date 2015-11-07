import pprint


def log(msg):
    try:
        from Insieme.Logger import Logger
        Logger.log(Logger.DEBUG, msg)
    except Exception as e:
        import logging
        pprint.pprint(msg)
