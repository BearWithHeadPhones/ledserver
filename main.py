from server import ( service )
from utils.logging import ( init_logger, logger )
from utils.arguments import ( parse_arguments )

if __name__ == '__main__':
    init_logger()
    logger.debug("started")
    arguments = parse_arguments()
    service.serve(arguments.port)
