import logging
import sys

# Configuration optimisée du logging
logging.basicConfig(
    level=logging.INFO,  # Changé de DEBUG à INFO pour de meilleures performances
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)  # Niveau explicite
