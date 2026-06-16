"""
Script para fazer push de prompts otimizados ao LangSmith Prompt Hub.

Este script:
1. Lê os prompts otimizados de prompts/bug_to_user_story_v2.yml
2. Valida os prompts
3. Faz push PÚBLICO para o LangSmith Hub
4. Adiciona metadados (tags, descrição, técnicas utilizadas)

SIMPLIFICADO: Código mais limpo e direto ao ponto.
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from langchain import hub
from langchain_core.prompts import ChatPromptTemplate

try:
    from .utils import load_yaml, check_env_vars, print_section_header
except ImportError:
    from utils import load_yaml, check_env_vars, print_section_header

load_dotenv()

LOCAL_PROMPT_KEY = "bug_to_user_story_v2"
PROMPT_FILE = Path(__file__).resolve().parent.parent / "prompts" / "bug_to_user_story_v2.yml"
REQUIRED_ENV_VARS = ["LANGSMITH_API_KEY", "USERNAME_LANGSMITH_HUB"]


def build_chat_prompt(prompt_data: dict) -> ChatPromptTemplate:
    """Cria o objeto LangChain que será publicado no LangSmith Hub."""
    prompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", prompt_data["system_prompt"]),
            ("human", prompt_data["user_prompt"]),
        ]
    )
    prompt_template.metadata = {
        "version": prompt_data.get("version"),
        "techniques_applied": prompt_data.get("techniques_applied", []),
    }

    return prompt_template


def build_prompt_readme(prompt_data: dict) -> str:
    """Monta uma descrição curta para aparecer junto do prompt no LangSmith."""
    techniques = ", ".join(prompt_data.get("techniques_applied", []))

    return (
        f"# {LOCAL_PROMPT_KEY}\n\n"
        f"{prompt_data.get('description', '')}\n\n"
        "## Técnicas aplicadas\n\n"
        f"{techniques}\n\n"
        "## Variáveis de entrada\n\n"
        "- `bug_report`: relato do bug que será convertido em User Story.\n"
    )


def push_prompt_to_langsmith(prompt_name: str, prompt_data: dict) -> bool:
    """
    Faz push do prompt otimizado para o LangSmith Hub (PÚBLICO).

    Args:
        prompt_name: Nome do prompt
        prompt_data: Dados do prompt

    Returns:
        True se sucesso, False caso contrário
    """
    try:
        prompt_template = build_chat_prompt(prompt_data)

        url = hub.push(
            prompt_name,
            prompt_template,
            new_repo_is_public=True,
            new_repo_description=prompt_data.get("description"),
            readme=build_prompt_readme(prompt_data),
            tags=prompt_data.get("tags", []),
        )

        print(f"✓ Prompt publicado com sucesso: {prompt_name}")
        print(f"✓ URL: {url}")
        return True
    except Exception as error:
        print(f"❌ Erro ao fazer push do prompt '{prompt_name}': {error}")
        return False


def validate_prompt(prompt_data: dict) -> tuple[bool, list]:
    """
    Valida estrutura básica de um prompt (versão simplificada).

    Args:
        prompt_data: Dados do prompt

    Returns:
        (is_valid, errors) - Tupla com status e lista de erros
    """
    errors = []

    required_fields = [
        "description",
        "system_prompt",
        "user_prompt",
        "version",
        "techniques_applied",
        "tags",
    ]

    for field in required_fields:
        value = prompt_data.get(field)
        if value is None or value == "" or value == []:
            errors.append(f"Campo obrigatório faltando ou vazio: {field}")

    system_prompt = prompt_data.get("system_prompt", "")
    user_prompt = prompt_data.get("user_prompt", "")
    full_prompt = f"{system_prompt}\n{user_prompt}"

    if "{bug_report}" not in user_prompt:
        errors.append("user_prompt deve conter a variável {bug_report}")

    if "[TODO]" in full_prompt:
        errors.append("Prompt ainda contém marcador [TODO]")

    techniques = prompt_data.get("techniques_applied", [])
    if not isinstance(techniques, list):
        errors.append("techniques_applied deve ser uma lista")
    elif len(techniques) < 2:
        errors.append("Prompt deve listar pelo menos 2 técnicas aplicadas")

    tags = prompt_data.get("tags", [])
    if not isinstance(tags, list):
        errors.append("tags deve ser uma lista")

    return len(errors) == 0, errors


def main():
    """Função principal"""
    print_section_header("Push do prompt otimizado")

    if not check_env_vars(REQUIRED_ENV_VARS):
        return 1

    prompt_file_data = load_yaml(str(PROMPT_FILE))
    if not prompt_file_data:
        return 1

    prompt_data = prompt_file_data.get(LOCAL_PROMPT_KEY)
    if not prompt_data:
        print(f"❌ Chave '{LOCAL_PROMPT_KEY}' não encontrada em {PROMPT_FILE}")
        return 1

    is_valid, errors = validate_prompt(prompt_data)
    if not is_valid:
        print("❌ Prompt inválido:")
        for error in errors:
            print(f"   - {error}")
        return 1

    username = os.getenv("USERNAME_LANGSMITH_HUB")
    prompt_name = f"{username}/{LOCAL_PROMPT_KEY}"

    print(f"Arquivo local: {PROMPT_FILE}")
    print(f"Destino LangSmith: {prompt_name}")
    print("Publicação: pública")

    return 0 if push_prompt_to_langsmith(prompt_name, prompt_data) else 1


if __name__ == "__main__":
    sys.exit(main())
