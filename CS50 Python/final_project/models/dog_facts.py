import logging

from models.base_facts import BaseFacts
from utils.endpoints import BASE_PATH, API_ENDPOINTS


class DogFacts(BaseFacts):
    """Dog facts class."""

    def _extract_dog_facts(self, facts: dict) -> list:
        """Extract facts from API response.

        Args:
            facts (dict): Facts to extract.

        Returns:
            list: Extracted facts.
        """
        return facts["facts"]

    def get_random_n_dog_fact(self, n: int) -> dict | None:
        """Get random dog facts.

        Args:
            n (int): Number of facts to return.

        Returns:
            dict: Random dog facts.
        """
        n_facts_query = f"?number={n}"
        url = BASE_PATH["dog_facts"] + API_ENDPOINTS["d_facts"] + n_facts_query
        try:
            facts = self.call_fact_api(url)
            facts = self._extract_dog_facts(facts)
        except Exception as e:
            logging.error(f"Error: {e}")
            facts = None
        return facts
