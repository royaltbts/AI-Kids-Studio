"""
Simple OpenAI connectivity test.
"""

from backend.app.providers.openai_provider import OpenAIProvider

provider = OpenAIProvider()

response = provider.generate("""
Say hello in exactly one short sentence.
""")

print(response)
