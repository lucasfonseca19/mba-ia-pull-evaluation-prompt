"""
Testes automatizados para validação de prompts.
"""
import pytest
import yaml
from pathlib import Path

PROMPT_FILE = Path(__file__).parent.parent / "prompts" / "bug_to_user_story_v2.yml"
PROMPT_KEY = "bug_to_user_story_v2"

def load_prompts(file_path: str):
    """Carrega prompts do arquivo YAML."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

class TestPrompts:
    @pytest.fixture
    def prompt_data(self):
        """Carrega o prompt v2 usado na entrega."""
        prompts = load_prompts(PROMPT_FILE)
        assert PROMPT_KEY in prompts
        return prompts[PROMPT_KEY]

    @pytest.fixture
    def full_prompt_text(self, prompt_data):
        """Concatena system e user prompt para facilitar buscas textuais."""
        return "\n".join([
            prompt_data.get("system_prompt", ""),
            prompt_data.get("user_prompt", ""),
        ])

    def test_prompt_has_system_prompt(self, prompt_data):
        """Verifica se o campo 'system_prompt' existe e não está vazio."""
        assert "system_prompt" in prompt_data
        assert prompt_data["system_prompt"].strip()

    def test_prompt_has_role_definition(self, prompt_data):
        """Verifica se o prompt define uma persona (ex: "Você é um Product Manager")."""
        system_prompt = prompt_data.get("system_prompt", "").lower()

        assert "você é" in system_prompt
        assert "product manager" in system_prompt

    def test_prompt_mentions_format(self, full_prompt_text):
        """Verifica se o prompt exige formato Markdown ou User Story padrão."""
        prompt_text = full_prompt_text.lower()

        assert "markdown" in prompt_text
        assert "user story" in prompt_text
        assert "como um" in prompt_text
        assert "eu quero" in prompt_text
        assert "para que" in prompt_text

    def test_prompt_has_few_shot_examples(self, prompt_data):
        """Verifica se o prompt contém exemplos de entrada/saída (técnica Few-shot)."""
        user_prompt = prompt_data.get("user_prompt", "").lower()

        assert "exemplo 1" in user_prompt
        assert "exemplo 2" in user_prompt
        assert user_prompt.count("entrada:") >= 2
        assert user_prompt.count("saída:") >= 2

    def test_prompt_no_todos(self, full_prompt_text):
        """Garante que você não esqueceu nenhum `[TODO]` no texto."""
        assert "[TODO]" not in full_prompt_text

    def test_minimum_techniques(self, prompt_data):
        """Verifica (através dos metadados do yaml) se pelo menos 2 técnicas foram listadas."""
        techniques = prompt_data.get("techniques_applied", [])

        assert isinstance(techniques, list)
        assert len(techniques) >= 2
        assert "few_shot_learning" in techniques

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
