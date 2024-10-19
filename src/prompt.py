from typing import Optional
from pydantic import BaseModel, Field


class Prompt(BaseModel):
    """
    Prompt class for constructing prompts.

    This class provides a structure for creating prompts with optional system and AI messages,
    and a required human message.

    Attributes:
        system_message (Optional[str]): An optional system message to set the context.
        ai_message (Optional[str]): An optional AI message to include in the prompt.
        human_message (str): The required human message or query.

    Examples:
        >>> prompt = Prompt(
        ...     system_message="You are a helpful AI assistant.",
        ...     ai_message="I'm ready to help!",
        ...     human_message="Your question here"
        ... )
        >>> print(prompt.construct_prompt())
        System: You are a helpful AI assistant.
        AI: I'm ready to help!
        Human: Your question here
    """

    system_message: Optional[str] = Field(None, description="System message")
    ai_message: Optional[str] = Field(None, description="AI message")
    human_message: str = Field(..., description="Human message")

    def construct_prompt(self) -> str:
        """
        Construct the full prompt by combining all provided messages.

        Returns:
            str: The constructed prompt string.

        Examples:
            >>> prompt = Prompt(
            ...     system_message="You are a helpful AI assistant.",
            ...     human_message="What's the weather like today?"
            ... )
            >>> print(prompt.construct_prompt())
            System: You are a helpful AI assistant.
            Human: What's the weather like today?
        """
        prompt_parts: list[str] = []
        if self.system_message:
            prompt_parts.append(f"System: {self.system_message}")
        if self.ai_message:
            prompt_parts.append(f"AI: {self.ai_message}")
        prompt_parts.append(f"Human: {self.human_message}")
        return "\n".join(prompt_parts)
