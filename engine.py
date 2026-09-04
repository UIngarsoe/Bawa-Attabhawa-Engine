#!/usr/bin/env python3
"""
Bawa-Attabhawa-Engine
Core Processing Module for Transmitting Practical Philosophy to Seekers of Direct Reality
"""

import json
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import List, Dict, Any

@dataclass
class EpisodeSpec:
    episode_number: int
    title: str
    existential_theme: str
    nanda_philosophical_concept: str
    lived_experience_anchor: str
    key_takeaways: List[str]

class BawaAttabhawaEngine:
    def __init__(self, references_path: str = "REFERENCES.json"):
        self.references_path = Path(references_path)
        self.config = self._load_references()
        self.episodes: Dict[int, EpisodeSpec] = {}

    def _load_references(self) -> Dict[str, Any]:
        """Loads contextual metadata and directives from REFERENCES.json."""
        if not self.references_path.exists():
            # Fallback default configuration if file is missing locally
            return {
                "target_audience": {
                    "primary_address": "Seekers of Direct Reality",
                    "prohibited_terms": ["Gen Z", "Zoomers", "Youth Demographic"],
                    "tone_directive": "Humble, non-dogmatic, non-preachy, peer-to-peer, self-verifying"
                },
                "applied_context": {
                    "author": "U Ingar Soe",
                    "core_insight": "Philosophy must withstand armed conflict, exile, and physical confinement."
                }
            }
        with open(self.references_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def register_episode(self, episode: EpisodeSpec) -> None:
        """Registers an episode specification into the engine."""
        self.episodes[episode.episode_number] = episode

    def generate_prompt_payload(self, episode_number: int) -> str:
        """Synthesizes structured system directives and metadata into an LLM payload."""
        ep = self.episodes.get(episode_number)
        if not ep:
            raise ValueError(f"Episode {episode_number} has not been registered.")
        
        target_info = self.config.get("target_audience", {})
        author_info = self.config.get("applied_context", {})
        
        payload = {
            "system_instruction": (
                f"You are drafting an episode addressed strictly to '{target_info.get('primary_address')}'. "
                f"Do NOT use prohibited terms such as {target_info.get('prohibited_terms')}. "
                f"Synthesize Sayar Nanda Thein Zan's 'Definition and Truth of Life' with the lived experience "
                f"of {author_info.get('author')} (1988 NLD organizer, 1989-1991 ABSDF student fighter, "
                f"non-violent activist, and political prisoner survivor). "
                f"Tone directive: {target_info.get('tone_directive')}."
            ),
            "episode_metadata": asdict(ep),
            "reference_config": self.config
        }
        return json.dumps(payload, indent=2, ensure_ascii=False)

def initialize_default_curriculum() -> BawaAttabhawaEngine:
    engine = BawaAttabhawaEngine()
    
    # Episode 1 Core Seed
    engine.register_episode(EpisodeSpec(
        episode_number=1,
        title="The AI Era, Broken Templates, and the Search for Authentic Agency",
        existential_theme="Confronting automated logic, digital noise, and institutional decay.",
        nanda_philosophical_concept="Direct conscious experience (Dhamma) vs. calculated data outputs.",
        lived_experience_anchor="Transitioning from frontline student fighting to non-violent mental sovereignty.",
        key_takeaways=[
            "Algorithms calculate probabilities; human consciousness experiences direct reality and holds moral agency.",
            "Questioning broken authority is the first step toward self-verification.",
            "Deep contemplation of a single truth builds an internal sanctuary no external force can breach."
        ]
    ))
    return engine

if __name__ == "__main__":
    engine = initialize_default_curriculum()
    print("=== Bawa-Attabhawa-Engine Initialized ===")
    print(engine.generate_prompt_payload(1))
