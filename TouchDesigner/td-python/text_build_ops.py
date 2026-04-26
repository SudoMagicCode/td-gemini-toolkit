from opDefaults import defaults
import devOpUtils


def build_ops():
    devOpUtils.clear_api_keys()
    devOpUtils.set_defaults()
    op("base_save_for_release").par.Package.pulse()


build_ops()
