"""
Script para fazer pull de prompts do LangSmith Prompt Hub.

Este script:
1. Conecta ao LangSmith usando credenciais do .env
2. Faz pull dos prompts do Hub
3. Salva localmente em prompts/bug_to_user_story_v1.yml

SIMPLIFICADO: Usa serialização nativa do LangChain para extrair prompts.
"""

import sys
from pathlib import Path
from dotenv import load_dotenv
from langchain import hub
from langchain_core.prompts import ChatPromptTemplate

try:
    from .utils import save_yaml, check_env_vars, print_section_header
except ImportError:
    from utils import save_yaml, check_env_vars, print_section_header

load_dotenv()

HUB_PROMPT_NAME = "leonanluppi/bug_to_user_story_v1"
LOCAL_PROMPT_KEY = "bug_to_user_story_v1"
OUTPUT_FILE = Path(__file__).resolve().parent.parent / "prompts" / "bug_to_user_story_v1.yml"
REQUIRED_ENV_VARS = ["LANGSMITH_API_KEY"]


def _serialize_prompt(prompt: ChatPromptTemplate) -> dict:
    """Converte o ChatPromptTemplate do Hub para o YAML da entrega."""
    system_prompt = prompt.messages[0].prompt.template
    user_prompt = prompt.messages[1].prompt.template

    return {
        LOCAL_PROMPT_KEY: {
            "description": "Prompt para converter relatos de bugs em User Stories",
            "system_prompt": system_prompt,
            "user_prompt": user_prompt or "{bug_report}",
            "version": "v1",
            "tags": ["bug-analysis", "user-story", "product-management"],
        }
    }


def pull_prompts_from_langsmith():
    """Faz pull do prompt inicial no LangSmith e salva em YAML local."""
    try:
        print_section_header("Pull do prompt inicial")
        print(f"Puxando prompt do LangSmith Hub: {HUB_PROMPT_NAME}")

        prompt = hub.pull(HUB_PROMPT_NAME)
        prompt_data = _serialize_prompt(prompt)

        if not save_yaml(prompt_data, str(OUTPUT_FILE)):
            return False

        print(f"Prompt salvo em: {OUTPUT_FILE}")
        return True
    except Exception as error:
        print(f"Erro ao fazer pull do prompt '{HUB_PROMPT_NAME}': {error}")
        return False


def main():
    """Função principal"""
    if not check_env_vars(REQUIRED_ENV_VARS):
        return 1

    return 0 if pull_prompts_from_langsmith() else 1


if __name__ == "__main__":
    sys.exit(main())
