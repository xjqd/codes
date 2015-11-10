#!/bin/bash
from oslo_config import cfg

# Register options for the service
OPTS = [
    cfg.IntOpt('port',
               default=8777,
               deprecated_name='metering_api_port',
               deprecated_group='DEFAULT',
               help='The port for the ceilometer API server.',
               ),
    cfg.StrOpt('host',
               default='0.0.0.0',
               help='The listen IP for the ceilometer API server.',
               ),
]

CONF = cfg.CONF
import pdb
pdb.set_trace()
opt_group = cfg.OptGroup(name='api',
                         title='Options for the ceilometer-api service')
CONF.register_group(opt_group)
CONF.register_opts(OPTS, opt_group)
