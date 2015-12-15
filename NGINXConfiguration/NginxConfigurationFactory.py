from NGINXConfiguration.NginxConfiguration import NginxConfiguration
from NGINXConfiguration.NginxBackend import NginxBackend
from NGINXConfiguration.NginxFrontend import NginxFrontend

__author__ = 'Fabrice Servais'


class NginxConfigurationFactory:

    @classmethod
    def from_API_configuration(cls, api_configuration):
        if api_configuration.get_type() == 0:
            return cls.from_configurations(api_configuration.get_value())

        return [], {}

    @classmethod
    def from_configurations(cls, configurations):
        """

        :param configurations: Type list<API.Configuration>
        :return:
        """
        # keys: {"configuration1": {'frontendCfg': nameOfFrontendConfiguration, 'upstreamCfg': nameOfBackendConfiguration}, ...}
        keys = {}

        frontend_configurations = {}
        backend_configurations = {}

        nginx_final_configurations = []

        management_configuration = {}
        for configuration in configurations:
            # Configurations of vnsMFunc
            if configuration.get_type() == 1:
                function_load_balancer = configuration.get_value()[0]  # (3,....) -> ...

                # Get the configurations
                func_configurations = function_load_balancer.get_value_by_key('configuration')  # (4, 'configuration', 'Configuration') -> ...

                for func_cfg in func_configurations:

                    configs_folders = func_cfg.get_value_by_type(4)
                    configs_params = func_cfg.get_value_by_type(5)

                    frontend_configs = []
                    backend_configs = []

                    enabled = False

                    for folder in configs_folders:
                        if folder.get_key() == 'frontendServerCfg':
                            front_rel = folder.get_value()
                            if front_rel is None:
                                continue

                            front_cfg_name = front_rel[0].get_target()

                            if front_cfg_name is None:
                                continue

                            frontend_configs.append(front_cfg_name)

                        elif folder.get_key() == 'upstreamCfg':
                            back_rel = folder.get_value()
                            if back_rel is None:
                                continue

                            back_cfg_name = back_rel[0].get_target()

                            if back_cfg_name is None:
                                continue

                            backend_configs.append(back_cfg_name)

                    for param in configs_params:
                        if param.key == 'enabled':
                            enabled = (param.get_value().lower() == "true")

                    keys[func_cfg.get_name()] = {'frontendCfgs': frontend_configs, 'upstreamCfgs': backend_configs, 'enabled': enabled}

                # Get the management configuration
                mgmt_cfg_value = function_load_balancer.get_value_by_key('management')

                if not mgmt_cfg_value:
                    continue

                # Get the HTTPS parameter
                management_configuration['https'] = False
                https_cfg = mgmt_cfg_value[0].get_value()

                if not https_cfg:
                    continue

                https_val = https_cfg[0].get_value()

                if not https_val:
                    continue

                management_configuration['https'] = (str(https_val.lower()) == 'true')


            # Configurations of vnsMDevCfg
            elif configuration.get_type() == 4:
                nginx_config_type_class = None
                if configuration.get_key() == 'frontendServer':
                    frontend_configurations[configuration.get_name()] = NginxFrontend.from_configuration(configuration.get_value())
                elif configuration.get_key() == 'upstream':
                    backend_configurations[configuration.get_name()] = NginxBackend.from_configuration(configuration.get_value())

        for config_name, config_value_names in keys.iteritems():
            frontend_names = config_value_names["frontendCfgs"]
            backend_names = config_value_names["upstreamCfgs"]

            frontends = list(map(lambda cfg_name: frontend_configurations[cfg_name], frontend_names))
            backends = list(map(lambda cfg_name: backend_configurations[cfg_name], backend_names))

            nginx_final_configurations.append(NginxConfiguration(frontends, backends, config_name, config_value_names["enabled"]))

        return nginx_final_configurations, management_configuration
