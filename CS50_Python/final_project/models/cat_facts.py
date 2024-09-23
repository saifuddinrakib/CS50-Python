
import random
import logging

from models.base_facts import BaseFacts
from utils.endpoints import BASE_PATH, API_ENDPOINTS


class CatFacts(BaseFacts):
    """Cat facts class."""

    def _extract_cat_facts(self, facts: dict) -> list:
        """Extract facts from API response.

        Args:
            facts (dict): Facts to extract.

        Returns:
            list: Extracted facts.
        """
        return [fact["text"] for fact in facts]

    def get_random_n_cat_fact(self, n: int) -> dict | None:
        """Get random cat facts.

        Args:
            n (int): Number of facts to return.

        Returns:
            dict: Random cat facts.
        """
        url = BASE_PATH["cat_facts"] + API_ENDPOINTS["c_facts"]
        try:
            facts = self.call_fact_api(url)
            facts = self._extract_cat_facts(facts)
        except Exception as e:
            logging.error(f"Error: {e}")
            facts = None
        return random.sample(facts, n)
