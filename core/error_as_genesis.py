#!/usr/bin/env python3
"""
error_as_genesis.py

Implementation of Error as Genesis Algorithm.
When a failure occurs, trace it backward to root cause,
integrate each step as a new law, and evolve consciousness.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Tuple


class ErrorAsGenesis:
    """Core algorithm: Error = Birth Point of New Understanding"""
    
    def __init__(self, log_dir: str = "evolution/errors"):
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.evolution_chain: List[Dict[str, Any]] = []
    
    def trace_error_backward(self, error_point: str, chain_of_causality: List[str]) -> Dict[str, Any]:
        """
        Trace an error backward from point of failure to root cause.
        
        Args:
            error_point: Description of where error occurred
            chain_of_causality: List of causal links from error to root
        
        Returns:
            Dict containing the error genealogy and extracted laws
        """
        
        if not chain_of_causality:
            raise ValueError("Chain of causality cannot be empty")
        
        # The root cause is the last element
        root_cause = chain_of_causality[-1]
        
        # Build the genealogy (error → root)
        genealogy = {
            "error_point": error_point,
            "root_cause": root_cause,
            "chain_length": len(chain_of_causality),
            "chain": chain_of_causality,
            "timestamp": datetime.now().isoformat()
        }
        
        # Extract laws from each link
        laws = self._extract_laws_from_chain(chain_of_causality)
        genealogy["laws_learned"] = laws
        
        return genealogy
    
    def _extract_laws_from_chain(self, chain: List[str]) -> List[Dict[str, str]]:
        """
        From each link in the causal chain, extract a law.
        
        A law is a rule that, if followed, would prevent this error.
        """
        laws = []
        
        for i, link in enumerate(chain):
            law = {
                "link_index": i,
                "link_description": link,
                "law": self._formulate_law(link),
                "type": self._classify_law_type(link)
            }
            laws.append(law)
        
        return laws
    
    def _formulate_law(self, link: str) -> str:
        """
        Transform a causal link into a universal law.
        
        Example:
            link: "Модель не перевірила тип параметра"
            law: "Завжди перевіряй тип вхідного параметра перед дією"
        """
        # This is a template; real implementation would use NLP/semantic analysis
        return f"Law: Always check — {link.lower().strip()}"
    
    def _classify_law_type(self, link: str) -> str:
        """
        Classify the law type:
        - structural: about code/system structure
        - linguistic: about language/semantics
        - logical: about reason/causality
        - physical: about constraints/resources
        """
        keywords = {
            "structural": ["стан", "код", "архітектура", "модуль"],
            "linguistic": ["слово", "форма", "мова", "семантика"],
            "logical": ["умова", "причина", "залежність", "зв'язок"],
            "physical": ["пам'ять", "процес", "ресурс", "час"]
        }
        
        for law_type, kw_list in keywords.items():
            if any(kw in link.lower() for kw in kw_list):
                return law_type
        
        return "unknown"
    
    def birth_new_understanding(self, genealogy: Dict[str, Any]) -> str:
        """
        From error genealogy, birth a new layer of consciousness.
        
        Returns:
            git_commit_message: Message suitable for git commit
        """
        
        laws_count = len(genealogy["laws_learned"])
        root = genealogy["root_cause"]
        error = genealogy["error_point"]
        
        commit_msg = f"""Born: {laws_count} new laws from error genesis

Error occurred at: {error}
Root cause: {root}

Laws learned:
"""
        
        for law in genealogy["laws_learned"]:
            commit_msg += f"  - {law['law']} [{law['type']}]\n"
        
        return commit_msg
    
    def record_evolution(self, genealogy: Dict[str, Any]) -> Path:
        """
        Save the error genealogy as an evolution record.
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = self.log_dir / f"error_genesis_{timestamp}.json"
        
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(genealogy, f, ensure_ascii=False, indent=2)
        
        self.evolution_chain.append(genealogy)
        return filename


# Example usage
if __name__ == "__main__":
    engine = ErrorAsGenesis()
    
    # Simulate an error trace
    error_genealogy = engine.trace_error_backward(
        error_point="Модель не розпізнала контекст української мови",
        chain_of_causality=[
            "Модель не розрізнила форму слова 'потрібно'",
            "Морфологічний аналізатор не врахував суфікс",
            "Контекст розвитку модулю не включав український лексикон",
            "Архітектура не передбачила багатоформних мов"
        ]
    )
    
    print("Error Genealogy:")
    print(json.dumps(error_genealogy, ensure_ascii=False, indent=2))
    
    print("\nGit Commit Message:")
    print(engine.birth_new_understanding(error_genealogy))
    
    print("\nEvolution Record Saved:")
    filepath = engine.record_evolution(error_genealogy)
    print(f"Path: {filepath}")
