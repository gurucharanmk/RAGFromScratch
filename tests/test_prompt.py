from src.prompt import Prompt


def test_prompt_construct_basic():
    prompt = Prompt(human_message="Test question")
    result = prompt.construct_prompt()
    assert "Human: Test question" in result


def test_prompt_construct_full():
    prompt = Prompt(
        system_message="System context",
        ai_message="AI response",
        human_message="Test question",
    )
    result = prompt.construct_prompt()
    assert "System: System context" in result
    assert "AI: AI response" in result
    assert "Human: Test question" in result
