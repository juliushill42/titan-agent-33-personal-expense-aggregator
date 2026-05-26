#  2026 Julius Cameron Hill / TitanU AI LLC. All rights reserved. Patent pending JCH-2026-001.
from agents.core.base_agent import BaseAgent
from typing import Dict, Any
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PersonalExpenseAggregatorAgent(BaseAgent):
    def __init__(self):
        super().__init__("agent-33-Personal-Expense-Aggregator") 
    def aggregate_expenses(self, statements: list) -> dict:
        logger.info("Aggregating disparate downstream personal ledger input streams.")
        return {"processed_items_count": len(statements), "net_allocation": sum(float(item.get("amount", 0.0)) for item in statements)}

    def categorize_spending(self, statements: list) -> dict:
        logger.info("Applying multi-tier operational classification tags to raw debit lines.")
        mapping = {}
        for item in statements:
            cat = item.get("category", "unclassified")
            mapping[cat] = mapping.get(cat, 0.0) + float(item.get("amount", 0.0))
        return {"categorical_footprint": mapping}
        for attr in dir(self):
            if callable(getattr(self, attr)) and not attr.startswith("__") and attr not in ["execute", "register_tool", "call_tool", "success", "failure", "telemetry"]:
                self.register_tool(attr, getattr(self, attr))

    def execute(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        try:
            logger.info(f"Processing structural execution matrix thread for agent: {self.name}") 
            statements = payload.get("statements", [])
            totals = self.call_tool("aggregate_expenses", statements=statements)
            categories = self.call_tool("categorize_spending", statements=statements)
            return self.success({"financial_totals": totals, "segmentation": categories})
        except Exception as e:
            logger.error(f"Execution matrix breakdown inside agent {self.name}: {str(e)}")
            return self.failure(str(e))
