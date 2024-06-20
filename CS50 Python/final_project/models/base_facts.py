import json
import requests
import logging


class BaseFacts:
    """Base facts class."""

    def call_fact_api(self, url: str) -> dict:
        """Call fact api.

        Args:
            None

        Returns:
            dict: Facts.
        """
        logging.info("Calling facts api...")
        facts = requests.get(url)
        try:
            facts.raise_for_status()
        except requests.exceptions.HTTPError as e:
            error_response = json.loads(e.response.text)
            logging.error(f"Error: {error_response['message']}")
        return facts.json()
